-- 1 шаг
select a.*, ROW_NUMBER() OVER(PARTITION BY a.band_id ORDER BY a.year) as album_num  --ранжирование 1 2 3 3 5
from album as a
where band_id in (93,192)
order by a.band_id, a.year;

-- 2 шаг
select *
from (
	select a.*, ROW_NUMBER() OVER(PARTITION BY a.band_id ORDER BY a.year) as album_num  --ранжирование 1 2 3 3 5
	from album as a
	where band_id in (93,192)
)
where album_num <= 3
order by band_id, year