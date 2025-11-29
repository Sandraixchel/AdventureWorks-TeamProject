SELECT Employee_1.BusinessEntityID, Employee_1.JobTitle, Employee_1.VacationHours, HumanResources.EmployeePayHistory.Rate, Sales.SalesPerson.Bonus
FROM HumanResources.Employee AS Employee_1 
INNER JOIN HumanResources.EmployeePayHistory ON Employee_1.BusinessEntityID = HumanResources.EmployeePayHistory.BusinessEntityID 
INNER JOIN Sales.SalesPerson ON Employee_1.BusinessEntityID = Sales.SalesPerson.BusinessEntityID
;