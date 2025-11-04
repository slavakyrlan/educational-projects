/*
Кумулятивные суммы (накопительные суммы, итог)
с каждой строкой добавляется цифра
*/
-- для 1 группы подсчет
SELECT 
	album_id, name, band_id , year, total_sales,
	SUM(total_sales) OVER (	
		ORDER BY year  --чтобы было понятно в каком порядке соортировать  - важна!
		ROWS BETWEEN UNBOUNDED PRECEDING  -- нижняя граница UNBOUNDED PRECEDING все предыдущие строки, а вверхник CURRENT ROW - текущая строка
				 AND CURRENT ROW -- какие строки участвуют в агрегации данных
	) as cumulative_sales
FROM album_sales
WHERE band_id = 1811
;

-- для 2 групп подсчет 
SELECT 
	album_id, name, band_id , year, total_sales,
	SUM(total_sales) OVER (
		PARTITION BY band_id --сумма по соответствию band_id, кумулятивная сумма для каждой группы
		ORDER BY year  --чтобы было понятно в каком порядке соортировать  - важна!
		ROWS BETWEEN UNBOUNDED PRECEDING  -- нижняя граница UNBOUNDED PRECEDING все предыдущие строки, а вверхник CURRENT ROW - текущая строка
				 AND CURRENT ROW -- какие строки участвуют в агрегации данных
	) as cumulative_sales
FROM album_sales
WHERE band_id in (93, 192)
;