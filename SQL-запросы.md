# Екатерина Сомова, 16-я когорта - Финальный проект. Инженер по тестированию плюс
___
## Задание 1:

- Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных. 
- Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» 
(поле inDelivery = true).

```
SELECT "Couriers".login,
        COUNT ("Orders".track)
FROM "Couriers"
INNER JOIN "Orders" ON "Couriers".id = "Orders"."courierId"
WHERE "Orders"."inDelivery" = true
GROUP BY login;
```
___
## Задание 2:

Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.

Для этого: выведи все трекеры заказов и их статусы. 

Статусы определяются по следующему правилу:

- Если поле `finished == true`, то вывести статус `2`.
- Если поле `canсelled == true`, то вывести статус `-1`.
- Если поле `inDelivery == true`, то вывести статус `1`.
- Для остальных случаев вывести `0`.

```
SELECT track,
  CASE
   WHEN "Orders"."finished" = true THEN '2'
   WHEN "Orders"."cancelled" = true THEN '-1'
   WHEN "Orders"."inDelivery" = true THEN '1'
   ELSE '0'
  END
FROM "Orders";
```