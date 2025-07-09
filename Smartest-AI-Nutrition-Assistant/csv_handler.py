import csv
import os

# Function to save user response to a CSV file
def save_user_response(name, age, goal, diet, allergies, user_input, response):
    csv_file_path = 'Smartest-AI-Nutrition-Assistant/user_responses.csv'
    
    file_exists = os.path.isfile(csv_file_path)
    
    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Age', 'Goal', 'Diet', 'Allergies', 'User  Input', 'Response']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'Name': name,
            'Age': age,
            'Goal': goal,
            'Diet': diet,
            'Allergies': ', '.join(allergies),
            'User  Input': user_input,
            'Response': response
        })
