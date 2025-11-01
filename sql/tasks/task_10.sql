-- 1 шаг
CREATE TABLE band_extended_backup AS
SELECT * FROM band_extended;
--82928 
SELECT COUNT(*)
FROM band_extended;

--для восстановления резерва
DELETE FROM band_extended; --все строки удалены
INSERT INTO band_extended SELECT * FROM band_extended_backup; --вставка в существующую таблицу


-- 2 шаг

SELECT *
FROM band_extended
WHERE name = 'Metallica';
--band id = 93 
--n_albums = 11

SELECT COUNT(*)
FROM album
WHERE band_id = 93;
--11

SELECT SUM(n_albums) FROM band_extended;
-- 121 918

SELECT COUNT(*) FROM album;
-- 121 918

-- 3 шаг
UPDATE band_extended
SET n_albums = NULL
WHERE name = 'Metallica';

SELECT * FROM band_extended WHERE name = 'Metallica';
SELECT SUM(n_albums) FROM band_extended;
--121 907
SELECT COUNT(*) FROM album;
--121 918

-- 4 шаг
SELECT * FROM band_extended WHERE band_id = -100;

INSERT INTO band_extended
VALUES (-100,'My Test',2000,'My comment',25,54);

SELECT COUNT(*)
FROM band_extended;
--82928 -> 82929


-- 5 шаг
SELECT * FROM band_extended WHERE name = 'Queen';
DELETE FROM band_extended WHERE name = 'Queen';
SELECT COUNT(*) FROM band_extended;
--82928 - строка удалена
