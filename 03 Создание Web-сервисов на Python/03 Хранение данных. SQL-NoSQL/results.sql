use test;
set names utf8;

-- 1. Выбрать все товары (все поля)
SELECT * FROM `test`.`product`;

-- 2. Выбрать названия всех автоматизированных складов
SELECT `store`.`name`
FROM `test`.`store`
WHERE `store`.`is_automated` = 1;

-- 3. Посчитать общую сумму в деньгах всех продаж
SELECT SUM(`sale`.`total`)
FROM `test`.`sale`;

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
SELECT DISTINCT `store`.`store_id`
FROM `test`.`store`
WHERE `store`.`store_id` in (SELECT distinct `sale`.`store_id` FROM `test`.`sale`);


-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
SELECT DISTINCT `store`.`store_id`
FROM `test`.`store`
WHERE `store`.`store_id` not in (SELECT distinct `sale`.`store_id` FROM `test`.`sale`);

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
SELECT `product`.`name`,
    sale.cost
FROM `test`.`product` inner join 
(SELECT `sale`.`product_id`, avg(`sale`.`total`/`sale`.`quantity`) as cost
	FROM `test`.`sale`
	group by `sale`.`product_id`) as sale
ON `product`.`product_id` = sale.`product_id`;

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
select `product`.`name`
from (SELECT distinct
    `sale`.`product_id`,
     `sale`.`store_id`
FROM `test`.`sale`) as sale
left outer join `test`.`product` on sale.product_id = `product`.`product_id`
group by sale.product_id
having count(sale.store_id) = 1;

-- 8. Получить названия всех складов, с которых продавался только один продукт
select store.`name`
from (SELECT distinct
	`sale`.`store_id`,
	`sale`.`product_id`
FROM `test`.`sale`) as sale
left outer join `test`.`store` on sale.store_id = `store`.`store_id`
group by sale.store_id
having count(sale.product_id) = 1;

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
SELECT *
FROM `test`.`sale`
where `sale`.`total` = 
 (SELECT max(`sale`.`total`)
FROM `test`.`sale`);

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
SELECT `sale`.`date`
FROM `test`.`sale`
group by `sale`.`date`
having sum(`sale`.`quantity`) = (select max(s.sold) from (
SELECT `sale`.`date`,
    sum(`sale`.`quantity`) as sold
FROM `test`.`sale`
group by `sale`.`date`) as s);

