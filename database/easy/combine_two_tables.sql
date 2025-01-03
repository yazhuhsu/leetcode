SELECT `FirstName`, `Lastname`, `City`, `State`
FROM `Person`
LEFT JOIN `Address` ON `Person`.`PersonID` = `Address`.`PersonID`