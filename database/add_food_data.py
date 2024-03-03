import sqlite3

connection = sqlite3.connect("database/Food.db")
cursor = connection.cursor()

food = {
    44 : "fried_rice",
    72 : "pancakes",
    53 : "hamburger",
    76 : "pizza",
    55 : "hot_dog"
}

for cls, name in food.items():
    cursor.execute("INSERT INTO food (food_id, food_name) VALUES (?, ?)", (cls, name))

connection.commit()
connection.close()
