### Solution
```
def majorityElement(nums):
    
    count_dict = dict()
    
    # Count appearances in a dictionary
    for i in nums:

        count_dict[i] = count_dict.get(i,0) + 1
        
    # Grab the key that belongs to the max value
    for key, value in count_dict.items():

        if value == max(count_dict.values()):
            return key
```
### Output
```
3
```
