import streamlit as st
import requests

st.title("🍽️ Food API App")  # set title

dish = st.text_input("Enter Dish Name : ")  # set input text
# Search_Food_Recipe_Using_Api
api_key = "Your_Api_Key"  # API key

if st.button("🔍 Search"):
    if dish:
        url = f'https://api.spoonacular.com/recipes/complexSearch?query={dish}&number=20&apiKey={api_key}'  # Reduced number to 10

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if data["results"]:
                for x in data["results"]:
                    st.subheader(x["title"])
                    st.image(x["image"], caption=x["title"], use_container_width=True)

                    recipe_id = x["id"]
                    recipe_url = f'https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}'

                    recipe_response = requests.get(recipe_url)
                    if recipe_response.status_code == 200:
                        recipe_data = recipe_response.json()
                        if 'instructions' in recipe_data:
                            st.write("### Recipe : ")
                            st.write(recipe_data["instructions"])
                        else:
                            st.warning("Recipe Instruction Not Available :(")
                    else:
                        st.error(f"Failed to fetch recipe details: {recipe_response.status_code}")
            else:
                st.warning("Recipe Not Found :(")
        else:
            st.error(f"API request failed with status {response.status_code}: {response.text}")
    else:
        st.error("Please enter a dish name")
