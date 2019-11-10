SELECT COUNT(*) FROM rooms
(SELECT 
	room_name
FROM
	hotels NATURAL JOIN rooms )
;

SELECT SalesOrderID,
       OrderDate,
       TotalDue,
       (SELECT COUNT(SalesOrderDetailID)
          FROM Sales.SalesOrderDetail
         WHERE SalesOrderID = SO.SalesOrderID) as LineCount
FROM   Sales.SalesOrderHeader SO

--SELECT COUNT(ip_address) FROM `ports` (
--    SELECT DISTINCT ip_address FROM `ports` WHERE status IS TRUE
--)
