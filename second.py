import json



f = open('detail.json', 'r')
obj = json.load(f)
details = obj['details']
temDetails = obj['temdetails']
for detail in details:
    print(detail['name'])
name = input("Enter the name: ")
age = int(input("Enter the age: "))
gender = input('Enter the gender: ')

newDic = {
        'name': name,
        'age': age,
        'gender': gender
    }
details.append(newDic)
f.close()

f = open('detail.json', 'w')
json.dump(obj, f)
f.close()

f = open('detail.json', 'r')
obj = json.load(f)
details = obj['details']

for detail in details:
    print(detail['name'])
f.close()