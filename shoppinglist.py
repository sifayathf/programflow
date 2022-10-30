shopping_list = ['bread','pasta','onion','milk','eggs','wheat','rice']

for item in shopping_list:
    print(item)

for item in shopping_list:
    if item == 'wheat':
        continue
    print(item)