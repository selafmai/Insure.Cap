import streamlit as st
from PIL import Image

def main():
    st.set_page_config(layout="wide")  # Set the entire page to wide layout

    option = st.sidebar.selectbox("Choose an option", ["Upload Image"])
    chat_enable = True
   
    # Set the width of the entire page
    

    # Divide the page into two columns
    col1, col2 = st.columns([1, 2])  # Adjust the relative widths as needed
    

    
    with col1:
        st.header("Upload an Image")

    if option == "Upload Image":
        with col1:
            uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
            if uploaded_file is not None:
                chat_enable = False
                image = Image.open(uploaded_file)
                st.image(image, caption='Uploaded Image', use_column_width=True)
                
            
                
            
        with col2:
            
                if "messages" not in st.session_state.keys(): # Initialize the chat message history
                    st.session_state.messages = [
                        {"role": "assistant", "content": "Ask me a question about Streamlit's open-source Python library!"}
                    ]
                
                        
                if prompt := st.chat_input(placeholder="Your question", disabled=chat_enable): # Prompt for user input and save to chat history

                    st.session_state.messages.append({"role": "user", "content": prompt})
                    st.session_state.messages.append({"role": "assistant", "content": prompt})
                with st.container(height=654):
                    for message in st.session_state.messages: # Display the prior chat messages
                        with st.chat_message(message["role"]):
                            st.write(message["content"])
                    
     

            


if __name__ == "__main__":
    main()
