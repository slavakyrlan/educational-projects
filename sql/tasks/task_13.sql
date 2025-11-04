-- 1 шаг
CREATE TABLE album_percentages (album_name varchar, sales numeric, percentage numeric);

insert into album_percentages
select 
	album_name, sales, 
	sales*100.00/sum(sales) over() as percentage 
from (
	select 
		a.name as album_name, 
		sum(a.total_sales) as sales 
	from album_sales as a
	where band_id in (93,192,1811) 
	group by 1
) as t;

---
select *
from album_percentages
order by sales desc;

-- 2 шаг
select 
	album_name, sales, percentage,
	SUM(percentage) OVER (
		--PARTITION BY band_id
		ORDER BY sales DESC
		ROWS BETWEEN UNBOUNDED PRECEDING
				 AND CURRENT ROW
	) as cumulative_percentage
from album_percentages
order by sales desc;

-- 3 шаг
select 
	album_name, sales, percentage, cumulative_percentage,
	case when cumulative_percentage between 0 and 80 then 'A'
		 when cumulative_percentage between 80 and 95 then 'B'
		 when cumulative_percentage between 95 and 100 then 'C'
		 else 'unknown' end as category
from (
	select 
		album_name, sales, percentage,
		SUM(percentage) OVER (
			--PARTITION BY band_id
			ORDER BY sales DESC
			ROWS BETWEEN UNBOUNDED PRECEDING
					 AND CURRENT ROW
		) as cumulative_percentage
	from album_percentages
) as subquery
order by sales desc;

/* бд в pgadmin такое не умеет
select 
	album_name, sales, percentage, 
	SUM(percentage) OVER ( ORDER BY sales DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW ) as cumulative_percentage,
	case when cumulative_percentage between 0 and 80 then 'A'
		 when cumulative_percentage between 80 and 95 then 'B'
		 when cumulative_percentage between 95 and 100 then 'C'
		 else 'unknown' 
		 end as category
from album_percentages
order by sales desc;
*/