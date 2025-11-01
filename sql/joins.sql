/* СОЕДИНЕНИЕ ТАБЛИЦ */

SELECT *
FROM album
WHERE band_id IN (
	SELECT band_id
	FROM band
);

SELECT a.*
FROM album as a
INNER JOIN band as b
	ON a.band_id = b.band_id;

-- M:1
SELECT a.album_id, a.name,
	a.band_id, b.name as band_name
FROM album as a
INNER JOIN band as b
	ON a.band_id = b.band_id;

-- 1:M
SELECT b.band_id, b.name as band_name,
	a.album_id, a.name
FROM band as b
INNER JOIN album as a
	ON a.band_id = b.band_id;


SELECT b.name as band_name
FROM band as b
INNER JOIN album as a
	ON b.band_id = a.band_id;


SELECT *
FROM band
WHERE name = 'Led Zeppelin';

/* Альбомы группы */
SELECT b.*, a.album_id, a.name, a.band_id, a.year
FROM band as b --муз группа
INNER JOIN album as a
	ON a.band_id = b.band_id
WHERE b.name = 'Led Zeppelin';

/* Соед 2-3 таб M:M */
SELECT *
FROM band as b -- 1:M band:band_person
INNER JOIN band_person as b_p
	ON b.band_id = b_p.band_id;
-- 257_474

SELECT COUNT(*) FROM band;
-- 82_928

SELECT COUNT(*) FROM band_person;
-- 257_474

SELECT b.band_id,
	b.name as band_name,
	p.person_id,
	p.name as person_name
FROM band as b -- 1:M band:band_person
	INNER JOIN band_person as b_p
		ON b.band_id = b_p.band_id
	INNER JOIN person as p
		ON p.person_id = b_p.person_id
	WHERE b.name = 'Metallica';
-- p.name =''
-- 257_474 count()

/* Проверка на первичный ключ */
SELECT  COUNT(*), COUNT(DISTINCT band_id)
FROM band;
-- если совпадают колонка уникальна band_id

/* Проверка на внешний ключ */
SELECT COUNT(*)
FROM album
WHERE band_id NOT IN (
	SELECT band_id
	FROM band
	WHERE band_id IS NOT NULL
) OR band_id IS NULL;
--0 значит все ок


SELECT 
	a.album_id, a.name, a.band_id, 
	b.name as band_name
FROM album as a -- LEFT OUTER указывает что album основной строки не потеряются
LEFT OUTER JOIN band as b
	ON a.band_id = b.band_id; -- band_name будет NULL если не найдется по band_id


SELECT 
	b.band_id, b.name as band_name,
	a.album_id, a.name as album_name
FROM band as b 
LEFT OUTER JOIN album as a
	ON a.band_id = b.band_id -- album_id и album_name будет NULL если не найдется по band_id
	AND a.name = 'Master of Puppets' --отобразит band и там где 'Master of Pippets' так как внешнее соединение таблиц
WHERE a.name = 'Master of Puppets'; --из-зв фильтрации отобразит только 1 строку где Master of Pippets


/* Вариации синтаксиса одинаковые варианты */
SELECT *
FROM album as a
INNER JOIN band as b --через INNER
	ON a.band_id = b.band_id
WHERE b.name = 'Metallica';

SELECT * 
FROM album as a, band as b
WHERE a.band_id = b.band_id
	AND b.name = 'Metallica';

/* Вариации синтаксиса одинаковые варианты 2 */
SELECT *
FROM album as a
INNER JOIN band as b  --убрать INNER
	ON a.band_id = b.band_id;

SELECT *
FROM album as  a
JOIN band as b
	ON a.band_id = b.band_id;
	
/* Вариации синтаксиса одинаковые варианты 3 */
SELECT *
FROM album as a
LEFT OUTER JOIN band as b --убрать OUTER
	ON a.band_id = b.band_id;

SELECT *
FROM album as a
LEFT JOIN band as b
	ON a.band_id = b.band_id;

/* LEFT указывает какая таблица не должна терять
строки в данном случае слева то есть та что в FROM 
Есть еще RIGHT
*/


/* Так если соотвестий не будет может быть NAME АЛЬБОМА NULL ИЛИ ГРУППА НАЗВАНИЕ null
*/
SELECT 
	a.album_id, a.name,
	a.band_id as b_id1,
	b.band_id as b_id2,
	b.name as band_name
FROM album as a
FULL OUTER JOIN band as b
	ON a.band_id = b.band_id;
	--AND b.name is NULL


/* self join соединение таб сама собой
1 духовые parent null
но 24 инструмент с parent 1
иерархическая структура в одной таблице
*/
SELECT *
FROM music_instrument;
--WHERE id = 1;

SELECT 
	a.id, a.name, a.parent_id,
	b.name as parent_name
FROM music_instrument as a
LEFT JOIN music_instrument as b
	ON b.id = a.parent_id
ORDER BY a.id;

/* 2 родителя */
SELECT 
	a.id, a.name, a.parent_id,
	b.name as parent_name,
	c.id as gp_id, c.name as gp_name
FROM music_instrument as a
LEFT JOIN music_instrument as b ON b.id = a.parent_id
LEFT JOIN music_instrument as c ON c.id = b.parent_id
ORDER BY a.id;

/* дети */
SELECT  
	a.id, a.name,
	b.id as child_id, 
	b.name as child_name
FROM music_instrument as a
LEFT JOIN music_instrument as b ON b.parent_id = a.id
WHERE a.parent_id IS NULL
ORDER BY a.id;

/* 2 ребенка */
SELECT  
	a.id, a.name,
	b.id as child_id, 
	b.name as child_name,
	c.id as grand_id,
	c.name as grand_name
FROM music_instrument as a
LEFT JOIN music_instrument as b ON b.parent_id = a.id
LEFT JOIN music_instrument as c ON c.parent_id = b.id
WHERE a.parent_id IS NULL
ORDER BY a.id;


SELECT 
	a.album_id, a.name,
	a.band_id as b_id1,
	b.band_id as b_id2,
	b.name as band_name
FROM album as a
CROSS JOIN band as b
LIMIT 10;


SELECT *
FROM album as a
CROSS JOIN band as b;

SELECT *
FROM 
	album as a, 
	band as b;