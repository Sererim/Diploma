food {
	id int pk
	food_id int
	food_name string
}

food_vitamins {
	id int pk increments
	food_id int > food.id
	vitamin_d double
	vitamin_c double
	vitamin_e double
	vitamin_a double
	vitamin_b6 double
	vitamin_l double
	magnesium double
	calcium double
	zinc double
	potassium double
	iron double
	iodine double
	folate double
}

food_nutrients {
	id int pk increments > food.id
	carbohydrates int
	fats int
	proteins int
}

