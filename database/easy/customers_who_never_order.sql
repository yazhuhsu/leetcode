/*
    suppose that a website contains two tables,

    Table 1. Customers
    +----+-------+
    | Id | Name  |
    +----+-------+
    | 1  | Joe   |
    | 2  | Henry |
    | 3  | Sam   |
    | 4  | Max   |
    +----+-------+

    Table 2. Orders
    +----+------------+
    | Id | CustomerId |
    +----+------------+
    | 1  | 3          |
    | 2  | 1          |
    +----+------------+

    using the above tables as example,
    return the following:
    +-----------+
    | Customers |
    +-----------+
    | Henry     |
    | Max       |
    +-----------+
*/

SELECT `Customers`.`Name` AS `Customers`
FROM `Customers`
LEFT OUTER JOIN `Orders`
ON `Customers`.`Id` = `Orders`.`CustomerId`
WHERE `Orders`.`Id` IS NULL