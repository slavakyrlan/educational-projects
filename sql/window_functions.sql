/* Оконные функции */
-- SUM(n_albums) OVER (...)

--1 сценарий детальные данные + агрегация
SELECT SUM(n_albums) as total
FROM band_extended
WHERE band_id IN (303,93,192);
--- total 42

SELECT band_id, name, year, n_albums
FROM band_extended
WHERE band_id IN (303,93,192);
-- 3 строки 

SELECT 
	d.band_id, d.name, d.year, d.n_albums, 
	a.total,
	d.n_albums * 100.00 / a.total as pct_albums
FROM band_extended as d
CROSS JOIN (
	SELECT SUM(n_albums) as total
	FROM band_extended
	WHERE band_id IN (303,93,192)
) as a
WHERE d.band_id IN (303,93,192);
-- 3 строки с total одинаковым

--Теперь с помощью оконной функции
SELECT 
	d.band_id, d.name, d.year, d.n_albums, 
	--SUM(d.n_albums) OVER() as total,
	d.n_albums * 100.00 / SUM(d.n_albums) OVER() as pct_albums
FROM band_extended as d
WHERE band_id IN (303,93,192);

	
------------------------------------------
--Оконные функции добавляем partition by--
------------------------------------------
/* 
SUM(n_albums) OVER()
AVG(n_albums) OVER() - ср значение

COUNT(*) OVER() - подсчет количества строк
COUNT(n_albums) OVER() - подсчет количества строк, где эта строка отличается от NULL

MIN(n_albums) OVER()
MAX(n_albums) OVER()
*/
--Подсчет количества лет с первого альбома

SELECT band_id, MIN(year) as min_year
FROM album
WHERE band_id IN (93, 192)
GROUP BY band_id;

SELECT 
	album_id, name, band_id, year,
	MIN(year) OVER(PARTITION BY band_id) as min_year, --PARTITION теперь будет оконная функция MIN работать не со всеми а отдельно с 1 и 2
	year - MIN(year) OVER(PARTITION BY band_id) as year_since_1st
FROM album
WHERE band_id IN (93, 192);

--для красоты
SELECT album_id, name, band_id, year, min_year, year - min_year as year_since_1st
FROM(
	SELECT 
		album_id, name, band_id, year,
		MIN(year) OVER(PARTITION BY band_id) as min_year
	FROM album
	WHERE band_id IN (93, 192)
);

-- БЕЗ оконной функции:
SELECT 
	d.album_id, d.name, d.band_id, d.year,
	a.min_year, d.year - a.min_year as year_since_1st
FROM album as d
INNER JOIN (
	SELECT band_id, MIN(year) as min_year
	FROM album
	WHERE band_id IN (93, 192)
	GROUP BY band_id
) as a 
	ON a.band_id = d.band_id
WHERE d.band_id IN (93, 192);
-- ОБРАЩЕНИЕ К 1 таблице несколько раз => оконная функция


-----------------------------------
----РЕЗЮМЕ ПО ОКОННЫМ ФУНКЦИЯМ-----
-----------------------------------
/*
Когда нужны оконные функции
1. детальные данные + агрегированные данные
2. кумулятивные суммы
3. скользящие функции
4. предыдущие и последующие строки
5. нумерация  иранжирование
*/