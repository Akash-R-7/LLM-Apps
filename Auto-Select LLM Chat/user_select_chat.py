import ollama
import streamlit as st
from streamlit_extras.tags import tagger_component
from streamlit_option_menu import option_menu

from model_details import models_and_details
from prompts import wizard_math_template


st.markdown("<h2 style='text-align: center;'>User-Select LLM Chatbot</h2>", unsafe_allow_html=True)

# initialize history
# list where messages(dict of roles and content) are to be appended
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# init models
if "model" not in st.session_state:
    st.session_state["model"] = ""


query_category = ""
selected_model = ""
top_p = 0.95

temperature_dict = {"Precise": 0.1,
                        "Balanced": 0.5,
                        "Creative": 1}

temperature = temperature_dict[option_menu("Choose a conversation style",
                                        ["Precise", "Balanced", "Creative"],
                                        default_index=1,
                                        icons=['cursor']*3,
                                        orientation="horizontal",
                                        styles = {"menu-title": {"text-align": "center", "font-size":"20px"},
                                                "icon": {"font-size": "20px"}, 
                                                "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                                                "nav-link-selected": {"background-color": "green"},
                                                }
                                                )] 
category_models, model_details_df = models_and_details()


# Selecting categoty and displaying model details
with st.sidebar:
    with st.container(border=True):
        query_category = st.selectbox("Select category", list(category_models.keys()))
        selected_model = category_models[query_category]
        st.subheader("Model selected: "+selected_model, divider='rainbow')

        paper_link = model_details_df[model_details_df['model']==selected_model]['Paper'].to_string(index=False)
        st.page_link(paper_link, label="Technical Report", icon="📝")

        hub_link = model_details_df[model_details_df['model']==selected_model]['Model Hub'].to_string(index=False)
        st.page_link(hub_link, label="Model Hub", icon="🏛️")

        tag_list = model_details_df[model_details_df['model']==selected_model]['Tags'].values.tolist()[0]
        tagger_component("Tags: ", tag_list, color_name=["blue", "orange", "green", "yellow", "pink"][:len(tag_list)])

        with st.popover("Tip 💡"):
            prompt_tip = model_details_df[model_details_df['model']==selected_model]['Tips'].to_string(index=False)
            st.markdown(prompt_tip)


# getting responses
def model_resp_generator():
    
    if st.session_state["model"] == "Math":
        stream = ollama.chat(
        model=st.session_state["model"],
        messages=st.session_state["messages"],
        options={"temperature": temperature,
                 "top_k": 40,
                 "top_p": top_p},
        template=wizard_math_template,
        stream=True,
    )
    else:
        stream = ollama.chat(
            model=st.session_state["model"],
            messages=st.session_state["messages"],
            options={"temperature": temperature,
                    "top_k": 40,
                    "top_p": top_p},
            stream=True,
        )
    
    for chunk in stream:
        yield chunk["message"]["content"]


# Displaying previous chats from history on rerun
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What's up?"):

    # adding latest message to {role, content}
    st.session_state["messages"].append({"role": "user",
                                        "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    
    with st.chat_message("assistant"):
        
        st.session_state["model"] = selected_model
                
        # Answering with the selected model
        message = st.write_stream(model_resp_generator)

        st.session_state["messages"].append({"role": "assistant",
                                            "content": message})
        
        
    
