SELECT COUNT(*) FROM album;
--121 918
SELECT SUM(n_albums) FROM band_extended;
--121 918

-- 1 расхождение -100 нет в альбомах но есть в band_extended с 11 альбомами несоотвествие
SELECT * FROM album WHERE band_id=-100;
--0 (no rows)
SELECT n_albums FROM band_extended WHERE band_id=-100;
--25

-- 2 расхождение для 93 в альбомах 11, а в band_extended null
SELECT * FROM album WHERE band_id=93;
-- 11 альбомов
SELECT n_albums FROM band_extended WHERE band_id=93;
-- null

-- 3 расхождение
SELECT * FROM album WHERE band_id IN (SELECT band_id FROM band WHERE name = 'Queen');
--14 строк id 192
SELECT n_albums FROM band_extended WHERE name = 'Queen';
--null

/* ИТОГО
BAND_ID: -100, 93, 192
*/

SELECT band_id, COUNT(*) AS album_count
FROM album
GROUP BY 1;

SELECT band_id, n_albums AS album_count
FROM band_extended
WHERE n_albums > 0 --отбросим нули
;


SELECT * FROM band_extended WHERE band_id = 1047484;
SELECT * FROM album WHERE band_id = 1047484;
-- 0 в оба


-----
SELECT band_id, COUNT(*) AS album_count
FROM album
WHERE band_id = 10302
GROUP BY 1;

SELECT band_id, n_albums AS album_count
FROM band_extended
WHERE n_albums > 0 --отбросим нули
	AND band_id = 10302;
-- 15 albums

--------- сравнение двух таблиц

SELECT band_id, COUNT(*) AS album_count
FROM album
GROUP BY 1
EXCEPT
SELECT band_id, n_albums AS album_count
FROM band_extended
WHERE n_albums > 0; 
-- 93 и 192 не хватает -100 это 1 запрос минус второй, поменяем
SELECT band_id, n_albums AS album_count
FROM band_extended
WHERE n_albums > 0
EXCEPT
SELECT band_id, COUNT(*) AS album_count
FROM album
GROUP BY 1;
-- -100


---------------

SELECT *
FROM (
	SELECT band_id, n_albums AS album_count
	FROM band_extended
	WHERE n_albums > 0 OR n_albums IS NULL
	) AS table_1
FULL OUTER JOIN (
	SELECT band_id, COUNT(*) AS album_count
	FROM album
	GROUP BY 1
	) AS table_2
ON table_1.band_id = table_2.band_id
WHERE table_1.album_count <> table_2.album_count
	OR (table_1.album_count IS NULL AND table_2.album_count IS NOT NULL)
	OR (table_1.album_count IS NOT NULL AND table_2.album_count IS NULL);

-- 3 строки
-- ЗАПИСЬ данных в таблицу для след шага
CREATE TABLE table_comparison AS
SELECT 
	table_1.band_id as band_id_band_extended,
	table_1.album_count as album_count_band_extended,
	table_2.band_id as band_id_album,
	table_2.album_count as album_count_album
FROM (
	SELECT band_id, n_albums AS album_count
	FROM band_extended
	WHERE n_albums > 0 OR n_albums IS NULL
	) AS table_1
FULL OUTER JOIN (
	SELECT band_id, COUNT(*) AS album_count
	FROM album
	GROUP BY 1
	) AS table_2
ON table_1.band_id = table_2.band_id
WHERE table_1.album_count <> table_2.album_count
	OR (table_1.album_count IS NULL AND table_2.album_count IS NOT NULL)
	OR (table_1.album_count IS NOT NULL AND table_2.album_count IS NULL);

SELECT * FROM table_comparison;

--------------------------
--устранение расхождений--
--------------------------
--примем что в band_extended ошибки исправляем по album
-- 1. band_id = 93 - UPDATE, исправляем в строке album_count band_extended путем взятия ее из album
UPDATE band_extended as band_alias
SET n_albums = table_1.album_count
FROM (
	SELECT band_id, COUNT(*) AS album_count
	FROM album
	GROUP BY 1
) as table_1
WHERE band_alias.band_id = table_1.band_id
	AND  band_alias.band_id IN (
		SELECT band_id_band_extended
		FROM table_comparison
		WHERE band_id_band_extended IS NOT NULL
			AND band_id_album IS NOT NULL
	);
	
-- строка по 1 пункту
SELECT band_id_band_extended
FROM table_comparison
WHERE band_id_band_extended IS NOT NULL
	AND band_id_album IS NOT NULL;

-- 2. band_id = -100 - *DELETE*, так как нет в albums, либо написать 0 в count_albums
SELECT *
FROM table_comparison
WHERE band_id_band_extended IS NOT NULL
	AND band_id_album IS NULL;

--SELECT *
DELETE
FROM band_extended
WHERE band_id IN (
	SELECT band_id_band_extended
	FROM table_comparison
	WHERE band_id_band_extended IS NOT NULL
		AND band_id_album IS NULL
);


-- 3. band_id = 192 INSERT так как данные нужно перенести из albums в band_extended
SELECT *
FROM band_extended
LIMIT 10;

SELECT band_id_album
FROM table_comparison
WHERE band_id_band_extended IS NULL
	AND band_id_album IS NOT NULL;

INSERT INTO band_extended(band_id, name, year, comment, n_albums)
SELECT 
	b.band_id, b.name, b.year, b.comment,
	COALESCE(albums.album_count,0) as n_albums
	--,COALESCE(songs.songs_count,0) as n_songs
FROM band as b
LEFT OUTER JOIN ( SELECT band_id, COUNT(*) AS album_count FROM album GROUP BY 1 ) AS albums
ON  albums.band_id = b.band_id
--LEFT OUTER JOIN ( SELECT band_id, COUNT(*) AS song_count FROM song GROUP BY 1 ) AS songs
--ON  songs.band_id = b.band_id
WHERE b.band_id IN (
	SELECT band_id_album
	FROM table_comparison
	WHERE band_id_band_extended IS NULL
		AND band_id_album IS NOT NULL
);



---------------------
--восстановление БД--
---------------------
SELECT COUNT(*) FROM band_extended_backup;
DELETE FROM band_extended;
INSERT INTO band_extended SELECT * FROM band_extended_backup;
