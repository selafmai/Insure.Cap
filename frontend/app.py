import streamlit as st
from PIL import Image

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2
from clarifai.client.model import Model
import io
import base64

PAT = 'a90021e0adb7490c95e36f65f6d0974d'
# Specify the correct user_id/app_id pairings
# Since you're making inferences outside your app's scope
USER_ID = 'openai'
APP_ID = 'chat-completion'
# Change these to whatever model and text URL you want to use
MODEL_ID = 'gpt-4-vision-alternative'
MODEL_VERSION_ID = '12b67ac2b5894fb9af9c06ebf8dc02fb'
RAW_TEXT = 'I love your product very much'

def get_image_details(image):
    prompt = """As an image analysis specialist, meticulously examine the provided image. 
                Identify and describe the prominent features and patterns, using your expertise to deduce insights. 
                Craft your explanation to be understandable to a non-specialist audience, yet detailed enough to reflect your specialist knowledge. 
                Describe the image. Additionally, outline from image the caption objects and items with the attribute recognition. 
                If there are OCR captions, also extract this data from the image.Outline the image description like a plain paragraph text with a few sentences.
                Additional outline in bullets points the KEY ELEMENTS if there is present the: -[item] caption\n-[object] detection\n-[attribute] recognition\n-[image] segmentation\n-[OCR] text and number extraction\n-[adjective] semantic search\n-[subject] from the image\n-[doing action]\n-[mobility]\n-[transportation]\n-[person]\n-[animal]\n-[furniture]\n-[electronics]\n-[house appliances]\n-[landscape]\n-[environment]\n-[liability] context search\n  
                Outline only the captioned KEY ELEMENTS categories as bullet points.
                Finish with a bold caption that encapsulates your analysis in a brief statement."""

    # image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"

    openai_api_key = PAT

    inference_params = dict(temperature=0.2, max_tokens=200, image_base64=image)

    # Model Predict
    model_prediction = Model("https://clarifai.com/openai/chat-completion/models/gpt-4-vision").predict_by_bytes(prompt.encode(), input_type="text", inference_params=inference_params)
    data = model_prediction.outputs[0].data.text.raw
    return data

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
                image_bytes = io.BytesIO()
                image.save(image_bytes,format=image.format)
                image_bytes = image_bytes.getvalue()
                
                base64_image = base64.b64encode(image_bytes).decode('utf-8')
                
                captions = get_image_details(base64_image)
                st.write(captions)
                
            
                
            
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
