-- 1 шаг
create table weather (the_date date, weather_type varchar);
insert into weather values(date'2023-01-01', 'Солнечно');
insert into weather values(date'2023-01-02', 'Снег');
insert into weather values(date'2023-01-03', 'Солнечно');
insert into weather values(date'2023-01-04', 'Солнечно');
insert into weather values(date'2023-01-05', 'Солнечно');
insert into weather values(date'2023-01-06', 'Облачно');
insert into weather values(date'2023-01-07', 'Солнечно');
insert into weather values(date'2023-01-08', 'Солнечно');
insert into weather values(date'2023-01-09', 'Снег');
insert into weather values(date'2023-01-10', 'Снег');
insert into weather values(date'2023-01-11', 'Снег');
insert into weather values(date'2023-01-12', 'Снег');

-- 2, 3 шаг
select the_date, weather_type,
	LAG(weather_type, 1) OVER(ORDER BY the_date) as previous_weather_type,
	CASE 
		WHEN weather_type <> LAG(weather_type, 1) OVER(ORDER BY the_date)
		THEN 1
		ELSE 0
	END as difference
from weather
order by the_date;

-- 4 шаг
select 
	the_date, weather_type, previous_weather_type, difference,
	sum(difference) OVER (ORDER BY the_date
						  ROWS BETWEEN UNBOUNDED PRECEDING 
						  AND CURRENT ROW)
from (
	select the_date, weather_type,
		LAG(weather_type, 1) OVER(ORDER BY the_date) as previous_weather_type,
		CASE 
			WHEN weather_type <> LAG(weather_type, 1) OVER(ORDER BY the_date)
			THEN 1
			ELSE 0
		END as difference
	from weather
)
order by the_date;

-- 5 шаг
select 
	cumulative,
	weather_type,
	count(*) as number_of_days
from(
	select 
		the_date, weather_type, previous_weather_type, difference,
		sum(difference) OVER (ORDER BY the_date
							  ROWS BETWEEN UNBOUNDED PRECEDING 
							  AND CURRENT ROW) as cumulative
	from (
		select the_date, weather_type,
			LAG(weather_type, 1) OVER(ORDER BY the_date) as previous_weather_type,
			CASE 
				WHEN weather_type <> LAG(weather_type, 1) OVER(ORDER BY the_date)
				THEN 1
				ELSE 0
			END as difference
		from weather
	)
) as t3
group by 1,2
order by 1;

-- 6 шаг максимальное количество подряд идущих солнечных дней
select max(number_of_days)
from(
	select 
		cumulative,
		weather_type,
		count(*) as number_of_days
	from(
		select 
			the_date, weather_type, previous_weather_type, difference,
			sum(difference) OVER (ORDER BY the_date
								  ROWS BETWEEN UNBOUNDED PRECEDING 
								  AND CURRENT ROW) as cumulative
		from (
			select the_date, weather_type,
				LAG(weather_type, 1) OVER(ORDER BY the_date) as previous_weather_type,
				CASE 
					WHEN weather_type <> LAG(weather_type, 1) OVER(ORDER BY the_date)
					THEN 1
					ELSE 0
				END as difference
			from weather
		)
	) as t3
	where weather_type = 'Солнечно'
	group by 1,2
) as t4
order by 1;