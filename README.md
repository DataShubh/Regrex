# Regrex
Dictionaries and Exception Handling
Regex to extract all the numbers with orange color background from the below text in italics.
{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}

----------------x---------- sample guidance-----------------------------x--------------- 
d = {"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}

d.keys()    
>>dict_keys(['orders', 'errors'])


d["orders"] 
>>""" [{'id': 1},
 {'id': 2},
 {'id': 3},
 {'id': 4},
 {'id': 5},
 {'id': 6},
 {'id': 7},
 {'id': 8},
 {'id': 9},
 {'id': 10},
 {'id': 11},
 {'id': 648},
 {'id': 649},
 {'id': 650},
 {'id': 651},
 {'id': 652},
 {'id': 653}]"""



d["errors"]
>>""" [{'code': 3,
  'message': '[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)'}]"""



d.values() 
>>""" dict_values([[{'id': 1}, {'id': 2}, {'id': 3}, 
{'id': 4}, {'id': 5}, {'id': 6}, {'id': 7}, {'id': 8}, {'id': 9}, 
{'id': 10}, {'id': 11}, {'id': 648}, {'id': 649}, {'id': 650}, {'id': 651}, {'id': 652}, 
{'id': 653}], [{'code': 3, 'message': '[PHP Warning #2]
count(): Parameter must be an array or an object that implements Countable (153)'}]])"""



d["orders"][1] 
>>{'id': 2}


d["orders"].key() 
>>error 'list' object has no attribute 'key'


list(d.keys()) 
>>['orders', 'errors']



d[k][i].values 
>>>dict_values([1])
dict_values([2])
dict_values([3])
dict_values([4])
dict_values([5])
dict_values([6])
dict_values([7])
dict_values([8])
dict_values([9])
dict_values([10])
dict_values([11])
dict_values([648])
dict_values([649])
dict_values([650])
dict_values([651])
dict_values([652])
dict_values([653])
dict_values([3, '[PHP Warning #2] 
count(): Parameter must be an array or an object that implements Countable (153)'])"""

>>>d[k][i].keys() here K = (orders and errors), i = length of order or length of errors
dict_keys(['id'])
dict_keys(['id'])
dict_keys(['id'])
dict_keys(['id'])
dict_keys(['id'])
dict_keys(['id'])
dict_keys(['id'])
dict_keys(['id'])
dict_keys(['id'])
dict_keys(['id'])
dict_keys(['id'])
dict_keys(['id'])
dict_keys(['id'])
dict_keys(['id'])
dict_keys(['id'])
dict_keys(['id'])
dict_keys(['id'])
dict_keys(['code', 'message'])"""
