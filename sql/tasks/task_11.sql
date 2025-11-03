-- 1 шаг

SELECT 
	a.album_id, a.name, b.band_id, b.name,
	CASE 
		WHEN a.name=b.name THEN 1 ELSE 0
	END as names_match_flag
FROM album as a
INNER JOIN band as b
	ON a.band_id = b.band_id;

-- 2 шаг

SELECT COUNT(*)
FROM (
	SELECT 
		a.album_id, a.name, b.band_id, b.name,
		CASE 
			WHEN a.name=b.name THEN 1 ELSE 0
		END as names_match_flag
	FROM album as a
	INNER JOIN band as b
		ON a.band_id = b.band_id
)
WHERE names_match_flag=1;
-- 6616

SELECT names_match_flag, COUNT(*)
FROM (
	SELECT 
		a.album_id, a.name, b.band_id, b.name,
		CASE 
			WHEN a.name=b.name THEN 1 ELSE 0
		END as names_match_flag
	FROM album as a
	INNER JOIN band as b
		ON a.band_id = b.band_id
)
GROUP BY 1;
-- 0/115308 1/6616 
		
-- 3 шаг
SELECT COUNT(*)
FROM album
WHERE name IN (
	SELECT name
	FROM band
);
-- 15277

-- берем album и с помощью внешнего соединения со списком муз групп это М:1
SELECT *
FROM album as a
LEFT OUTER JOIN (
	SELECT DISTINCT name
	FROM band
) as b
	ON a.name = b.name;

-- БЕЗ null
SELECT *
FROM album as a
JOIN (
	SELECT DISTINCT name
	FROM band
) as b
	ON a.name = b.name;

SELECT COUNT(*), SUM(bang_FLAG)
	FROM (
		SELECT 
			a.*,
			CASE WHEN b.name IS NOT NULL THEN 1 ELSE 0 END as bang_FLAG
		FROM album as a
		LEFT OUTER JOIN (
			SELECT DISTINCT name
			FROM band
		) as b
		ON a.name = b.name
) as t1;
-- 15277


--сразу ответ для двух шагов 15277, 6615
SELECT COUNT(*), SUM(bang_FLAG), SUM(names_match_flag)
	FROM (
		SELECT 
			a.*,
			CASE WHEN b.name IS NOT NULL THEN 1 ELSE 0 END as bang_FLAG,
			CASE WHEN a.name=b2.name THEN 1 ELSE 0 END as names_match_flag
		FROM album as a
		INNER JOIN band as b2 ON a.band_id = b2.band_id
		LEFT JOIN (
			SELECT DISTINCT name
			FROM band
		) as b ON a.name = b.name
) as t1;


SELECT 
	a.*,
	CASE WHEN b.name IS NOT NULL THEN 1 ELSE 0 END as bang_FLAG
FROM album as a
LEFT JOIN (
	SELECT DISTINCT name
	FROM band
) as b ON a.name = b.name;

--альтернатива

SELECT 
	a.*,
	CASE WHEN a.name IN (SELECT DISTINCT name FROM band)
		THEN 1 ELSE 0 END as bang_FLAG
FROM album as a

