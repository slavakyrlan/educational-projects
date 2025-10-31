-- 1 шаг
SELECT *
FROM band
WHERE name LIKE '%magic%'
ORDER BY name;

-- 2 шаг
SELECT *
FROM band
WHERE lower(name) LIKE '%magic%'
ORDER BY name;

-- 3 шаг
SELECT COUNT(*)
FROM (
	SELECT name, substring(name,1,1) as first_letter
	FROM person
	WHERE substring(name,1,1) between 'A' and 'Z'
	-- БОЛЕЕ строгое условие position(substring(name,1,1) in 'ABCDEFGHIJKLMNOPQSTUVWXYZ')>0
);

--4 шаг
SELECT substring(name,1,1) as first_letter, COUNT(*)
FROM person
WHERE substring(name,1,1) between 'A' and 'Z'
GROUP BY 1
ORDER BY 2 DESC;


--5 шаг
SELECT 
	--name, 
	--substring(name,1,1) as first_letter,
	--position(' ' in name),
	substring(name, 1, position(' ' in name)),
	COUNT(*)
FROM person
WHERE 
	substring(name,1,1) between 'A' and 'Z'
	AND name LIKE '% %'
GROUP BY 1
ORDER BY 2 DESC;
