import sqlite3

connection = sqlite3.connect("database/Food.db")

cursor = connection.cursor()

cursor.execute("""CREATE TABLE food (
    food_id INT PRIMARY KEY, 
    food_name TEXT)
    """
)

cursor.execute("""CREATE TABLE food_vitamins (
    food_id INT,
	vitamin_d REAL,
	vitamin_c REAL,
	vitamin_e REAL,
	vitamin_a REAL,
	vitamin_b6 REAL,
	vitamin_l REAL,
	magnesium REAL,
	calcium REAL,
	zinc REAL,
	potassium REAL,
	iron REAL,
	iodine REAL,
	folate REAL,
    FOREIGN KEY (food_id) REFERENCES food(food_id))
    """
)

cursor.execute("""CREATE TABLE food_nutrients (
    food_id INT,
    carbohydrates REAL,
    fats REAL,
    proteins REAL,
    FOREIGN KEY (food_id) REFERENCES food(food_id))
    """
)

connection.commit()
connection.close()
