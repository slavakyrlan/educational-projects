/* 
Для числовых типов:
- ABS(-10) - вернет положительное = 10
- ROUND(2.8) - округлит до целого = 3
- TRUNC(-2.3) - отбрасывает др часть = -2
- - TRUNC(2.8311, 2) - вернет 2.83, 2 числа после запятой
- FLOOR(2.8)(-2.8) - пол/потолок 2/-3 вернет число меньше указанного
- CEILING(2.8)(-2.8) - аналогичная функция возвраащает больше указанного 3/-2

cast(n_albums as numeric) - сконвертируем в нумерик
NULLIF(n_bands, 0) - если в поле n_bands будет 0 заменит его на null, чтоб не было деления на 0 
- рекомендуется писать в знаменателе 
DISTINCT - уникальные отличны от NULL
*/
SELECT 
	n_albums, --121918
	n_bands, --36882
	n_albums/n_bands, --3
	cast(n_albums as numeric) / NULLIF(n_bands, 0), --3.30562333
	ROUND(cast(n_albums as numeric) / n_bands, 3), --3.306
	ROUND(cast(n_albums as numeric) / n_bands),  --3
	FLOOR(cast(n_albums as numeric) / n_bands), --3
	CEILING(cast(n_albums as numeric) / n_bands) --4
FROM (
	SELECT 
		COUNT(*) AS n_albums,
		COUNT(DISTINCT band_id) AS n_bands
	FROM album
);

/* 
Для символьных типов:
LIKE - текст похожий на шаблон
- % любое количество символов
- _ один символ
SUBSTRING('DD', 11, 4) - поиск строки в подстроке
- с 11 символа берем 4 символа, если не найдет вернет ''
POSITION('dad' in 'DASDA dad') 
- вернет позицию в строке, капс влияет, если не найдет вернет 0
Character_lenght('asdasd') - кол-во символов в строке с ' '
TRIM(' BOOK ') - отбрасывает пробелы вернет BOOK
- TRIM('x' from 'xxBOOKxx') - вернет BOOK, уберет что указано в первом для отбрасывания
- TRIM(leading 'x' from 'xxBOOKxx') - отбросить символы слева
- TRIM(trailing 'x' from 'xxBOOKxx') - отбросить символы справа
LOWER ниж регистр
UPPER верх регистр
*/
SELECT *
FROM album
WHERE 
	name LIKE '% of %'; -- до и после of несколько символов

SELECT *
FROM album
WHERE 
	name LIKE '%F%%' ESCAPE 'F';  -- F исключаем чтоб найти %

SELECT 
	name,
	position(' ' in name),
	substring(name, 1, position(' ' in name) - 1) as firstname,
	substring(name, position(' ' in name) + 1) as lastname
FROM 
	person
WHERE 
	position(' ' in name) > 0
	AND name = 'Bob Ashley';

/* 
Для типов даты и времени:
to_date('2018-12-31','yyyy-mm-dd') = 2018-12-31 перевод строки в дату с указаением где месяц год и тд
to_timestamp('2018-12-31 23:40:42', 'yyyy-mm-dd hh24:mi:ss')

to_char(date '2012-11-23', 'yyyy-mm-dd') - наоборот из даты вернет str - 2018-12-31
to_char(date '2012-11-23', 'dd-mm-yyyy') - наоборот из даты вернет str в том формате котором хочу ответ 31-12-2018

current_date = текущая дата 2018-01-01
сurrent_time = 23:55:55.1232+00:00
current_timestamp 2018-01-01 23:55:33.12123+00:00

extract - извелечение отдельных сооставляющих 
extract(year from date '2018-12-31') = 2018
extract(month from date '2018-12-31') = 12
extract(day from date '2018-12-31') = 31
*/


