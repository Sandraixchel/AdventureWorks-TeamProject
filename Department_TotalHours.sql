SELECT SUM(Employee_1.SickLeaveHours) AS total_hours, HumanResources.vEmployeeDepartment.Department, COUNT(HumanResources.vEmployeeDepartment.Department) AS employees_by_department 
FROM HumanResources.Employee AS Employee_1 
INNER JOIN HumanResources.vEmployeeDepartment ON Employee_1.BusinessEntityID = HumanResources.vEmployeeDepartment.BusinessEntityID
GROUP BY Department
ORDER BY total_hours DESC
;

