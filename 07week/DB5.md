### 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.

```sql
SELECT * FROM playlist_track A ORDER BY A.PlaylistId DESC LIMIT 5;
```

### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요
| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT * FROM tracks B ORDER BY B.TrackId ASC LIMIT 5;
```

### 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.
| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 

```sql
SELECT A.PlaylistId, B.Name FROM playlist_track A
INNER JOIN tracks B
ON A.TrackId = B.TrackId
ORDER BY A.PlaylistId DESC
LIMIT 10;
```

### 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 
| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.

```sql
SELECT A.PlaylistId, B.Name FROM playlist_track A
INNER JOIN tracks B
ON A.TrackId = B.TrackId
WHERE A.PlaylistId = 10
ORDER BY B.Name DESC
LIMIT 5;
```

### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.

```sql
SELECT count(*) FROM tracks A
INNER JOIN artists B
ON A.Composer = B.Name;
```

### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.

```sql
SELECT count(*) FROM tracks A
LEFT JOIN artists B
ON A.Composer = B.Name;
```

### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.
```plain
INNER JOIN 은 겹치는 것만 LEFT JOIN은 값이 없는 것도 JOIN(OUTER JOIN)
```

### 8. invoice_items 테이블의 데이터를 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
SELECT InvoiceLineId,InvoiceId FROM invoice_items
ORDER BY InvoiceId ASC LIMIT 5;
```

### 9. invoices 테이블의 데이터를 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
SELECT InvoiceId, CustomerId FROM invoices
ORDER BY InvoiceId ASC LIMIT 5;
```

### 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.

```
SELECT A.InvoiceLineId, B.InvoiceId FROM invoice_items A
JOIN invoices B
ON A.InvoiceId = B.InvoiceId
ORDER BY B.InvoiceId DESC LIMIT 5;
```


### 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.

```
SELECT A.CustomerId, B.InvoiceId FROM customers A
JOIN invoices B
ON A.CustomerId = B.CustomerId
ORDER BY B.InvoiceId DESC LIMIT 5;
```

### 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.

```
SELECT A.InvoiceLineId, B.InvoiceId, C.CustomerId FROM invoice_items A
JOIN invoices B
ON A.InvoiceId = B.InvoiceId
JOIN customers C
ON B.CustomerId = C.CustomerId
ORDER BY A.InvoiceId DESC LIMIT 5;
```

### 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.
| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
SELECT D.CustomerId, count(*) FROM invoice_items A
JOIN (SELECT * from invoices B
JOIN customers C
ON B.CustomerId = C.CustomerId) D
ON A.InvoiceId = D.InvoiceId
GROUP BY D.CustomerId ORDER BY D.CustomerId ASC LIMIT 5;
```
