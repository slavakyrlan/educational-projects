/*Скользящие средние, предыдущие строки и последующие строки*/

/*
Варианты ROWS BETWEEN

ORDER BY year                         |
ROWS BETWEEN UNBOUNDED PRECEDING      | Все, что раньше + текущая строка
		 AND CURRENT ROW              |


ORDER BY year                         |
ROWS BETWEEN 3 PRECEDING              | три предыдущие строки + текущая строка
		 AND CURRENT ROW              |

-- хорош для скользящей средней

ORDER BY year                         |
ROWS BETWEEN 3 PRECEDING              | 3 предыдущие строки + 3 следующие строки
		 AND 3 FOLLOWONG              |


ORDER BY year                         |
ROWS BETWEEN CURRENT ROW              | текущая строка + все что дальше
		 AND UNBOUNDED FOLLOWONG      |
100   *
472   *
1770 -> 6371
2006 - *
2595 - *
Это можно наоборот написать, меняем порядок сортировки
ORDER BY year DESC                    |
ROWS BETWEEN UNBOUNDED PRECEDING      | Все предыдущие строки + текущая строка
		 AND CURRENT ROW              |
-- по убыванию


можно и без текущей строки
ORDER BY year                         |
ROWS BETWEEN 2 PRECEDING              | 2 предыдущие строки
		 AND 1 PRECEDING              |

*/
SELECT 
	album_id, name, band_id , year, total_sales,
	AVG(total_sales) OVER (	 -- cначала кумулятивная
		ORDER BY year 
		ROWS BETWEEN 2 PRECEDING  
				 AND 1 PRECEDING
	) as avg2_sales
FROM album_sales
WHERE band_id = 1811
ORDER BY year -- потом по имени сортировка
;

/*
LAG(total_sales,1) OVER (ORDER BY year)
оконная функция, которая позволяет получить значение из предыдущей строки
ORDER BY year 
		ROWS BETWEEN 1 PRECEDING  - НО так выбирается 1 строка нет смысла писать MAX AVG (year)
				 AND 1 PRECEDING

Последующая 
ORDER BY year
ROWS BETWEEN 1 FOLLOWONG
		 AND 1 FOLLOWONG
LEAD(total_sales,1) OVER (ORDER BY year) - вперед

можно поменять порядок LAG и получить LEAD
LAG(total_sales,1) OVER (ORDER BY year DESC)

можно указать partition by если посчитать для отдельных групп
*/

SELECT 
	album_id, name, band_id , year,
	LAG(year,1) OVER (ORDER BY year) as prev_year,
	year - LAG(year,1) OVER (ORDER BY year) as diff_year
FROM album
WHERE band_id = 1811
ORDER BY year
;


