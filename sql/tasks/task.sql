SELECT band_id, name, year
FROM band
WHERE name = 'Led Zeppelin';


SELECT *
FROM album
WHERE band_id = 388;


SELECT * FROM album WHERE band_id IN (SELECT band_id FROM band WHERE name = 'Metallica');


SELECT band_id, band_name
FROM ( 
	SELECT band_id, name as band_name  
	FROM band) as table_1;


SELECT *
FROM album
WHERE band_id IN (
	SELECT band_id
	FROM band
	WHERE name = 'Led Zeppelin'
);


SELECT  a,
		b,
		coalesce(a,0)+coalesce(b,0) as sum,
		a=b
FROM mytable_int;


SELECT * 
FROM mytable_int
WHERE  a <> b
	OR (a IS NULL     AND b IS NOT NULL)
	OR (a IS NOT NULL AND b IS NULL);


SELECT * 
FROM mytable_int
WHERE  a <> 1 
	OR a IS NULL;


SELECT * 
FROM band
WHERE  name = 'Icarus' 
	AND  year IS NULL;


SELECT * 
FROM band
WHERE  band_id IN (
	SELECT id
	FROM list1
);


SELECT band_id, name
FROM band
WHERE  band_id NOT IN (
	SELECT id
	FROM list1
	WHERE id IS NOT NULL
);


SELECT COUNT(*)
FROM album
WHERE band_id = 93;


SELECT 93 as band_id, 
	COUNT(*)
FROM album
WHERE band_id = 93;


SELECT band_id, 
	COUNT(*) as band_count
FROM album
GROUP BY band_id;


SELECT band_id, 
	year,
	COUNT(*)
FROM album
WHERE year > 2000
GROUP BY band_id, year; --счетчик одинаковых строк band_id year


SELECT COUNT(*)
FROM album
WHERE band_id IN (93, 192);
--25


SELECT band_id, 
	COUNT(*) AS band_count
FROM album
WHERE band_id IN (93, 192) 
	-- AND COUNT(*) = 11 count сразу считается отсюда ошибка надо использовать HAVING
GROUP BY band_id
HAVING COUNT(*) = 11;


SELECT band_id 
	--COUNT(*) AS band_count
FROM album
GROUP BY band_id
HAVING COUNT(*) = 1;


SELECT COUNT(*) as count1,
	COUNT(n_albums) as count2, --счет отличных от NULL
	SUM(n_albums)
FROM band_extended;


SELECT band_id,
	COUNT(*) AS band_count
FROM album
--WHERE band_id is NULL
GROUP BY 1;


SELECT MIN(year), 
	MAX(year)
FROM album;


SELECT MIN(counter), MAX(counter)
FROM (
	SELECT band_id, COUNT(*) AS counter
	FROM album
	GROUP BY 1
) as table_1;
-- 1/204


SELECT COUNT(*), COUNT(DISTINCT album_id), COUNT(DISTINCT band_id)
FROM album;
--121918,121918,36882

SELECT *
FROM band
WHERE band_id NOT IN (
	SELECT band_id
	FROM album
	WHERE band_id IS NOT NULL
);
-- группы без альбома


