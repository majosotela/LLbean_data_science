SELECT * FROM [dbo].[tblCategory];
SELECT * FROM [dbo].[tblContinent];
SELECT * FROM [dbo].[tblCountry];
SELECT * FROM [dbo].[tblEvent];

SELECT EventName, EventDate
FROM tblEvent
ORDER BY EventDate DESC;

SELECT top 3 CategoryName
from tblCategory
ORDER BY CategoryName DESC; 

