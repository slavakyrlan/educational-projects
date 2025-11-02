/*
INSERT вставка строк
UPDATE обн
DELETE удаление строк
*/

INSERT INTO band(band_id, name, year, comment) -- можно не указывать comment будет null
	VALUES (303, 'The Beatles', 1957, '');

INSERT INTO band -- можно не указывать вообще колонки
	VALUES (303, 'The Beatles', 1957, '');

--INSERT INTO band(band_id, name, year)
--SELECT ...
--FROM another_table;

COPY band FROM '/tmp/band'; -- в какую таблицу из фала взять и загрузить в таблицу

/* сделать ставку при создании таблицы
CREATE TABLE band AS
SELECT ...
FROM another_table; */

UPDATE band
SET comment = 'Rock' -- название колонки и на что меняем
WHERE name = 'Metallica';

UPDATE band
SET comment = ''; --заменит все данные на '' ОСТОРОЖНО!

-- ПЕРЕНОС данных из одной таблицы в другую, так в band обновляем 
UPDATE band as b
SET name = t2.name
FROM band_old as t2
WHERE t.band_id = t2.band_id;


/*DELETE Уудаление строк*/
DELETE
FROM band
WHERE name = 'Metallica';




