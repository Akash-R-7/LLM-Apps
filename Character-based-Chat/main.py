import ollama
import streamlit as st
from streamlit_image_select import image_select
from collections import defaultdict 
  
      

d = defaultdict(list)

st.title("Character-based Chatbot")

# initialize history
# dict(of key characters) where list of each character messages(dict of roles and content) are appended
# instead of list where messages(dict of roles and content) was appended
if "messages" not in st.session_state:
    st.session_state["messages"] = d

# init models
if "model" not in st.session_state:
    st.session_state["model"] = ""

character_models = {"Harry Potter": "harry-potter",
                    "Matt Murdock": "daredevil",
                    "Michael Scott": "mike-scott"}
char_names = ["Harry Potter", "Matt Murdock", "Michael Scott"]

base_path = "Character Images/"

# Option 1
# character_name = st.selectbox("Choose your character", char_names)

# Option 2
character_name = char_names[image_select("Select a character",
                    [base_path+char_names[0]+".jpg", base_path+char_names[1]+".jpg", base_path+char_names[2]+".jpg"],
                    captions=char_names, return_value="index")]



st.session_state["model"] = character_models[character_name]

def model_resp_generator():
    stream = ollama.chat(
        model=st.session_state["model"],
        messages=st.session_state["messages"][character_name],
        stream=True,
    )
    for chunk in stream:
        yield chunk["message"]["content"]


# Displaying chats from history on rerun
for char_message in st.session_state["messages"][character_name]:
    with st.chat_message(char_message["role"]):
        st.markdown(char_message["content"])

if prompt := st.chat_input("What's up?"):
    # adding latest message to {role, content}
    st.session_state["messages"][character_name].append({"role": "user",
                                                        "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message = st.write_stream(model_resp_generator)
        st.session_state["messages"][character_name].append({"role": "assistant",
                                                              "content": message})
    
