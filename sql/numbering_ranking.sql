/* Нумерация и ранжирование */
SELECT 
	a.*,
	ROW_NUMBER() OVER(ORDER BY total_sales DESC, album_id) as rn, -- нумерация 1 2 3 4 5
	RANK()       OVER(ORDER BY total_sales DESC) as rank,  --ранжирование 1 2 3 3 5
	DENSE_RANK() OVER(ORDER BY total_sales DESC) as d_rank  --ранжирование без пропусков нумерации 1 2 3 3 4
FROM album_sales as a
WHERE band_id = 2454
ORDER BY total_sales DESC, album_id
;