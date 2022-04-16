import json

import demjson3
data0 = [{'a': 1, 'v': 2, 'c': 3, 'd': 4}]
json_ob = demjson3.encode(data0)
print(json_ob)

print('********demjson3************')

json_ob1 = '[{"a": 1, "c": 3, "d": 4, "v": 2}]'
py_data = demjson3.decode(json_ob1)
print(py_data)
print('********demjson3************')


# data = [{'a': 1, 'v': 2, 'c': 3, 'd': 4}]
data = {'a': 1, 'v': 2, 'c': 3, 'd': 4}
print('data type:', type(data))
print('data:', data)
print('*************************')
json_obj = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
print('json_obj type:', type(json_obj))
print('json_obj:', json_obj)
print('*************************')
json.dump(data, open('json.txt', 'w'), sort_keys=True, indent=4, separators=(',', ': '))

print('--------------------------')

json_obj = '{"a": 1, "v": 2, "c": 3, "d": 4}'
data = json.loads(json_obj)
print('loads data:', data)
print('*************************')
data2 = json.load(open('json.txt', 'r'))
print('loads data2:', data2)

