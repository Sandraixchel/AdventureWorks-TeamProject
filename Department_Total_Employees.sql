SELECT HumanResources.vEmployeeDepartment.Department, COUNT(HumanResources.vEmployeeDepartment.Department) AS total_department
FROM HumanResources.vEmployeeDepartment
GROUP BY Department
ORDER BY total_department;