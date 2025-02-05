# Food API App

## Description
The **Food API App** is a simple Streamlit web application that allows users to search for recipes based on a dish name. It fetches data from the Spoonacular API and displays relevant recipes along with their images and instructions.

## Features
- Users can enter a dish name and retrieve up to 10 related recipes.
- Displays recipe titles and images.
- Fetches and displays detailed cooking instructions.
- Handles API request failures gracefully with user-friendly messages.

## Technologies Used
- **Python**
- **Streamlit** (for building the web app)
- **Requests** (for making API calls)
- **Spoonacular API** (for fetching recipes)

## Installation
1. Clone this repository or copy the script.
2. Install required dependencies:
   ```sh
   pip install streamlit requests
   ```
3. Run the application:
   ```sh
   streamlit run app.py
   ```

## Configuration
Before running the application, replace `"Your-API-Key"` with your actual Spoonacular API key in the script:
```python
api_key = "Your-API-Key"  # Insert your actual API key
```
You can obtain an API key by signing up at [Spoonacular](https://spoonacular.com/food-api).

## Usage
1. Enter a dish name in the input field.
2. Click the **"Searcg"** button.
3. View the retrieved recipes along with their images and instructions.

## Error Handling
- If no recipes are found, a warning message is displayed.
- If the API request fails, an error message is shown.
- If recipe instructions are missing, the app notifies the user.

## Example Output
- **Dish Name:** "Pasta"
- **Result:** A list of pasta recipes with images and cooking steps.

## License
This project is open-source and can be modified as per requirements.

## Author
Developed by Anjali Dahake


