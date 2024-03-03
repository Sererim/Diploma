import sqlite3

connection = sqlite3.connect("database/Food.db")
cursor = connection.cursor()

_MK: float = 0.000001
_MG: float = 0.001

pancake = {
    'food_id'    :  72,
    'carbohydrates' : 28.3,
    'fats'          : 9.7,
    'proteins'      : 6.4
}

hot_dogs = {
    'food_id'    :  55,
    'carbohydrates' : 2.89,
    'fats'          : 28,
    'proteins'      : 11.7
}

hamburgers = {
    'food_id'    :  53,
    'carbohydrates' : 29.6,
    'fats'          : 10.2,
    'proteins'      : 13.3
}

fried_rice = {
    'food_id'    :  44,
    'carbohydrates' : 27.6,
    'fats'          : 3.66,
    'proteins'      : 7.28
}

pizza = {
    'food_id'    :  76,
    'carbohydrates' : 5.65,
    'fats'          : 24.5,
    'proteins'      : 19.2
}

foods = [pancake, hot_dogs, hamburgers, fried_rice, pizza]

for item in foods:
    cursor.execute("INSERT INTO food_nutrients \
        (food_id, carbohydrates, fats, proteins) VALUES (?, ?, ?, ?)", 
        (item['food_id'], item['carbohydrates'], item['fats'], item['proteins']))

connection.commit()
connection.close()
