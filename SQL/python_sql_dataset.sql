select * from dataset_1;
select * from dataset_1 limit 10;
select Distinct passanger from dataset_1;
select * from dataset_1 where destination = 'Home';
select * from dataset_1 order by coupon;
select destination as 'destination' from dataset_1;
select occupation from dataset_1 group by occupation;
select weather ,avg (temperature) as 'avg_temp' from dataset_1 group by weather;
select weather, count(temperature) as 'count_temp' from dataset_1 group by weather;
select weather, count(distinct temperature) as 'count_distinct_temp' from dataset_1 group by weather;
select weather, sum (temperature) as 'sum_temp'from dataset_1 group by weather;
select weather, min (temperature) as 'min_temp'from dataset_1 group by weather;
select weather, max (temperature) as 'max_temp'from dataset_1 group by weather;
select occupation from dataset_1 group by occupation having occupation = 'Student';
SELECT DISTINCT destination FROM(SELECT * FROM dataset_1 UNION SELECT * FROM table_to_union);
select * from dataset_1 where weather like 'Sun%';
select DISTINCT temperature FROM dataset_1 WHERE temperature BETWEEN 29 AND 75 ;
select occupation FROM dataset_1 WHERE occupation IN('Sales & Related','Management');


