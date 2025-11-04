/* CTE common table expression
*/
--вложенный подзапрос 
SELECT 
	SUM(album_count),
	COUNT(*)
FROM (
	SELECT 
		band_id,
		COUNT(*) as album_count
	FROM album
	GROUP BY 1
);
-- SUM 121918 количество альбомов, COUNT 36882 количество муз групп
--промежуточная таблица с удалением после использования
CREATE TABLE table_1 as 
	SELECT band_id, 
		count(*) as album_count
	FROM album as a
	GROUP BY 1;
SELECT SUM(album_count), count(*)
from table_1;
DROP TABLE table_1;

--CTE
WITH table_1 as (
SELECT 
	band_id,
	COUNT(*) as album_count
FROM album
GROUP BY 1
)
SELECT 
	SUM(album_count),
	COUNT(*)
FROM table_1;

-- Несколько CTE
WITH table_1 as ( -- 1 запрос СТЕ
		SELECT 
			band_id,
			COUNT(*) as album_count
		FROM album
		GROUP BY 1
),
	 table_2 as ( -- 2 запрос СТЕ
		SELECT 
			SUM(album_count) as a_c,
			COUNT(*) as counter
		FROM table_1
)
SELECT * -- основной запрос
FROM table_2;


---------------------------
--Рекурсивные запросы
---------------------------
--music_instrument
--task_7.sql
WITH RECURSIVE recursive_table as (
SELECT  --начало рекурсии
	l_1.parent_id, 
	cast(NULL AS CHARACTER VARYING) as parent_name,
	coalesce(l_1.name,'') as chained_name,
	l_1.id, l_1.name,
	1 as depth
FROM music_instrument as l_1
WHERE l_1.id = 1

UNION ALL

SELECT --шаг рекурсии
	recursive_alias.id as parent_id, recursive_alias.name as parent_name,
	recursive_alias.chained_name || ' -> ' || coalesce(l_next.name, '') as chained_name,
	l_next.id, l_next.name,
	recursive_alias.depth + 1 as depth
FROM recursive_table as recursive_alias
LEFT JOIN music_instrument as l_next
	ON l_next.parent_id = recursive_alias.id
WHERE depth <= 10 --выйти из рекурсии
	AND l_next.id IS NOT NULL
) SELECT * FROM recursive_table
ORDER BY depth, parent_name, name



