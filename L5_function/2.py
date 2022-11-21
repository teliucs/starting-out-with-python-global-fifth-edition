# 2 A nutritionist who works for a fitness club helps members by evaluating their diets. As part of her evaluation, she asks members for the number of fat grams and carbohydrate grams that they consumed in a day. Then, she calculates the number of calories that result from the fat, using the following formula:  calories_from_fat=fat_grams×9 

# Next, she calculates the number of calories that result from the carbohydrates, using the following formula:  calories_from_carbs=carb_grams×4 

# The nutritionist asks you to write a program that will make these calculations.

def init():
    print("I can calculate the number of calories that result from the" + 
          " fat and the number of calories that result from the carbohydrates")

def calories(fat_grams, carb_grams):
    calories_from_fat = fat_grams * 9 
    calories_from_carb = carb_grams * 4 
    print(f"From fat he takes: {calories_from_fat:,} cal a day.")
    print(f"From carbs he takes: {calories_from_carb:,} cal a day.")

def main():
    init()
    
    fat_grams = int(input("Number of fat grams that they consumed in a day: "))
    carb_grams = int(input("Number of carbohydrate grams that they consumed in a day: "))
    
    calories(fat_grams, carb_grams)
    
main()

