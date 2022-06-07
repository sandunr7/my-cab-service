from tkinter import *

details = [
    {
        'name': 'Rikaz',
        'age': 25,
        'gender': 'male'
    },
    {
        'name': 'Fathima',
        'age': 20,
        'gender': 'female'
    },
    {
        'name': 'Aska',
        'age': 20,
        'gender': 'female'
    },
    {
        'name': 'Nuwan',
        'age': 25,
        'gender': 'male'
    }
]

temDetails = []

persons = [
    [
        'Rikaz',
        25
    ],
    [
        'Himan',
        20
    ],
    [
        'Lahiru',
        22
    ]
]

# Add, Remove, Assign, Release, View
# View

# for detail in details:
#     print("Name: ", detail['name'], "  Age: ", detail['age'])
#
# for person in persons:
#     print("Name: ", person[0], "  Age: ", person[1])
#
# root = Tk()
# root.geometry("600x400")
# row = 1
# for person in persons:
#     # Label(root, text=person[0]).grid(row=row, column=1)
#     # Label(root, text=person[1]).grid(row=row, column=2)
#     # row += 1
#     print("Name: ", person[0], "  Age: ", person[1])
#
# root.mainloop()

# Add
# name = input("Enter the name: ")
# age = int(input("Enter the age: "))
#
# # newDic = {
# #         'name': name,
# #         'age': age
# #     }
# # details.append(newDic)
# # print(details)
#
# newList = [
#     name,
#     age
# ]
# persons.append(newList)
# print(persons)

# Remove

# for detail in details:
#     print("ID", details.index(detail), "Name: ", detail['name'], "  Age: ", detail['age'])
#
# # for person in persons:
# #     print("ID", persons.index(person) , "Name: ", person[0], "  Age: ", person[1])
#
# remId = int(input("Select the ID: "))
# details.pop(remId)
# for detail in details:
#     print("ID", details.index(detail), "Name: ", detail['name'], "  Age: ", detail['age'])

# Assign
# for detail in details:
#     print("ID", details.index(detail), "Name: ", detail['name'], "  Age: ", detail['age'], " Gender: ", detail['gender'])
#
#
#
# userSelection = input("Assign 1 for male\nAssign 2 for female\n")
# if userSelection == '1':
#     for detail in details:
#         if detail['gender'] == 'male':
#             dic = detail
#             id = details.index(detail)
#             break
# elif userSelection == '2':
#     for detail in details:
#         if detail['gender'] == 'female':
#             dic = detail
#             id = details.index(detail)
#             break
# temDetails.append(dic)
# details.pop(id)
#
# print("After Assign")
# for detail in details:
#     print("ID", details.index(detail), "Name: ", detail['name'], "  Age: ", detail['age'], " Gender: ", detail['gender'])
#
# print("temDetails")
# for detail in temDetails:
#     print("ID", temDetails.index(detail), "Name: ", detail['name'], "  Age: ", detail['age'], " Gender: ", detail['gender'])
#
# userSelection = int(input("Enter the id: "))
# relId = userSelection
# obj = temDetails[relId]
# print(details)
# print(temDetails)
# details.append(obj)
# temDetails.pop(relId)
#
# print("After Assign")
# for detail in details:
#     print("ID", details.index(detail), "Name: ", detail['name'], "  Age: ", detail['age'], " Gender: ", detail['gender'])
#
# print("temDetails")
# for detail in temDetails:
#     print("ID", temDetails.index(detail), "Name: ", detail['name'], "  Age: ", detail['age'], " Gender: ", detail['gender'])



while True:
    mainOption = input("1 for Add\n2 for remove\n3 for Assign\n4 for Release\n5 for View\n6 for Exit\n")
    if mainOption == '6':
        break
    elif mainOption == '1':
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        gender = input('Enter the gender: ')

        newDic = {
                'name': name,
                'age': age,
                'gender': gender
            }
        details.append(newDic)
    elif mainOption == '2':
        for detail in details:
            print("ID", details.index(detail), "Name: ", detail['name'], "  Age: ", detail['age'])
        remId = int(input("Select the ID: "))
        details.pop(remId)
    elif mainOption == '3':
        for detail in details:
            print("ID", details.index(detail), "Name: ", detail['name'], "  Age: ", detail['age'], " Gender: ", detail['gender'])
        userSelection = input("Assign 1 for male\nAssign 2 for female\n")
        if userSelection == '1':
            for detail in details:
                if detail['gender'] == 'male':
                    dic = detail
                    id = details.index(detail)
                    break
        elif userSelection == '2':
            for detail in details:
                if detail['gender'] == 'female':
                    dic = detail
                    id = details.index(detail)
                    break
        temDetails.append(dic)
        details.pop(id)
    elif mainOption == '4':
        for detail in temDetails:
            print("ID", temDetails.index(detail), "Name: ", detail['name'], "  Age: ", detail['age'], " Gender: ", detail['gender'])

        userSelection = int(input("Enter the id: "))
        relId = userSelection
        obj = temDetails[relId]
        details.append(obj)
        temDetails.pop(relId)
    elif mainOption == '5':
        print("Available Persons")
        for detail in details:
            print("ID", details.index(detail), "Name: ", detail['name'], "  Age: ", detail['age'], " Gender: ", detail['gender'])
        print("Assigned Persons")
        for detail in temDetails:
            print("ID", temDetails.index(detail), "Name: ", detail['name'], "  Age: ", detail['age'], " Gender: ",
                  detail['gender'])