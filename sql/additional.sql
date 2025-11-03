/*
CASE
CASE 
	WHEN условие_1 THEN значение 1
	WHEN условие_2 THEN значение 2
	WHEN условие_3 THEN значение 3
	ELSE				значение 4
END
*/
SELECT 
	album_id, name, band_id,
	CASE WHEN band_id=93 THEN 1 ELSE 0 END as b_93,
	CASE WHEN band_id=192 THEN 1 ELSE 0 END as b_192
FROM album as a;

SELECT 
	album_id, name, band_id,
	CASE band_id WHEN 93 THEN 1 ELSE 0 END as b_93,
	CASE band_id WHEN 192 THEN 1 ELSE 0 END as b_192
FROM album as a
WHERE band_id IN (93, 192);


--полезно
SELECT person_id, name, position (' ' in name) as space_position,
	substring(name, 1, position (' ' in name)-1) as first_name
FROM person
WHERE name like '% %'
UNION ALL
SELECT person_id, name, position (' ' in name) as space_position,
	name as first_name
FROM person
WHERE NOT (name like '% %');
-- вывод имен где есть имя+фамилия или просто имя
-- реализация с помощью CASE 1 раз обращаемся к таблице

SELECT 
	person_id, name, position (' ' in name) as space_position,
	CASE 
		WHEN name like '% %' THEN substring(name, 1, position (' ' in name)-1) 
		ELSE 					  name
	END as first_name
FROM person;


SELECT *
FROM album
WHERE band_id IN (93, 192);
--25


SELECT band_id, COUNT(*)
FROM album
WHERE band_id IN (93, 192)
GROUP BY 1;
-- 93/11 192/14

--надо:
--93 192 total
--11 14	25
SELECT SUM(b_93), SUM(b_192), SUM(total)
FROM (
	SELECT 
		COUNT(*) as b_93,
		NULL as b_192,
		CAST(NULL AS BIGINT) as total
	FROM album
	WHERE band_id in (93)
	UNION ALL
	SELECT 
		NULL as b_93,
		COUNT(*) as b_192,
		NULL as total
	FROM album
	WHERE band_id in (192)
	UNION ALL
	SELECT 
		NULL as b_93,
		NULL as b_192,
		COUNT(*) as total
	FROM album
	WHERE band_id in (93,192)
) as table_1;

--проще:
SELECT 
	SUM(CASE WHEN band_id=93 then 1 else 0 end) as b_93,
	SUM(CASE WHEN band_id=192 then 1 else 0 end) as b_192,
	COUNT(*) as total
FROM album
WHERE band_id in (93,192);

--разбивка по категориям
SELECT 
	CASE 
		WHEN band_id=93 then '1. band_93'
		WHEN band_id=192 then '2. band_192'
		ELSE '3. all other bands'
	END AS band_categories,
	a.*
FROM album as a;
--группировка
SELECT band_categories, COUNT(*)
FROM (
	SELECT 
		CASE 
			WHEN band_id=93  THEN '1. band_93'
			WHEN band_id=192 THEN '2. band_192'
			ELSE 				  '3. all other bands'
		END AS band_categories,
		a.*
	FROM album as a
)
GROUP BY 1
ORDER BY 1;


--- ПРИМЕР на майтпбл
SELECT 
	a, b, 
	CASE 
		WHEN a = b THEN 'a=b'
		WHEN a > b THEN 'a>b'
		WHEN a < b THEN 'a<b'
		ELSE 'UNKNOWN'
	END as comparison,
	-- наиб
	CASE 
		WHEN a = b THEN a
		WHEN a > b THEN a
		WHEN a < b THEN b
		WHEN a IS NOT NULL AND b IS NULL THEN a
		WHEN a IS  NULL AND b IS NOT NULL THEN b
		ELSE NULL
	END as greater,
	greatest(a,b)
FROM mytable_int