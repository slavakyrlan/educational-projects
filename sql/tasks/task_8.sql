-- 1 шаг
SELECT band_id
FROM album
WHERE name = 'Now';


-- 2 шаг
SELECT band_id
FROM album
WHERE name = 'The Collection';

-- 3 шаг
SELECT band_id FROM album WHERE name = 'Now'
INTERSECT
SELECT band_id FROM album WHERE name = 'The Collection';


-- 4 шаг
SELECT *
FROM band
WHERE band_id IN (
	SELECT band_id FROM album WHERE name = 'Now'
	INTERSECT
	SELECT band_id FROM album WHERE name = 'The Collection'
);