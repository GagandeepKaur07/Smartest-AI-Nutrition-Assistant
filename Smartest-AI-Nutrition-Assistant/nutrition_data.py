import pandas as pd

# preprocessed dataset
def load_nutrition_data(file_path='Smartest-AI-Nutrition-Assistant
/preprocessed_healthy_diet_recipes.csv'):
    return pd.read_csv(file_path)

# Function to get nutrition information
def get_nutrition_info(food_name, df):
    food_info = df[df['Recipe'].str.contains(food_name, case=False, na=False)]
    if not food_info.empty:
        return food_info.iloc[0].to_dict()
    else:
        return None
