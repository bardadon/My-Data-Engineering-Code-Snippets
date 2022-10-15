### Load the Data
```
db.employee.insertMany([{'id':1, 'salary':100}, {'id':2, 'salary':200}, {'id':3, 'salary':300}])
```
### Solution
```
db.employee.aggregate([{
  "$sort": {
    "salary": -1
  }
},{
  "$limit": 2
},{
  "$project": {
    "_id": 0,
    "salary": 1
  }
},{
  "$group": {
    "_id": {},
    "Nth_Highest_Salary": {
      "$min": "$salary"
    }
  }
},{
  "$project": {
    "Nth_Highest_Salary": 1,
    "_id": 0
  }
}])
```
### Output
```
{ "Nth_Highest_Salary" : 200 }
```
