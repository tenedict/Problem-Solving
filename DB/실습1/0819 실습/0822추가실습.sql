---1
SELECT *
FROM playlist_track A
ORDER BY PlaylistId DESC
LIMIT 5;

---2
SELECT *
FROM Tracks B
ORDER BY TrackId ASC
LIMIT 5;

--3
SELECT *
FROM playlist_track A 
JOIN Tracks B
ON A.TrackId = B.TrackId
ORDER BY A.PlaylistId DESC
LIMIT 5;

--4
SELECT *
FROM tracks t
JOIN PLAYLIST_track p
on t.trackid = p.trackid
where P.playlistId = 10
ORDER BY t.NAME DESC
limit 5

--5
SELECT count(*)
FROM tracks t 
JOIN artists a
ON a.name = t.Composer

--6
SELECT count(*)
FROM tracks t 
LEFT JOIN artists a
ON a.name = t.Composer

--8
SELECT InvoiceLineId, InvoiceId
FROM invoice_items
ORDER BY InvoiceId
limit 5;

--9
SELECT InvoiceId, CustomerId
FROM invoices
ORDER BY InvoiceId
limit 5;

--10
SELECT  IT.InvoiceLineId, IT.InvoiceId
FROM invoice_itemS It
join invoiceS i
on i.InvoiceId = It.InvoiceId
ORDER BY I.InvoiceId DESC
LIMIT 5 ;

--11
SELECT  I.InvoiceId, C.CustomerId
FROM InvoiceS I
join CUSTOMERS C
on i.CustomerId = C.CustomerId
ORDER BY I.InvoiceId DESC
LIMIT 5 ;

--12
SELECT  I.InvoiceLineId, INV.InvoiceId, INV.CustomerId
FROM invoice_itemS I
JOIN invoiceS INV
ON i.InvoiceId = INV.InvoiceId
ORDER BY I.InvoiceId DESC
LIMIT 5 ;

--13
SELECT C.CustomerId, count(*) FROM invoice_items A
INNER JOIN (
    SELECT * FROM invoices A
    INNER JOIN customers B
    ON A.CustomerId = B.CustomerId
) C
ON A.InvoiceId = C.InvoiceId
GROUP BY C.CustomerId
ORDER BY C.CustomerId ASC
LIMIT 5;

--13.1
SELECT Z.CUSTOMERID, count(*) FROM INVOICE_ITEMS w
JOIN(
    SELECT * FROM invoices A
    INNER JOIN customers B
    ON A.CustomerId = B.CustomerId
)  Z
ON W.InvoiceId = Z.InvoiceId
GROUP BY Z.CustomerId
ORDER BY Z.CustomerId ASC
LIMIT 5;


--14
SELECT t.name, g.name
FROM tracks t
JOIN genres g
ON t.GenreId = g.GenreId

--15
SELECT c.lastname, e.firstname'근로자이름', c.firstname'손님이름'
FROM employees e	NULL	162 E Superior Street	Chicago	IL	USA	60611
JOIN customers c
ON e.LastName = c.LastName

--16
SELECT Company
FROM customers
where company is not null