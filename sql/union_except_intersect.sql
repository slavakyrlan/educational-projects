/* Операторы множеств */

-- UNION склейка строк из обеих таблиц
SELECT *
FROM album
UNION ALL
SELECT *
FROM album_archive;


-- UNION устраняет дубликаты (убрать ALL)

-- названия второго селектора игнорируются
SELECT *
FROM album_small
UNION ALL
SELECT *
FROM album_archive
ORDER BY name;

-- список строк в разных таблицах
SELECT 'album' as table_name, COUNT(*) FROM album
UNION ALL
SELECT 'band' as table_name, COUNT(*) FROM band
UNION ALL
SELECT 'person' as table_name, COUNT(*) FROM person;

-- EXCEPT ALL (MINUS) вычитает строки ИСКЛЮЧАЯЯ
/* 
в 1 таблице 3 строки одинаковые
во 2 таблице такая же строка 1
EXCEPT ALL => вернет 2 строки одинаковые
без ALL НИЧЕГО не вернет - устраняет дубликаты и вычитают запросы, все 3 строки исключены будут
*/
SELECT *
FROM album
EXCEPT ALL
SELECT *
FROM album_archive;

-- МОЖНО через WHERE NOT IN  сделать
SELECT *
FROM album_small
WHERE (album_id, name, band_id, year) NOT IN (
	SELECT album_id, name, band_id, year
	FROM album_archive
);

-- NULL В СТРОКЕ при 2 случае помешает получить правильный результат!


-- INTERSECT пересечение
/* в 1 таблице 3 одинаковые строки, а во втрой 2
тем самым вернет те строки что есть в обоих то есть 2 строки вернет
если убрать ALL - УСТРАНЕНИЕ дубликатов строк - 1 строку вернет
*/
SELECT *
FROM album_small
INTERSECT ALL
SELECT *
FROM album_archive;

-- второй способ через IN

SELECT *
FROM album_small
WHERE (album_id, name, band_id, year) IN (
	SELECT album_id, name, band_id, year
	FROM album_archive
);

-- ВТРОЙ способ не сработает если строка какая-та будет NULL, МОЖНО использовать coalesce(year,-1)


