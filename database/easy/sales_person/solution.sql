SELECT name
FROM SalesPerson
WHERE name NOT IN (
    SELECT SalesPerson.name
    FROM Orders
    LEFT JOIN Company ON Company.com_id = Orders.com_id
    LEFT JOIN SalesPerson ON SalesPerson.sales_id = Orders.sales_id
    WHERE Company.name = 'RED'
)