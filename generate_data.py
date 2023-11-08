import random
import csv

def generate_random_data(num_items):
    data = []
    for _ in range(num_items):
        food_item = f"Food{random.randint(1, 100)}"
        calories = random.randint(50, 500)
        protein = round(random.uniform(0.5, 50), 1)
        carbohydrates = round(random.uniform(5, 100), 1)
        fat = round(random.uniform(0.1, 30), 1)
        data.append([food_item, calories, protein, carbohydrates, fat])
    return data

def save_to_csv(data, file_path):
    with open(file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Food Item", "Calories", "Protein", "Carbohydrates", "Fat"])
        csvwriter.writerows(data)

if __name__ == "__main__":
    num_items = 20
    generated_data = generate_random_data(num_items)
    save_to_csv(generated_data, "food_data.csv")
    print(f"{num_items} random food items with nutrient data have been saved to 'food_data.csv'.")
