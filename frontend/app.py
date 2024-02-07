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
Prompt: The **role**: Act as enriched caption vision expert agent that compile a vision computation as caption object detector, attribute recognition, items from image, OCR.

The **task**: Describe the image. Additionally outline from image the caption items with the attribute recognition. If there are OCR caption also extract this data from the image.

The **instructions**: Outline the image description like a plain paragraph text in the English language with a few sentences.

Additional outline in bullets points the KEY ELEMENTS if is there present the:

- [image] classification
- [item] caption
- [object] detection
- [attribute] recognition
- [image] segmentation
- [OCR] text and number extraction
- [adjective] semantic search
- [subject] from the image
- [doing action]
- [ownership]
- [mobility]
- [person]
- [animal]
- [furniture]
- [house appliances]
- [electronics]
- [landscape]
- [environment]
- [liability] context search

Always write and respond in the English language. Outline only the captioned KEY ELEMENTS categories as bullet points.

First: describe the image!

Second: nurture a possible risk and hazard exposure for the captioned categories.

Third: outline an insurance coverage insight of captioned items!

Forth: compile 5 question storyboard that emphasises the text game play which scores the coverage understanding of insurance product and the propensity for the risk adversity of itemised hazards.

The **context**: Knowing that the outline will be used as embedding retrieval dataset that compile agent architecture to nurture the right insurance coverage and instruct to the customer for the prevention behavior that decrease risks and derisk hazards.
                                                                                                                                                                                          

                    
                    st.session_state.messages.append({"role": "user", "content": prompt})
                    st.session_state.messages.append({"role": "assistant", "content": prompt})
                with st.container(height=654):
                    for message in st.session_state.messages: # Display the prior chat messages
                        with st.chat_message(message["role"]):
                            st.write(message["content"])
                    
     

            


if __name__ == "__main__":
    main()
