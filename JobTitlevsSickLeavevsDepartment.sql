SELECT Employee_1.JobTitle, COUNT(Employee_1.JobTitle) AS total_employee, SUM(Employee_1.SickLeaveHours) AS total_sick_hours, HumanResources.vEmployeeDepartment.Department 
FROM HumanResources.Employee AS Employee_1 
INNER JOIN HumanResources.vEmployeeDepartment ON Employee_1.BusinessEntityID = HumanResources.vEmployeeDepartment.BusinessEntityID
GROUP BY Employee_1.JobTitle, Department
ORDER BY total_employee DESC
;

