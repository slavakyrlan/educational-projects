/*
ORDER BY для window functions
*/

SELECT 
	album_id, name, band_id , year, total_sales,
	SUM(total_sales) OVER (	
		ORDER BY year  --чтобы было понятно в каком порядке соортировать  - важна!
		ROWS BETWEEN UNBOUNDED PRECEDING  -- нижняя граница UNBOUNDED PRECEDING все предыдущие строки, а вверхник CURRENT ROW - текущая строка
				 AND CURRENT ROW -- какие строки участвуют в агрегации данных
	) as cumulative_sales
FROM album_sales
WHERE band_id = 1811
;
-- 1 ORDER BY - по ошибке можно забыть!
-- будут просуммированы рандомно
SELECT 
	album_id, name, band_id , year, total_sales,
	SUM(total_sales) OVER (	
		ROWS BETWEEN UNBOUNDED PRECEDING  -- нижняя граница UNBOUNDED PRECEDING все предыдущие строки, а вверхник CURRENT ROW - текущая строка
				 AND CURRENT ROW -- какие строки участвуют в агрегации данных
	) as cumulative_sales
FROM album_sales
WHERE band_id = 1811
;
-- 2 ORDER BY оконной функции может отличаться от финального ORDER BY

SELECT 
	album_id, name, band_id , year, total_sales,
	SUM(total_sales) OVER (	 -- cначала кумулятивная
		ORDER BY year 
		ROWS BETWEEN UNBOUNDED PRECEDING  
				 AND CURRENT ROW
	) as cumulative_sales
FROM album_sales
WHERE band_id = 1811
ORDER BY name -- потом по имени сортировка
;
-- 3 для проверки удобно указывать финальный ORDER BY таким же, как в окнонной функции

SELECT 
	album_id, name, band_id , year, total_sales,
	SUM(total_sales) OVER (	 -- cначала кумулятивная
		ORDER BY year 
		ROWS BETWEEN UNBOUNDED PRECEDING  
				 AND CURRENT ROW
	) as cumulative_sales
FROM album_sales
WHERE band_id = 1811
ORDER BY year -- потом по имени сортировка
;

--вернемся к старому запросу
SELECT 
	album_id, name, band_id , year, total_sales,
	SUM(total_sales) OVER (
		PARTITION BY band_id --сумма по соответствию band_id, кумулятивная сумма для каждой группы
		ORDER BY year  --чтобы было понятно в каком порядке соортировать  - важна!
		ROWS BETWEEN UNBOUNDED PRECEDING  -- нижняя граница UNBOUNDED PRECEDING все предыдущие строки, а вверхник CURRENT ROW - текущая строка
				 AND CURRENT ROW -- какие строки участвуют в агрегации данных
	) as cumulative_sales
FROM album_sales
WHERE band_id in (93, 192)
ORDER BY band_id, year -- сначала по band_id потом по year, чтоб не было смешивания
;

-- две оконные функции и как влияет order
SELECT 
	album_id, name, band_id , year, total_sales,
	SUM(total_sales) OVER (ORDER BY year 
		ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
	) as cumulative_sales,
	COUNT(*) OVER (ORDER BY total_sales DESC  --ранжирование строк
		ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
	) as sales_rank
FROM album_sales
WHERE band_id = 1811;
-- 4 Если нужен финальный ордер указываем явно
-- 5 если не нужен финальный ордер то не указываем его
-- любая сортировака напригает запрос + время
-- 6 осторожно с значениями NULL


--что если в строке year NULL считать в начале, в конце или пропустить
SELECT a
FROM mytable_int
ORDER BY a;
-- 1 2 3 22 NULL

SELECT a
FROM mytable_int
ORDER BY a NULLS LAST;
-- 1 2 3 22 NULL

SELECT a
FROM mytable_int
ORDER BY a DESC;
-- NULL 22 3 2 1

SELECT a
FROM mytable_int
ORDER BY a NULLS FIRST;
-- NULL 1 2 3 22

SELECT a
FROM mytable_int
ORDER BY a DESC NULLS FIRST;
-- NULL 22 3 2 1

SELECT a
FROM mytable_int
ORDER BY a DESC NULLS LAST;
-- 22 3 2 1 NULL

-- 7 Желатнльео делать сортировку однозначной
SELECT 
	album_id, name, band_id , year, total_sales,
	SUM(total_sales) OVER (
		PARTITION BY band_id 
		ORDER BY year
		ROWS BETWEEN UNBOUNDED PRECEDING
				 AND CURRENT ROW
	) as cumulative_sales
FROM album_sales
WHERE band_id in (93, 192)
ORDER BY year
;
-- если одинаковые года(ORDER BY year), то там рандомно расположится строка, устронить вернуться и дополнить доп данными, чтобы знать порядок выхода альбомов
-- если нет то лучше в ORDER BY year добавить еще album_id - уникальный, всегда будет порядок без неопределенностей 
