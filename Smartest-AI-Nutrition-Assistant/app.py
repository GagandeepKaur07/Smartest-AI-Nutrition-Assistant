import streamlit as st
from nutrition_assistant import get_nutrition_response
from csv_handler import save_user_response
from nutrition_data import load_nutrition_data, get_nutrition_info
from streamlit_chat import message  
import base64  

# Load Dataset 
nutrition_df = load_nutrition_data("Smartest-AI-Nutrition-Assistant/preprocessed_healthy_diet_recipes.csv")

# Page Settings 
# def set_background(image_file):
#     with open(image_file, "rb") as f:
#         img_data = f.read()
#     b64_encoded = base64.b64encode(img_data).decode()
#     style = f"""
#         <style>
#         .stApp {{
#             background-image: url(data:image/png;base64,{b64_encoded});
#             background-size: cover;
#             background-position: center;
#             background-repeat: no-repeat;
#             background-attachment: fixed;
#             background-color: rgba(255, 255, 255, 0.9);
#             background-blend-mode: multiply;
#         }}
#         </style>
#     """
#     st.markdown(style, unsafe_allow_html=True)
'''def set_background(image_file):
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-color: rgba(255, 255, 255, 0.5);
            background-blend-mode: overlay;
        }}
        body, .stApp, .stMarkdown, .css-18e3th9, .css-1d391kg, .stTextInput, .stSelectbox, .stMultiselect, .stNumberInput, .stRadio {{
            color: black !important;
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)'''

def set_background_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.unsplash.com/photo-1605296867304-46d5465a13f1");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-color: rgba(255, 255, 255, 0.5);
            background-blend-mode: overlay;
        }}
        body, .stApp, .stMarkdown, .css-18e3th9, .css-1d391kg, .stTextInput, .stSelectbox, .stMultiselect, .stNumberInput, .stRadio {{
            color: black !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the new function
set_background_url()

set_background('background.jpg')  
# CSS
st.markdown("""
<style>
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 5px solid #2196f3;
    }
    .assistant-message {
        background-color: #f1f8e9;
        border-left: 5px solid #8bc34a;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    }
</style>
""", unsafe_allow_html=True)

# App Layout
st.title("🍏 The Smartest AI Nutrition Assistant")
st.markdown("""
<div style="border-bottom: 2px solid #4CAF50; padding-bottom: 10px; margin-bottom: 20px;">
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header(" Your Profile")
    st.image('Icon.png', width=150)  
    
    with st.expander("Personal Details", expanded=True):
        name = st.text_input("Name:")
        age = st.number_input("Age:", min_value=1, max_value=120)
        
    with st.expander("Dietary Preferences", expanded=True):
        goal = st.radio("Your Goal:", 
                       ["Weight Loss", "Muscle Gain", "Healthy Maintenance"],
                       key="goal")
        
        diet = st.selectbox("Diet Type:", 
                           ["Omnivore", "Vegetarian", "Vegan", "Keto", "Paleo", "Gluten-Free"],
                           key="diet")
        
        allergies = st.multiselect("Allergies/Intolerances:",
                                 ["Nuts", "Dairy", "Gluten", "Eggs", "Shellfish", "None"],
                                 default=["None"])

# Chat Interface
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hello! I'm your AI Nutrition Assistant. How can I help you today?"]
if 'past' not in st.session_state:
    st.session_state['past'] = []

# Response Generator
def generate_response():
    if user_input and name and age:
        try:
            query = f"My goal is {goal}, I prefer {diet} diet and I'm allergic to {', '.join(allergies)}.\n\nUser question: {user_input}"
            
            if any(keyword in user_input.lower() for keyword in ['nutrition', 'recipe', 'food', 'meal']):
                food_name = user_input.split(" for")[-1].strip() if " for" in user_input.lower() else user_input
                nutrition_info = get_nutrition_info(food_name, nutrition_df)
                if nutrition_info:
                    return f"Here's what I found about {food_name}:\n\n{str(nutrition_info)}"
            
            with st.spinner("Let me think..."):
                answer = get_nutrition_response(query)
                save_user_response(name, age, goal, diet, allergies, user_input, answer)
                return answer
        except Exception as e:
            return f"Error occurred: {str(e)}"
    else:
        return "Please complete your profile first!"

# Chat Container
chat_container = st.container()
response_container = st.container()

with chat_container:
    with st.form(key='chat_form', clear_on_submit=True):
        user_input = st.text_area("Ask me about nutrition, recipes, or meal plans:", key='input', height=80)
        submit_button = st.form_submit_button(label='Ask')

# Chat Display
if submit_button and user_input:
    output = generate_response()
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

with response_container:
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            if i < len(st.session_state['past']):
                message(st.session_state['past'][i], is_user=True, key=f"user_{i}")
            message(st.session_state["generated"][i], key=f"ai_{i}", logo="🍏")

# Features Section
st.divider()
st.subheader(" Features")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**Personalized Meal Plans**\n\nTailored to your dietary needs")
with col2:
    st.markdown("**Nutrition Analysis**\n\nDetailed breakdown of macros & micros")
with col3:
    st.markdown("**Recipe Suggestions**\n\nHealthy meals based on preferences")

# Footer
st.markdown("""<hr style="margin-top:30px; margin-bottom:10px;">""", unsafe_allow_html=True)
st.markdown(
    '<div style="text-align: center; color: black; font-size: 14px;">'
    '© NutriGAS3 | AIPA | 2025'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("""
<style>
div.stButton > button {
    background-color: #00ffff ;  
    color: black ;
    border: 1px solid #388E3C ;
    border-radius: 20px ;
    padding: 8px 20px ;
    font-weight: bold ;
    font-size: 16px ;
}
</style>
""", unsafe_allow_html=True)
