SELECT 
    e.JobTitle,
    COUNT(e.JobTitle) AS total_employee,
    SUM(e.SickLeaveHours) AS total_sick_hours,
    v.Department,
    p.PersonType
FROM HumanResources.Employee AS e
INNER JOIN HumanResources.vEmployeeDepartment AS v
    ON e.BusinessEntityID = v.BusinessEntityID
INNER JOIN Person.Person AS p
    ON e.BusinessEntityID = p.BusinessEntityID
WHERE p.PersonType IN ('EM', 'SP')
GROUP BY e.JobTitle, v.Department, p.PersonType
ORDER BY total_employee DESC;
