fruits = [
    "apple", "pear", "banana"
]

def modify_fruit(fruit):
    if 'n' in fruit:
        return fruit + ' pie'
    return fruit




new_list = [modify_fruit(fruit) for fruit in fruits]

print(new_list)