An application requires different date formats to be converted into one common date format.

### Implement the function transform_date_format, which:
 - Accepts a list of dates as strings.
 - Returns a new list of strings that represents dates in the format YYYYDDMM, where:
    - YYYY represents the year.
    - DD represents the day.
    - MM represents the month.
 - Only dates in one of the following formats should be included in the returned list:
    - Y YYYp DDp MM
    - YYYY/MM/DD
    - MM-DD-YYYY

### Examples:
```py
transform_date_format(["2010/02/20", "2 016p 19p 12", "11-18-2012", "2018 12 24", "20130720"])
```
### Should return:
```py
["20102002", "20161912", "20121811"]
```
