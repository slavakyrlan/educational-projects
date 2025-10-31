SELECT *
FROM album
WHERE band_id = 388
ORDER BY year;

SELECT year, COUNT(*)
FROM album
WHERE band_id = 388
GROUP BY year;

SELECT *
FROM calendar_year 
WHERE year>1968 AND year < 1983;

SELECT *
FROM calendar_year 
WHERE year BETWEEN 1969 AND 1982;

SELECT c.year, COUNT(a.album_id)
FROM calendar_year as c
LEFT JOIN album as a
	ON c.year = a.year 
	AND a.band_id = 388
WHERE c.year BETWEEN 1969 AND 1982
GROUP BY c.year