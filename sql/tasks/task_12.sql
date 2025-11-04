-- 1 шаг 
CREATE TABLE album_sales (
album_id INTEGER, name VARCHAR, band_id INTEGER, year SMALLINT, total_sales NUMERIC
);
INSERT INTO album_sales
SELECT album_id, name, band_id, year,
100000/((2015-coalesce(year,1900)) * (2015-coalesce(year,1900)))* character_length(name) as total_sales
FROM album WHERE year<2015;
-- 2 шаг
select year, sum(total_sales)
from album_sales
group by year
order by 2 desc
;

-- 3 шаг
select 
	year, sales, 
	sales * 100.00 / sum(sales) over() as percentage
from (
	select year, sum(total_sales) as sales
	from album_sales
	group by year
) as subquery
order by 2 desc
;

