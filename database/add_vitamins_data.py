import sqlite3

connection = sqlite3.connect("database/Food.db")
cursor = connection.cursor()

_MK: float = 0.000001
_MG: float = 0.001


pancake = {
    'food_id'    :  72,
    'vitamin_d'  : 0,
	'vitamin_c'  : 0.3,
	'vitamin_e'  : 0,
	'vitamin_a'  : 54 * _MK,
	'vitamin_b6' : 0.046 * _MG,
	'vitamin_l'  : 0,
	'magnesium'  : 0,
	'calcium'    : 219,
	'zinc'       : 0.56,
	'potassium'  : 132 * _MG,
	'iron'       : 1.8 * _MG,
	'iodine'     : 0,
	'folate'     : 38 * _MK
}

hot_dogs = {
    'food_id'    :  55,
    'vitamin_d'  : 0.9 * _MK,
	'vitamin_c'  : 0,
	'vitamin_e'  : 0.51 * _MG,
	'vitamin_a'  : 3 * _MK,
	'vitamin_b6' : 0.104 * _MG,
	'vitamin_l'  : 0,
	'magnesium'  : 0,
	'calcium'    : 15 * _MG,
	'zinc'       : 2.06 * _MG,
	'potassium'  : 326 * _MG,
	'iron'       : 1.14 * _MG,
	'iodine'     : 0,
	'folate'     : 0
}

hamburgers = {
    'food_id'    :  53,
    'vitamin_d'  : 0.1 * _MK,
	'vitamin_c'  : 0.3 * _MG,
	'vitamin_e'  : 0.07 * _MG,
	'vitamin_a'  : 3 * _MK,
	'vitamin_b6' : 0.108 * _MG,
	'vitamin_l'  : 1000 * _MK,
	'magnesium'  : 22 * _MG,
	'calcium'    : 116 * _MG,
	'zinc'       : 2.03 * _MG,
	'potassium'  : 197 * _MG,
	'iron'       : 2.87 * _MG,
	'iodine'     : 0,
	'folate'     : 17 * _MK
}

fried_rice = {
    'food_id'    :  44,
    'vitamin_d'  : 0,
	'vitamin_c'  : 3.2 * _MG,
	'vitamin_e'  : 0.17 * _MG,
	'vitamin_a'  : 20 * _MK,
	'vitamin_b6' : 0.064 * _MG,
	'vitamin_l'  : 3 * _MK,
	'magnesium'  : 12 * _MG,
	'calcium'    : 12 * _MG,
	'zinc'       : 0.83 * _MG,
	'potassium'  : 100 * _MG,
	'iron'       : 0.5 * _MG,
	'iodine'     : 0,
	'folate'     : 6 * _MK
}

pizza = {
    'food_id'    :  76,
    'vitamin_d'  : 0.7 * _MK,
	'vitamin_c'  : 0.7 * _MG,
	'vitamin_e'  : 0,
	'vitamin_a'  : 0,
	'vitamin_b6' : 0.244 * _MG,
	'vitamin_l'  : 4600 * _MK,
	'magnesium'  : 27 * _MG,
	'calcium'    : 314 * _MG,
	'zinc'       : 2.74 * _MG,
	'potassium'  : 302 * _MG,
	'iron'       : 0.97 * _MG,
	'iodine'     : 0,
	'folate'     : 14 * _MK
}

foods = [pancake, hot_dogs, hamburgers, fried_rice, pizza]


for item in foods:
	cursor.execute("INSERT INTO food_vitamins \
                (food_id, vitamin_d, vitamin_c, vitamin_e, vitamin_a, vitamin_b6, vitamin_l, magnesium, calcium, zinc, potassium, iron, iodine, folate) \
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
               (item['food_id'], item['vitamin_d'], item['vitamin_c'], item['vitamin_e'], item['vitamin_a'], item['vitamin_b6'], 
                item['vitamin_l'], item['magnesium'], item['calcium'], item['zinc'], item['potassium'], item['iron'], item['iodine'], item['folate']))
 
connection.commit()
connection.close()
