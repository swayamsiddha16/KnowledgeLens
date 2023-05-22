import json 


f = open('sample_data.json')
  
data = json.load(f)
  
result = []
for param in data['parametersList']:
	# print(param)
	result.append({
		"parameterName": param["parameterName"],
		"max": param["max"],
		"min": param["min"],
		"avg": param["avg"]
		})


for res in result:
    print(res)
