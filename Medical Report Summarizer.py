import fitz  # PyMuPDF
from transformers import pipeline
import re  # Regular expression module
import time  # For controlling the speed of the typewriter effect
import streamlit as st
from streamlit.components.v1 import html
from datetime import datetime  # Import the datetime library
import base64
import os
from PIL import Image

#function to load the stetoscope image instead of emoji
def encode_image(image_path):
    """
    Encodes an image file as a Base64 string.
    
    Args:
        image_path (str): Path to the image file.
        
    Returns:
        str: Base64-encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()
image_path = "stetoscope.jpg"
#fetch the background image from directory 
def img_to_base64(img_path):
    try:
        with open(img_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        return encoded_string
    except FileNotFoundError:
        st.error("Image file not found at the specified path.")
        return None

# Image name
image_name = "Med_back.jpg"  # The local image file in directory

# Convert the image to base64
img_base64 = img_to_base64(image_name)

# If the image was successfully encoded, set it as the background
if img_base64:
    background_css = f"""
    <style>
    html, body, #root, .stApp {{
        height: 100%;
        margin: 0;
    }}
    .stApp {{
        background-image: url('data:image/jpg;base64,{img_base64}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        display: flex;
        flex-direction: column;
    }}
    body {{
        color: white;
    }}
    .streamlit-expanderHeader {{
        font-size: 20px;
        color: white;
    }}
    </style>
    """
    st.markdown(background_css, unsafe_allow_html=True)

# fetch the image for sidebar from directory 
def img_to_base64(img_path):
    try:
        with open(img_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        return encoded_string
    except FileNotFoundError:
        st.error("Image file not found at the specified path.")
        return None

# Load and display sidebar image
st.markdown(
    """
    <style>
    .cover-glow {
        width: 100%;
        height: auto;
        padding: 3px;
        box-shadow: 
            0 0 5px #330000,
            0 0 10px #660000,
            0 0 15px #990000,
            0 0 20px #CC0000,
            0 0 25px #FF0000,
            0 0 30px #FF3333,
            0 0 35px #FF6666;
        position: relative;
        z-index: -1;
        border-radius: 45px;
    }
.st-emotion-cache-12fmjuu {
    display: none !important;
}
    [data-testid="stSidebar"] .st-expander > div:first-child {
        color: black !important;  /* Ensure Help is always black */
        font-weight: bold;
    }
        .st-expanderHeader {
        color: black !important;  /* Ensure Help is always black */
    }
            st-emotion-cache-12fmjuu {
        display: none;
    </style>
    """,
    unsafe_allow_html=True,
)
img_path = "botdna_logo-05.png"
img_base64 = img_to_base64(img_path)
if img_base64:
    st.sidebar.markdown(
        f'<img src="data:image/png;base64,{img_base64}">',
        unsafe_allow_html=True,
    )

st.sidebar.write('')
st.sidebar.write('')    
import streamlit as st
import base64

# Function to encode the image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Encode the stethoscope image
image_base64 = encode_image("stetoscope.jpg")

# Display the heading with the image beside it in the sidebar
st.sidebar.markdown(
    f"""
    <h1 style='color: green; font-size: 24px;'>
        I want to
        <img src="data:image/jpeg;base64,{image_base64}" alt="stethoscope" style="height: 24px; vertical-align: middle;"/>
    </h1>
    """,
    unsafe_allow_html=True
)

# The rest of your Streamlit app code
nav = st.sidebar.radio(
    '',
    [
        ':green[Go to Homepage]', 
        ':green[Medical Report]',
        ':green[Virtual Health Assistants]',
        ':green[Radiology Image Analysis]',
        ':green[Personalized Treatment Plans]'
    ]
)

st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
#HOME
####
#Inject custom CSS to set the expander title color
st.markdown("""
    <style>
    .stSidebar .st-expander {
        color: black !important; /* Ensures text color stays black */
    }
    </style>
    """, unsafe_allow_html=True)

# Example sidebar expander
expander = st.sidebar.expander(':red[Help]')
expander.write(":red[Botdna.ai] (https://botdna.ai), botdna@ipath.io")

if nav == ':green[Go to Homepage]':

    # Use the function to encode the image
    image_base64 = encode_image("stetoscope.jpg")

    # Display the heading with the image beside the word "Healthbot"
    st.markdown(
        f"""
        <h1 style='text-align: center; color: #F63366; font-size:34px;'>
            Welcome to <span style='vertical-align: middle;'>BotDNA Healthcare Bot!</span>
            <img src="data:image/jpeg;base64,{image_base64}" alt="stetoscope" style="height: 34px; vertical-align: middle;"/>
        </h1>
        """,
        unsafe_allow_html=True
    )


    st.markdown("<h3 style='text-align: center; color: #F63366; font-size:20px;'>Summarize medical reports with ease and gain actionable insights in seconds. Interact with our AI-powered chatbot for accurate health guidance and personalized assistance!</h3>", unsafe_allow_html=True)
   
    st.markdown('___')
    st.write(':point_left: Use the menu at left to select a task (click on > if closed).')
    st.markdown('___')
    st.markdown("<h3 style='text-align: left; color:#F63366; font-size:18px;'><b>What is this App about?<b></h3>", unsafe_allow_html=True)
    st.write("The Generative AI App for Healthcare revolutionizes medical diagnostics by leveraging cutting-edge artificial intelligence and data analysis. It simplifies report summarization and provides personalized, accurate health insights for patients, doctors, and healthcare providers.")
    st.markdown("<h3 style='text-align: left; color:#F63366; font-size:18px;'><b>Who is this App for?<b></h3>", unsafe_allow_html=True)
    st.markdown(
                """
Here's a breakdown of the potential target audience for the Medical Report Summarizer and Chatbot:

-Patients and Caregivers: To easily understand complex medical reports and receive personalized health insights.\n
-Doctors and Healthcare Professionals: For quick report summaries and streamlined patient interactions.\n
-Hospitals and Clinics: To enhance patient care and optimize report analysis workflows.\n
-Medical Researchers and Analysts: For efficient data extraction and insights from medical documents.\n
-HealthTech Companies: To integrate advanced AI tools into their healthcare solutions.\n
-Educational Institutions: For teaching and training purposes in medical fields.
                """
                )
    
if nav == ':green[Medical Report]':
    # CSS to hide chat input in Tab 1 and cover it with a white background
    st.markdown("""
        <style>
        [data-testid="stChatInput"] {
        background-color: #D4EDEA; /* default white background */
            z-index:900;
        }
.st-emotion-cache-128upt6 {
    position: relative;
    bottom: 0px;
    width: 100%;
    min-width: 100%;
    background-color: rgb(212, 237, 234);
    display: flex
;
    flex-direction: column;
    -webkit-box-align: center;
    align-items: center;
}

        /* White background to cover the chat input in Tab 1 */
        .tab1-cover {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 100px; /* Adjust to cover chat input */
            background-color: #D4EDEA; /* Mint green color */
            z-index: 1000; /* Ensure cover is above chat input */
        }
        /* Initially hide chat input in Tab 1 */
        .hidden-chat-input {
            display: none !important;
        }
                    .st-emotion-cache-6qob1r {
            position: relative;
            height: 100%;
            width: 100%;
            overflow: overlay;
            color: #D4EDEA;
        }
        st-emotion-cache-12fmjuu {
        display: none;
    }
        </style>
        """, unsafe_allow_html=True)

    # JavaScript to handle the hiding and showing of chat input in different tabs
    st.markdown("""
        <script>
        window.onload = function() {
            const chatInput = document.querySelector("[data-testid='stChatInput']");
            const tab1 = document.querySelector('button[data-baseweb="tab"][id="0"]');
            const tab2 = document.querySelector('button[data-baseweb="tab"][id="1"]');
            
            // Hide chat input in Tab 1
            if (tab1) {
                tab1.addEventListener('click', () => {
                    chatInput.classList.add('hidden-chat-input');
                });
            }

            // Show chat input in Tab 2
            if (tab2) {
                tab2.addEventListener('click', () => {
                    chatInput.classList.remove('hidden-chat-input');
                });
            }
        };
        </script>
        """, unsafe_allow_html=True)

    if "chatbox_visible" not in st.session_state:
        st.session_state["chatbox_visible"] = False  # Initialize state
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    if "medical_progress_question" not in st.session_state:
        st.session_state["medical_progress_question"] = True
    if "show_doctor_patient_buttons" not in st.session_state:
        st.session_state["show_doctor_patient_buttons"] = False
    if "show_specialty_buttons" not in st.session_state:
        st.session_state["show_specialty_buttons"] = False
    if "selected_yes" not in st.session_state:
        st.session_state["selected_yes"] = False
    if "selected_no" not in st.session_state:
        st.session_state["selected_no"] = False
    if "selected_doctor" not in st.session_state:
        st.session_state["selected_doctor"] = False
    if "selected_patient" not in st.session_state:
        st.session_state["selected_patient"] = False
    if "selected_specialty" not in st.session_state:
        st.session_state["selected_specialty"] = None
    if "answer_showed" not in st.session_state:
        st.session_state["answer_showed"] = False
    if "selected_fee" not in st.session_state:
        st.session_state["selected_fee"] = None
    if "fee_selected" not in st.session_state:
        st.session_state["fee_selected"] = False
    if "appointment_booked" not in st.session_state:
        st.session_state["appointment_booked"] = False
    if "selected_appointment" not in st.session_state:
        st.session_state["selected_appointment"] = None
    if "selected_tablet" not in st.session_state:
        st.session_state.selected_tablet = None
    if "message" not in st.session_state:
        st.session_state.message = ""
    if "tablet_message" not in st.session_state:
        st.session_state.tablet_message = ""
    if "messages_chat" not in st.session_state:
        st.session_state["messages_chat"] = []
    if "report_clicked" not in st.session_state:
        st.session_state["report_clicked"] = True
    if "summary_shown" not in st.session_state:
        st.session_state["summary_shown"] = False
    if "Summary" not in st.session_state:
        st.session_state["Summary"] = False
    if "initial_prompt_shown" not in st.session_state:
        st.session_state.initial_prompt_shown = True
    if "selected_disease" not in st.session_state:
        st.session_state.selected_disease = None
    if "show_patient" not in st.session_state:
        st.session_state.show_patient = False
    if "condition" not in st.session_state:
        st.session_state.condition = False
    if "condition_shown" not in st.session_state:
        st.session_state.condition_shown = False
    if "yes_selected" not in st.session_state:
        st.session_state.yes_selected = False
    if "question" not in st.session_state:
        st.session_state.question = ""
    if "message_shown" not in st.session_state:
        st.session_state.message_shown = False
    if "initial_messages_added" not in st.session_state:
        st.session_state.initial_messages_added = False
    if "doctor_messages_added" not in st.session_state:
        st.session_state.doctor_messages_added = False
    if "patient_messages_added" not in st.session_state:
        st.session_state.patient_messages_added = False
    if "condition_messages_added" not in st.session_state:
        st.session_state.condition_messages_added = False
    if "breast_cancer" not in st.session_state:
        st.session_state.breast_cancer = False
    if "kidney_stone" not in st.session_state:
        st.session_state.kidney_stone = False
    if "prostate_cancer" not in st.session_state:
        st.session_state.prostate_cancer = False
    if "spinner_displayed" not in st.session_state:
        st.session_state.spinner_displayed = False
    if "sidebar_displayed" not in st.session_state:
        st.session_state.sidebar_displayed = True


    if "selected_role" not in st.session_state:
        st.session_state.selected_role = None
    if "condition" not in st.session_state:
        st.session_state.condition = None
    if "output" not in st.session_state:
        st.session_state.output = ""  # Stores the generated output for typewriter effect
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []  # Stores the chat history for the conversation
    if "interaction_count" not in st.session_state:
        st.session_state.interaction_count = 0
    if "last_displayed_index" not in st.session_state:
        st.session_state.last_displayed_index = 0
    if "chat_history_doctor" not in st.session_state:
        st.session_state.chat_history_doctor = []
    if "chat_history_medical" not in st.session_state:
        st.session_state.chat_history_medical = []
    if "chat_history_patient" not in st.session_state:
        st.session_state.chat_history_patient = []
    if "chat_history_condition" not in st.session_state:
        st.session_state.chat_history_condition = []
    if "chat_history_condition_chat" not in st.session_state:
        st.session_state.chat_history_condition_chat = []
    if "chat_history_condition_last" not in st.session_state:
        st.session_state.chat_history_condition_last = []
    if "First_medical" not in st.session_state:
        st.session_state.First_medical = False
    if "second_medical" not in st.session_state:
        st.session_state.second_medical = False
    if "third_medical" not in st.session_state:
        st.session_state.third_medical = False
    if "show_role_buttons" not in st.session_state:
        st.session_state.show_role_buttons = True
    if "chat_history_summary" not in st.session_state:
        st.session_state.chat_history_summary = []
    if "chat_number" not in st.session_state:
        st.session_state.chat_number = 1
    if "show_questions" not in st.session_state:
        st.session_state.show_questions = False
    if "button_pressed" not in st.session_state:
        st.session_state.button_pressed = None
    if "show_spinner" not in st.session_state:
        st.session_state.show_spinner = False
    if "follow_up_prompt" not in st.session_state:
        st.session_state.follow_up_prompt = False


    breast_cancer = [
        "What are the early symptoms of breast cancer?",
        "How is breast cancer diagnosed?",
        "What are the available treatment options for breast cancer?",
    ]

    kidney_stone = [
        "What are the symptoms of kidney stones?",
        "How can kidney stones be prevented?",
        "What are the treatment options for large kidney stones?",
    ]

    prostate_cancer = [
        "What are the risk factors for prostate cancer?",
        "How is prostate cancer detected early?",
        "What are the side effects of prostate cancer treatments?",
    ]

    example_prompts = [
        "What is the significance of both lobe involvement and seminal vesicle involvement(T3b)?\n\n",
        "What do a positive excision margin tumor extension to periprostatic tissue imply?\n\n",
        "Could you provide any recent research on adenocarcinoma of the prostate with a gleason score of 9",
    ]


    def display_summary():
        for message in st.session_state.chat_history_summary:
            if message["role"] == "user":
                st.chat_message("user").markdown(
                    f"{message['time']}\n\n<div style='padding: 10px; border-radius: 10px;'>{message['message']}</div>",
                    unsafe_allow_html=True,
                )
            elif message["role"] == "system":
                if not st.session_state.get("First_medical", False):
                    with st.spinner("🩺Generating summary..."):
                        typewriter_text = ""
                        with st.chat_message("assistant"):
                            typewriter_container = st.empty()
                            for char in message["message"]:
                                typewriter_text += char
                                typewriter_container.markdown(
                                    f"{message['time']}\n\n{typewriter_text}",
                                    unsafe_allow_html=True,
                                )
                                time.sleep(0.005)
                            st.session_state.First_medical = True
                else:
                    with st.chat_message("assistant"):
                        st.markdown(
                            f"{message['time']}\n\n{message['message']}",
                            unsafe_allow_html=True,
                        )


    def display_chat_history(chat_history_condition_last):
        for message in chat_history_condition_last:
            if not st.session_state.get("yes_or_no", False):
                if message["role"] == "user":
                    st.chat_message("user").markdown(
                        f"{message['time']}\n\n<div style='padding: 10px; border-radius: 10px;'>{message['message']}</div>",
                        unsafe_allow_html=True,
                    )
                elif message["role"] == "system":
                    typewriter_text = ""
                    with st.chat_message("assistant"):
                        typewriter_container = st.empty()
                        for char in message["message"]:
                            typewriter_text += char
                            typewriter_container.markdown(
                                f"<div style='padding: 10px; border-radius: 10px; background-color: #f0f0f0; display: flex; align-items: center;'>"
                                f"<div style='flex-grow: 1;'>"
                                f"<p style='margin: 0; font-size: 16px; color: black;'>{message['time']}</p>"
                                f"<p style='margin: 0;'>{typewriter_text}</p>"
                                f"</div>"
                                f"</div>",
                                unsafe_allow_html=True,
                            )
                            time.sleep(0.005)
                    st.session_state.yes_or_no = True
            else:
                st.chat_message("user").markdown(
                    f"{message['time']}\n\n<div style='padding: 10px; border-radius: 10px;'>{message['message']}</div>",
                    unsafe_allow_html=True,
                )
                with st.chat_message("assistant"):
                    st.markdown(
                        f"<div style='padding: 10px; border-radius: 10px; background-color: #f0f0f0; display: flex; align-items: center;'>"
                        f"<div style='flex-grow: 1;'>"
                        f"<p style='margin: 0; font-size: 16px; color: black;'>{message['time']}</p>"
                        f"<p style='margin: 0;'>{message['message']}</p>"
                        f"</div>"
                        f"</div>",
                        unsafe_allow_html=True,
                    )


    def display():
        # Display all the chat history
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.chat_message("user").markdown(
                    f"{message['time']}\n\n<div style='padding: 10px; border-radius: 10px;'>{message['message']}</div>",
                    unsafe_allow_html=True,
                )
            elif message["role"] == "system":
                st.chat_message("assistant").markdown(
                    f"{message['time']}\n\n<div style='padding: 10px;background-color: #f0f0f0; border-radius: 10px;'>{message['message']}</div>",
                    unsafe_allow_html=True,
                )


    def display_values():
        for message in st.session_state.chat_history_doctor:
            if message["role"] == "user":
                st.chat_message("user").markdown(
                    f"{message['time']}\n\n<div style='padding: 10px; border-radius: 10px;'>{message['message']}</div>",
                    unsafe_allow_html=True,
                )
            elif message["role"] == "system":
                if not st.session_state.get("second_medical", False): 
 
                        # Use a placeholder to simulate a spinner with an image and text
                        placeholder = st.empty()  # Create a placeholder for the spinner

                        # Start the spinner
                        with st.spinner(""):
                            # Display the spinner with image and text in the placeholder
                            placeholder.markdown(
                                f"""
                                <div style="display: flex; align-items: center;">
                                    <div class="spinner-border" role="status" style="margin-right: 8px;"></div>
                                    <img src="data:image/jpeg;base64,{image_base64}" alt="stetoscope" style="height: 24px; margin-right: 8px;"/>
                                    <span>Processing...</span>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )
                            # Simulate a delay or your processing logic
                            time.sleep(3)

                        # Clear the placeholder once processing is complete
                        placeholder.empty()


                        typewriter_text = ""
                        with st.chat_message("assistant"):
                            typewriter_container = st.empty()
                            for char in message["message"]:
                                typewriter_text += char
                                typewriter_container.markdown(
                                    f"{message['time']}\n\n{typewriter_text}",
                                    unsafe_allow_html=True,
                                )
                                time.sleep(0.05)
                            st.session_state.second_medical = True
                else:
                    with st.chat_message("assistant"):
                        st.markdown(
                            f"{message['time']}\n\n{message['message']}",
                            unsafe_allow_html=True,
                        )


    def display_medical():
        for message in st.session_state.chat_history_medical:
            if message["role"] == "user":
                st.chat_message("user").markdown(
                    f"{message['time']}\n\n<div style='padding: 10px; border-radius: 10px;'>{message['message']}</div>",
                    unsafe_allow_html=True,
                )
            elif message["role"] == "system":
                if not st.session_state.spinner_displayed:
                    # Use a placeholder to simulate a spinner with an image and text
                    placeholder = st.empty()  # Create a placeholder for the spinner

                    # Start the spinner
                    with st.spinner(""):
                        # Display the spinner with image and text in the placeholder
                        placeholder.markdown(
                            f"""
                            <div style="display: flex; align-items: center;">
                                <div class="spinner-border" role="status" style="margin-right: 8px;"></div>
                                <img src="data:image/jpeg;base64,{image_base64}" alt="stetoscope" style="height: 24px; margin-right: 8px;"/>
                                <span>Processing...</span>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                        # Simulate a delay or your processing logic
                        time.sleep(3)

                    # Clear the placeholder once processing is complete
                    placeholder.empty()

                    st.session_state.spinner_displayed = True
                st.chat_message("assistant").markdown(
                    f"{message['time']}\n\n<div style='padding: 10px; border-radius:background-color: #f0f0f0; 10px;'>{message['message']}</div>",
                    unsafe_allow_html=True,
                )


    def display_patient():
        for message in st.session_state.chat_history_patient:
            if message["role"] == "user":
                st.chat_message("user").markdown(
                    f"{message['time']}\n\n<div style='padding: 10px; border-radius: 10px;'>{message['message']}</div>",
                    unsafe_allow_html=True,
                )
            elif message["role"] == "system":
                st.chat_message("assistant").markdown(
                    f"{message['time']}\n\n<div style='padding: 10px;background-color: #f0f0f0; border-radius: 10px;'>{message['message']}</div>",
                    unsafe_allow_html=True,
                )


    def display_condition():
        for message in st.session_state.chat_history_condition:
            if message["role"] == "user":
                st.chat_message("user").markdown(
                    f"{message['time']}\n\n<div style='padding: 10px; border-radius: 10px;'>{message['message']}</div>",
                    unsafe_allow_html=True,
                )
            elif message["role"] == "system":
                if not st.session_state.get("second_medical", False):
# Use a placeholder to simulate a spinner with an image and text
                        placeholder = st.empty()  # Create a placeholder for the spinner

                        # Start the spinner
                        with st.spinner(""):
                            # Display the spinner with image and text in the placeholder
                            placeholder.markdown(
                                f"""
                                <div style="display: flex; align-items: center;">
                                    <div class="spinner-border" role="status" style="margin-right: 8px;"></div>
                                    <img src="data:image/jpeg;base64,{image_base64}" alt="stetoscope" style="height: 24px; margin-right: 8px;"/>
                                    <span>Processing...</span>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )
                            # Simulate a delay or your processing logic
                            time.sleep(3)

                        # Clear the placeholder once processing is complete
                        placeholder.empty()

                        typewriter_text = ""
                        with st.chat_message("assistant"):
                            typewriter_container = st.empty()
                            for char in message["message"]:
                                typewriter_text += char
                                typewriter_container.markdown(
                                    f"{message['time']}\n\n{typewriter_text}",
                                    unsafe_allow_html=True,
                                )
                                time.sleep(0.005)
                            st.session_state.second_medical = True
                else:
                    with st.chat_message("assistant"):
                        st.markdown(
                            f"{message['time']}\n\n{message['message']}",
                            unsafe_allow_html=True,
                        )


    def display_conditionchat():
        for message in st.session_state.chat_history_condition_chat:
            if message["role"] == "user":
                st.chat_message("user").markdown(
                    f"{message['time']}\n\n<div style='padding: 10px; border-radius: 10px;'>{message['message']}</div>",
                    unsafe_allow_html=True,
                )
            elif message["role"] == "system":
                if not st.session_state.spinner_displayed:
                    # Use a placeholder to simulate a spinner with an image and text
                    placeholder = st.empty()  # Create a placeholder for the spinner

                    # Start the spinner
                    with st.spinner(""):
                        # Display the spinner with image and text in the placeholder
                        placeholder.markdown(
                            f"""
                            <div style="display: flex; align-items: center;">
                                <div class="spinner-border" role="status" style="margin-right: 8px;"></div>
                                <img src="data:image/jpeg;base64,{image_base64}" alt="stetoscope" style="height: 24px; margin-right: 8px;"/>
                                <span>Processing...</span>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                        # Simulate a delay or your processing logic
                        time.sleep(3)

                    # Clear the placeholder once processing is complete
                    placeholder.empty()

                    st.session_state.spinner_displayed = True
                st.chat_message("assistant").markdown(
                    f"{message['time']}\n\n<div style='padding: 10px;background-color: #f0f0f0; border-radius: 10px;'>{message['message']}</div>",
                    unsafe_allow_html=True,
                )


    def display_last():
        for message in st.session_state.chat_history_condition_last:
            if message["role"] == "user":
                st.chat_message("user").markdown(
                    f"{message['time']}\n\n<div style='padding: 10px; border-radius: 10px;'>{message['message']}</div>",
                    unsafe_allow_html=True,
                )
            elif message["role"] == "system":
                st.chat_message("assistant").markdown(
                    f"{message['time']}\n\n<div style='padding: 10px;background-color: #f0f0f0; border-radius: 10px;'>{message['message']}</div>",
                    unsafe_allow_html=True,
                )


    def get_time():
        return datetime.now().strftime("%I:%M:%S %p")


    def typewriter_effect(container, message, delay=0.005):
        """
        Displays text in a typewriter effect within a Streamlit container.

        Args:
            container: Streamlit container for displaying the text.
            message: The full message to display.
            delay: Delay in seconds between each character.
        """
        text = ""
        for char in message:
            text += char
            container.markdown(
                f"<div style='padding: 10px;background-color: #f0f0f0; border-radius: 10px;'>{text}</div>",
                unsafe_allow_html=True,
            )
            time.sleep(delay)


    # Add this to ensure session state variables are initialized
    if "tab2_loading" not in st.session_state:
        st.session_state.tab2_loading = False  # Tracks loading state for Tab 2


    # Function to enable loading spinner
    def enable_tab2_spinner():
        st.session_state.tab2_loading = True


    # Function to disable loading spinner
    def disable_tab2_spinner():
        st.session_state.tab2_loading = False
    current_time = datetime.now().strftime("%I:%M:%S %p")

    if "tab2_name" not in st.session_state:
        st.session_state.tab2_name = "Interactive chatbot 🔒"
    if "summary_generated" not in st.session_state:
        st.session_state.summary_generated = (
            False  # Tracks if the summary has been generated
        )

    # Create two tabs in the Streamlit app
    tab1, tab2 = st.tabs(["Medical Report Summarizer", st.session_state.tab2_name])
    st.session_state.tab2_name = "Interactive chatbot"
    @st.cache_resource
    @st.cache_resource(show_spinner=False)
    def load_summarizer():
        return pipeline(
            "summarization", model="t5-small"
        )  # to load the summarization model

    summarizer = load_summarizer()
    # Content for Tab 1 (Medical Report Summarizer)
    with tab1:
        st.markdown('<div class="tab1-cover"></div>', unsafe_allow_html=True)

        # Call the existing encode_image function
        image_base64 = encode_image("stetoscope.jpg")

        # Display the heading with the image beside it
        st.markdown(
            f"""
            <h1 style='color: red; font-size: 34px;'>
                Medical Report Summarizer
                <img src="data:image/jpeg;base64,{image_base64}" alt="stetoscope" style="height: 34px; vertical-align: middle;"/>
            </h1>
            """,
            unsafe_allow_html=True
        )


        st.write(
            "Upload a medical report (PDF) to generate an accurate and concise summary."
        )

        # Function to preprocess and clean up text with regex-based corrections
        def preprocess_text(text):
            replacements = {
                r"pa\(ent": "patient",
                r"vomi\(ng": "vomiting",
                r"inform\s*at*ion": "information",
                r"specimen\s*exam\s*ination": "specimen examination",
                r"gross\s*exam\s*ination": "gross examination",
                r"LAB NUM BER": "LAB NUMBER",
                r"CLINICAL INFORM ATION": "CLINICAL INFORMATION",
                r"SPECIM EN": "SPECIMEN",
                r"GROSS EXAM INATION": "GROSS EXAMINATION",
                r"MICROSCOPY AND IM PRESSION": "MICROSCOPY AND IMPRESSION",
            }

            for pattern, replacement in replacements.items():
                text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

            text = re.sub(r"\b[A-Z\s]+\b", lambda match: match.group(0).lower(), text)

            unwanted_patterns = [
                r"#",  # Remove all occurrences of #
                r"\"",  # Remove all occurrences of double quotes
                r"‘",  # Remove all occurrences of left single quotes
                r"’",  # Remove all occurrences of right single quotes
                r"MRN\s*[:\-\w]+",  # MRN
                r"Visit\s*No\s*[:\-\w]+",  # Visit No
                r"Age\s*[:\d]+",  # Age
                r"Gender\s*[:\w]+",  # Gender
                r"Ordered\s*by\s*[:\w\s]+",  # Ordered by
                r"Sample\s*Receipt\s*Date\s*[:\w\s\-\d:]+",  # Sample Receipt Date
                r"Referred\s*by\s*[:\w\s]+",  # Referred by
                r"Reported\s*Date\s*[:\w\s\-\d:]+",  # Reported Date
                r"\b[a-zA-Z\s]*\d{2,4}-\d{2,4}-\d{4}\b",  # Removing date-like formats like 17-11-2022
                r"\b[a-zA-Z\s]*[0-9]{1,2}(:[0-9]{2}){1,2}[apm]+\b",  # Removing time formats like 11:53 am
            ]

            for pattern in unwanted_patterns:
                text = re.sub(pattern, "", text)

            text = re.sub(r"\(\s+", "(", text)
            text = re.sub(r"\s+\)", ")", text)
            return text.strip()

        # Function to extract text from a PDF file
        def extract_text_from_pdf(pdf_file):
            text = ""
            pdf = fitz.open(stream=pdf_file.read(), filetype="pdf")
            for page in pdf:
                text += page.get_text("text")
            pdf.close()
            return preprocess_text(text)

        # Function to extract relevant medical details from the text
        def extract_medical_info(text):
            # Check for conditions: kidney stone, breast biopsy, prostate cancer
            if "kidney stone" in text.lower():
                condition = "Kidney stone"
            elif "biopsy" in text.lower() and "breast" in text.lower():
                condition = "Breast cancer"
            elif "prostate" in text.lower():
                condition = "Prostate cancer"
            else:
                condition = "unknown"

            return condition

        # Function to construct the summary with proper formatting
        def construct_dynamic_summary(condition, text):
            additional_summary = summarizer(
                text, max_length=130, min_length=50, do_sample=False
            )[0]["summary_text"]

            final_summary = f"The report indicates a condition related to {condition}. {additional_summary}"
            final_summary = final_summary.replace("aen(on)", "attention.")

            # Ensure proper capitalization after a period
            final_summary = re.sub(
                r"(?<=\.\s)([a-z])", lambda x: x.group().upper(), final_summary
            )

            # Clean up spaces before punctuation
            final_summary = re.sub(r"\s+([.,;:])", r"\1", final_summary)

            # Ensure one space after a period (if not followed by punctuation or end of line)
            final_summary = re.sub(r"\.(?![.\s])", ". ", final_summary)

            # Strip any extra whitespace from the beginning and end
            final_summary = final_summary.strip()

            return final_summary

        def disable_summary_workflow():
            st.session_state.summary_workflow_enabled = False

        def enable_summary_workflow():
            """
            Re-enables summary generation logic if a new file is uploaded.
            """
            st.session_state.summary_workflow_enabled = True

        # Ensure session state variables are initialized
        if "summary_workflow_enabled" not in st.session_state:
            st.session_state.summary_workflow_enabled = True  # Enabled by default

        if "file_base_name" not in st.session_state:
            st.session_state.file_base_name = None

        uploaded_file = st.file_uploader("Upload PDF file", type="pdf")

        # checks whether a file has been uploaded
        if uploaded_file is not None:
            file_name = uploaded_file.name
            file_base_name = file_name.rsplit(".", 1)[0]
            # Check if a new file is uploaded and reset workflow state
            # Check if a new file is uploaded and reset workflow state
            if st.session_state.file_base_name != file_base_name:
                st.session_state.file_base_name = file_base_name
                enable_summary_workflow()  # Re-enable workflow for new file
                enable_tab2_spinner()
                # Reset Tab 2 state to ensure new interaction
                # Clear selected role in Tab 2
                st.session_state.new_report_uploaded = (
                    True  # Set flag that a new report is uploaded
                )
                st.session_state.no_selected = False
                # Add these lines to reset relevant session state variables
                st.session_state.selected_role = None
                st.session_state.condition = None
                st.session_state.chat_history = []
                st.session_state.chat_history_doctor = []
                st.session_state.chat_history_medical = []
                st.session_state.chat_history_patient = []
                st.session_state.chat_history_condition = []
                st.session_state.chat_history_condition_chat = []
                st.session_state.chat_history_condition_last = []
                st.session_state.patient_messages_added = False  # Ensure this is reset to False
                st.session_state.show_role_buttons = True
                st.session_state.selected_doctor = False
                st.session_state.selected_patient = False
                st.session_state.follow_up_prompt = False
                st.session_state.button_pressed = None
                st.session_state.condition_shown = False
                st.session_state.condition_messages_added = False
                st.session_state.breast_cancer = False
                st.session_state.kidney_stone = False
                st.session_state.prostate_cancer = False
                st.session_state.spinner_displayed = False
                st.session_state.yes_selected = False
                st.session_state.message_shown = False
                st.session_state.initial_messages_added = False
                st.session_state.doctor_messages_added = False
                st.session_state.First_medical = False
                st.session_state.second_medical = False
                st.session_state.third_medical = False
                st.session_state.summary_shown = False
                st.session_state.Summary = False
                st.session_state.show_questions = False
                st.session_state.button_pressed = None
                st.session_state.show_spinner = False
                st.session_state.follow_up_prompt = False
                st.session_state.selected_disease = None
                st.session_state.show_patient = False
                st.session_state.condition = False
                st.session_state.condition_shown = False
                st.session_state.yes_selected = False
                st.session_state.question = ""
                st.session_state.message_shown = False
                st.session_state.initial_messages_added = False
                st.session_state.doctor_messages_added = False
                st.session_state.patient_messages_added = False
                st.session_state.condition_messages_added = False
                st.session_state.breast_cancer = False
                st.session_state.kidney_stone = False
                st.session_state.prostate_cancer = False
                st.session_state.spinner_displayed = False
                st.session_state.sidebar_displayed = True
                del st.session_state.chat_history_condition_last
                st.session_state.no_selected = False
                st.session_state.message_shown = False
                st.rerun()

            if st.session_state.summary_workflow_enabled:
                with st.spinner("Processing Report..."):
                    pdf_text = extract_text_from_pdf(uploaded_file)

                if pdf_text:
                    # Encode the image using the existing function
                    image_base64 = encode_image("stetoscope.jpg")

                    # Use a placeholder to simulate a spinner with an image and text
                    placeholder = st.empty()  # Create a placeholder for the spinner

                    with st.spinner(""):
                        # Display the spinner with image and text in the placeholder
                        placeholder.markdown(
                            f"""
                            <div style="display: flex; align-items: center;">
                                <img src="data:image/jpeg;base64,{image_base64}" alt="stetoscope" style="height: 24px; margin-right: 8px;"/>
                                <span>Generating summary...</span>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                        # Simulate a delay or your processing logic
                        import time
                        time.sleep(3)

                    # Clear the placeholder once processing is complet



                        condition = extract_medical_info(pdf_text)
                        summary = construct_dynamic_summary(condition, pdf_text)
                    placeholder.empty()
                    # Save summary and condition to session state
                    st.session_state.summary = summary  # Save summary to session state
                    st.session_state.condition = (
                        condition  # Store the condition in session state
                    )
                    st.session_state.summary_generated = (
                        True  # Set the flag for summary generation
                    )
                    st.markdown(f"**The summary for {file_base_name} is as follows:**\n\n")
                    final_summary = summary


                    # Use st.chat_message for the assistant effect
                    
                    typewriter_container = st.empty()  # Placeholder for typewriter effect
                    typewriter_text = ""

                    # Generate the typewriter effect for the assistant's message
                    for char in final_summary:
                        typewriter_text += char
                        typewriter_container.markdown(
                            f"<div style='padding: 10px; border-radius: 10px; background-color: #f0f0f0; display: flex; align-items: center;'>"
                            f"<div style='flex-grow: 1;'>"
                            f"<p style='margin: 0; font-size: 16px; color: block;'></p>"
                            f"<p style='margin: 0;'>{typewriter_text}</p>"
                            f"</div>"
                            f"</div>",
                            unsafe_allow_html=True,
                        )
                        time.sleep(0.01)  # Delay for typewriter effect

                    # Additional message or error handling after the summary
                    disable_summary_workflow()

                else:
                    st.error("Unable to extract text from the uploaded PDF.")

    # Content for Tab 2 (Interactive Chatbot)
    with tab2:

        if st.session_state.selected_role:
            st.rerun()
        if "chat_input_visible" not in st.session_state:
            st.session_state.chat_input_visible = True
        if st.session_state.get("new_report_uploaded", False):
            # Clear chat history in Tab 2 for both Patient and Practitioner
            st.session_state.chat_history_condition_chat = []  # Clear chat history
            st.session_state.chat_history_condition_last = []  # Clear last chat history

            # Reset any flags related to follow-up prompts or button states
            st.session_state.follow_up_prompt = False
            st.session_state.button_pressed = None

            # Set flag back to False once the reset is done
            st.session_state.new_report_uploaded = (
                False  # Reset flag to avoid continuous resetting
            )

        if st.session_state.tab2_loading:
            with st.spinner("Tab 2 is loading, please wait..."):
                time.sleep(2)  # Simulate loading duration
            disable_tab2_spinner()  # Disable spinner after loading
        # Ensure the session state tracks PDF upload status
        if "pdf_uploaded" not in st.session_state:
            st.session_state.pdf_uploaded = False  # Defaults to False until PDF is uploaded
        if "summary_generated" not in st.session_state:
            st.session_state.summary_generated = (
                False  # Tracks if the summary has been generated
            )

        if not st.session_state.summary_generated:
            st.warning("Please upload the Medical Report(PDF) to continue.")
            st.stop()
        else:
            st.chat_message("assistant").markdown(
                f"<div style='padding: 10px; border-radius: 10px;background-color: #f0f0f0;'>Thank you for uploading {st.session_state.file_base_name}. Hello there! I am your trusted medical assistant. Are you a curious patient, a knowledgeable medical practitioner? Let me know, and I will tailor my assistance just for you.</div>",
                unsafe_allow_html=True,
            )

            # Reload the page to reflect the new state and reset the chat
            if "selected_role" in st.session_state:
                del st.session_state["selected_role"]
            if "selected_role" not in st.session_state:
                st.session_state.selected_role = None
            if "condition" not in st.session_state:
                st.session_state.condition = None  # Set a default condition
            if "chat_history" not in st.session_state:
                st.session_state.chat_history = []
            if "chat_history_doctor" not in st.session_state:
                st.session_state.chat_history_doctor = []
            if "chat_history_medical" not in st.session_state:
                st.session_state.chat_history_medical = []
            if "chat_history_patient" not in st.session_state:
                st.session_state.chat_history_patient = []
            if "chat_history_condition" not in st.session_state:
                st.session_state.chat_history_condition = []
            if "chat_history_condition_chat" not in st.session_state:
                st.session_state.chat_history_condition_chat = []
            if "chat_history_condition_last" not in st.session_state:
                st.session_state.chat_history_condition_last = []
            if "patient_messages_added" not in st.session_state:
                st.session_state.patient_messages_added = True
            if "show_role_buttons" not in st.session_state:
                st.session_state.show_role_buttons = False
            if "selected_doctor" not in st.session_state:
                st.session_state["selected_doctor"] = False
            if "selected_patient" not in st.session_state:
                st.session_state["selected_patient"] = False

            if st.session_state.show_role_buttons or st.session_state.summary_generated:
                col1, col2 = st.columns([1, 3])
                with col1:
                    if st.button(
                        "Medical practitioner",
                        key="doctor_button",
                        disabled=st.session_state.get("selected_patient", False),
                    ):
                        st.session_state.show_specialty_buttons = True
                        st.session_state.selected_doctor = True
                        st.rerun()

                with col2:
                    if st.button(
                        "Patient",
                        key="patient_button",
                        disabled=st.session_state.get("selected_doctor", False),
                    ):
                        st.session_state.selected_patient = True
                        st.rerun()
            if st.session_state.selected_doctor:
                if not st.session_state.doctor_messages_added:
                    current_time = datetime.now().strftime("%I:%M:%S %p")
                    st.session_state.chat_history_doctor.append(
                        {
                            "role": "user",
                            "message": "You selected Medical Practitioner",
                            "time": current_time,
                        }
                    )
                    st.session_state.chat_history_doctor.append(
                        {
                            "role": "system",
                            "message": "Feel free to ask questions such as:\n\n",
                            "time": current_time,
                        }
                    )
                    st.session_state.doctor_messages_added = True
                display_values()
                for message in st.session_state.chat_history_medical:
                    if message["role"] == "user":
                        st.chat_message("user").markdown(
                            f"{message['time']}\n\n<div style='padding: 10px; border-radius: 10px;'>{message['message']}</div>",
                            unsafe_allow_html=True,
                        )
                    elif message["role"] == "system":
                        if not message.get("displayed", False):
                            # Use a placeholder to simulate a spinner with an image and text
                            placeholder = st.empty()  # Create a placeholder for the spinner

                            # Start the spinner
                            with st.spinner(""):
                                # Display the spinner with image and text in the placeholder
                                placeholder.markdown(
                                    f"""
                                    <div style="display: flex; align-items: center;">
                                        <div class="spinner-border" role="status" style="margin-right: 8px;"></div>
                                        <img src="data:image/jpeg;base64,{image_base64}" alt="stetoscope" style="height: 24px; margin-right: 8px;"/>
                                        <span>Processing...</span>
                                    </div>
                                    """,
                                    unsafe_allow_html=True
                                )
                                # Simulate a delay or your processing logic
                                time.sleep(3)

                            # Clear the placeholder once processing is complete
                            placeholder.empty()

                            container = st.chat_message("assistant").empty()
                            typewriter_effect(
                                container, f"{message['time']}\n\n{message['message']}"
                            )
                            message["displayed"] = True
                        else:
                            st.chat_message("assistant").markdown(
                                f"{message['time']}\n\n<div style='padding: 10px;background-color: #f0f0f0; border-radius: 10px;'>{message['message']}</div>",
                                unsafe_allow_html=True,
                            )

                if (
                    not st.session_state.button_pressed
                    and not st.session_state.follow_up_prompt
                ):
                    cols = st.columns(3)
                    for i, prompt in enumerate(example_prompts):
                        with cols[i % 3]:
                            if st.button(prompt, key=f"prompt_{i}"):
                                st.session_state.button_pressed = prompt
                                st.rerun()
                elif st.session_state.button_pressed:
                    current_time = datetime.now().strftime("%I:%M:%S %p")
                    user_message = st.session_state.button_pressed
                    st.session_state.chat_history_medical.append(
                        {"role": "user", "message": user_message, "time": current_time}
                    )

                    # Generate assistant response
                    if user_message == example_prompts[0]:
                        assistant_message = (
                            "The significance of both lobe involvement and seminal vesicle involvement (T3b) in prostate cancer staging is that it indicates a more advanced stage of the disease. "
                            "This is because the cancer has spread beyond the prostate gland to the seminal vesicles, which are located near the prostate, and has also involved both lobes of the prostate. "
                            "This is considered a more aggressive form of cancer and requires more aggressive treatment. The presence of both lobe involvement and seminal vesicle involvement is associated with a higher risk of cancer recurrence and metastasis. "
                            "Therefore, patients with T3b prostate cancer typically require more intensive treatment, such as radiation therapy, chemotherapy, or hormone therapy, and may also require more frequent follow-up and monitoring."
                        )
                    elif user_message == example_prompts[1]:
                        assistant_message = (
                            "Definition: In cancer surgery, the excision margin refers to the edge of the tissue removed during surgery. A positive margin means that cancer cells are present at or near the edge of the removed tissue, indicating that the surgeon may not have removed all of the cancerous tissue. "
                            "Implication: A positive margin suggests that some cancer might still remain in the body, which increases the risk of recurrence (cancer returning after surgery). After surgery, this can lead to the need for additional treatments such as radiation or hormone therapy."
                        )
                    elif user_message == example_prompts[2]:
                        assistant_message = (
                            "Adenocarcinoma of the prostate with a Gleason score of 9 is considered high-risk, as it reflects a high degree of tumor aggressiveness. Gleason scores of 9 (comprising 4+5 or 5+4 patterns) are associated with a significant risk of disease progression, distant metastasis, and mortality. "
                            "Research highlights that men diagnosed with Gleason 9 tumors often face a poor prognosis, especially if untreated or inadequately managed. The 5-year prostate cancer-specific mortality (PCSM) for Gleason 9 cancers can range from 30% to 56%, with the likelihood of death from prostate cancer increasing over time."
                        )
                    else:
                        assistant_message = (
                            "Sorry, I do not have an answer for that specific question."
                        )

                    st.session_state.chat_history_medical.append(
                        {
                            "role": "system",
                            "message": assistant_message,
                            "time": current_time,
                            "displayed": False,
                        }
                    )
                    st.session_state.button_pressed = None
                    st.session_state.follow_up_prompt = True
                    st.rerun()
                elif st.session_state.follow_up_prompt:
                    initial_prompt = st.empty()
                    initial_prompt.markdown(
                        '<div style="text-align: left; color: black; padding: 5px 0;">Do you have any other questions, I can assist you with?</div>',
                        unsafe_allow_html=True,
                    )
                    col1, col2 = st.columns([1, 10])
                    if col1.button(
                        "Yes", disabled=st.session_state.get("yes_selected", False)
                    ):
                        current_time = datetime.now().strftime("%I:%M:%S %p")
                        st.session_state.chat_history_medical.append(
                            {
                                "role": "user",
                                "message": " You selected Yes",
                                "time": current_time,
                            }
                        )
                        st.session_state.chat_history_medical.append(
                            {
                                "role": "system",
                                "message": "Please select the options:",
                                "time": current_time,
                            }
                        )
                        st.session_state.follow_up_prompt = False
                        st.rerun()
                    if col2.button("No"):
                        current_time = datetime.now().strftime("%I:%M:%S %p")
                        st.session_state.chat_history_condition_last.append(
                            {
                                "role": "user",
                                "message": "You selected No",
                                "time": current_time,
                            }
                        )
                        st.session_state.chat_history_condition_last.append(
                            {
                                "role": "system",
                                "message": "Please prioritize your health! Early treatment can lead to swift recovery. "
                                "Make an appointment with a doctor soon. You've got this, stay strong! :) Take care!! See you around.",
                                "time": current_time,
                            }
                        )
                        st.session_state.yes_selected = True
                        st.rerun()
                    display_chat_history(st.session_state.chat_history_condition_last)

            elif st.session_state.selected_patient:
                if not st.session_state.patient_messages_added:
                    current_time = datetime.now().strftime("%I:%M:%S %p")
                    st.session_state.chat_history_patient.append(
                        {"role": "user", "message": "You selected Patient", "time": current_time}
                    )
                    st.session_state.condition_shown = True
                    st.session_state.patient_messages_added = True
                display_patient()

            if st.session_state.condition_shown and st.session_state.condition:
                if not st.session_state.condition_messages_added:
                    if st.session_state.condition == "Breast cancer":
                        current_time = datetime.now().strftime("%I:%M:%S %p")
                        st.session_state.chat_history_condition.append(
                            {
                                "role": "system",
                                "message": "Breast cancer treatment often includes surgery, chemotherapy, radiation therapy, and hormone therapy. Regular follow-ups are crucial.",
                                "time": current_time,
                            }
                        )
                        st.session_state.breast_cancer = True
                    elif st.session_state.condition == "Kidney stone":
                        current_time = datetime.now().strftime("%I:%M:%S %p")

                        st.session_state.chat_history_condition.append(
                            {
                                "role": "system",
                                "message": "Kidney stones can be treated with hydration, pain relief, or surgical removal if they are large. Preventive measures include dietary adjustments.",
                                "time": current_time,
                            }
                        )
                        st.session_state.kidney_stone = True
                    elif st.session_state.condition == "Prostate cancer":
                        current_time = datetime.now().strftime("%I:%M:%S %p")
                        st.session_state.chat_history_condition.append(
                            {
                                "role": "system",
                                "message": "Prostate cancer treatments include active surveillance, surgery, radiation, and hormone therapy. Discuss options with a specialist.",
                                "time": current_time,
                            }
                        )
                        st.session_state.prostate_cancer = True
                st.session_state.condition_messages_added = True
                display_condition()

            if st.session_state.breast_cancer:
                for message in st.session_state.chat_history_condition_chat:
                    if message["role"] == "user":
                        st.chat_message("user").markdown(
                            f"{message['time']}\n\n<div style='padding: 10px; border-radius: 10px;'>{message['message']}</div>",
                            unsafe_allow_html=True,
                        )
                    elif message["role"] == "system":
                        if message["message"] == "Please select the options:":
                            with st.chat_message("assistant"):
                                st.markdown(
                                    f"<div style='padding: 10px; border-radius: 10px; background-color: #f0f0f0; display: flex; align-items: center;'>"
                                    f"<div style='flex-grow: 1;'>"
                                    f"<p style='margin: 0; font-size: 16px; color: block;'>{message['time']}</p>"
                                    f"<p style='margin: 0;'>{message['message']}</p>"
                                    f"</div>"
                                    f"</div>",
                                    unsafe_allow_html=True,
                                )
                        else:
                            if not message.get("displayed", False):
                                # Use a placeholder to simulate a spinner with an image and text
                                placeholder = st.empty()  # Create a placeholder for the spinner

                                # Start the spinner
                                with st.spinner(""):
                                    # Display the spinner with image and text in the placeholder
                                    placeholder.markdown(
                                        f"""
                                        <div style="display: flex; align-items: center;">
                                            <div class="spinner-border" role="status" style="margin-right: 8px;"></div>
                                            <img src="data:image/jpeg;base64,{image_base64}" alt="stetoscope" style="height: 24px; margin-right: 8px;"/>
                                            <span>Processing...</span>
                                        </div>
                                        """,
                                        unsafe_allow_html=True
                                    )
                                    # Simulate a delay or your processing logic
                                    time.sleep(3)

                                # Clear the placeholder once processing is complete
                                placeholder.empty()

                                container = st.chat_message("assistant").empty()
                                typewriter_effect(
                                    container, f"{message['time']}\n\n{message['message']}"
                                )
                                message["displayed"] = True
                            else:
                                with st.chat_message("assistant"):
                                    st.markdown(
                                        f"<div style='padding: 10px; border-radius: 10px; background-color: #f0f0f0; display: flex; align-items: center;'>"
                                        f"<div style='flex-grow: 1;'>"
                                        f"<p style='margin: 0; font-size: 16px; color: block;'>{message['time']}</p>"
                                        f"<p style='margin: 0;'>{message['message']}</p>"
                                        f"</div>"
                                        f"</div>",
                                        unsafe_allow_html=True,
                                    )

                if (
                    not st.session_state.button_pressed
                    and not st.session_state.follow_up_prompt
                ):
                    cols = st.columns(len(breast_cancer))
                    for i, prompt in enumerate(breast_cancer):
                        with cols[i % 3]:
                            if st.button(prompt, key=f"prompt_{i}"):
                                st.session_state.button_pressed = prompt
                                st.rerun()
                elif st.session_state.button_pressed:
                    current_time = datetime.now().strftime("%I:%M:%S %p")
                    user_message = st.session_state.button_pressed
                    st.session_state.chat_history_condition_chat.append(
                        {"role": "user", "message": user_message, "time": current_time}
                    )
                    if user_message == breast_cancer[0]:
                        assistant_message = (
                            "The symptoms for breast cancer typically include:\n\n"
                            "1. Lump in the Breast or Underarm (Axilla)\n"
                            "2. Changes in Breast Shape or Size\n"
                            "3. Skin Changes on the Breast\n"
                            "4. Nipple Changes\n"
                            "5. Persistent Pain in the Breast or Nipple\n"
                            "6. Visible Veins on the Breast\n"
                            "Please consult a doctor for a detailed plan tailored to your condition."
                        )

                    elif user_message == breast_cancer[1]:
                        assistant_message = (
                            "The diagnosis for breast cancer typically includes:\n\n"
                            "1. Physical Examination\n"
                            "2. Imaging Tests\n"
                            "3. Biopsy\n"
                            "4. Lab Tests on Biopsy Sample\n"
                            "5. Blood Tests\n"
                            "6. Staging Tests\n"
                            "Please consult a doctor for a detailed plan tailored to your condition."
                        )
                    elif user_message == breast_cancer[2]:
                        assistant_message = (
                            "The treatment options for breast cancer typically include:\n\n"
                            "1. Surgery\n"
                            "2. Chemotherapy\n"
                            "3. Radiation therapy\n"
                            "4. Hormone therapy\n"
                            "5. Targeted therapy\n"
                            "6. Immunotherapy\n"
                            "Please consult a doctor for a detailed plan tailored to your condition."
                        )
                    else:
                        assistant_message = (
                            "Sorry, I do not have an answer for that specific question."
                        )
                    st.session_state.chat_history_condition_chat.append(
                        {
                            "role": "system",
                            "message": assistant_message,
                            "time": current_time,
                            "displayed": False,
                        }
                    )
                    st.session_state.button_pressed = None
                    st.session_state.follow_up_prompt = True
                    st.rerun()
                elif st.session_state.follow_up_prompt:
                    initial_prompt = st.empty()
                    initial_prompt.markdown(
                        '<div style="text-align: left; color: black; padding: 5px 0;">Do you have any other questions, I can assist you with?</div>',
                        unsafe_allow_html=True,
                    )
                    col1, col2 = st.columns([1, 10])
                    if col1.button(
                        "Yes", disabled=st.session_state.get("yes_selected", False)
                    ):
                        st.session_state.chat_history_condition_chat.append(
                            {
                                "role": "user",
                                "message": "You selected Yes",
                                "time": current_time,
                            }
                        )
                        st.session_state.chat_history_condition_chat.append(
                            {
                                "role": "system",
                                "message": "Please select the options:",
                                "time": current_time,
                            }
                        )
                        st.session_state.follow_up_prompt = False
                        st.rerun()
                    if col2.button("No"):
                        st.session_state.chat_history_condition_last.append(
                            {
                                "role": "user",
                                "message": "You selected No",
                                "time": current_time,
                            }
                        )
                        st.session_state.chat_history_condition_last.append(
                            {
                                "role": "system",
                                "message": "Please prioritize your health! Early treatment can lead to swift recovery. Make an appointment with a doctor soon. You've got this, stay strong!:) Take care!! See you around.",
                                "time": current_time,
                            }
                        )
                        st.session_state.yes_selected = True
                        st.rerun()
                    display_chat_history(st.session_state.chat_history_condition_last)

            if st.session_state.kidney_stone:
                for message in st.session_state.chat_history_condition_chat:
                    if message["role"] == "user":
                        st.chat_message("user").markdown(
                            f"{message['time']}\n\n<div style='padding: 10px; border-radius: 10px;'>{message['message']}</div>",
                            unsafe_allow_html=True,
                        )
                    elif message["role"] == "system":
                        if message["message"] == "Please select the options:":
                            with st.chat_message("assistant"):
                                st.markdown(
                                    f"<div style='padding: 10px; border-radius: 10px; background-color: #f0f0f0; display: flex; align-items: center;'>"
                                    f"<div style='flex-grow: 1;'>"
                                    f"<p style='margin: 0; font-size: 16px; color: block;'>{message['time']}</p>"
                                    f"<p style='margin: 0;'>{message['message']}</p>"
                                    f"</div>"
                                    f"</div>",
                                    unsafe_allow_html=True,
                                )
                        else:
                            if not message.get("displayed", False):
                                # Use a placeholder to simulate a spinner with an image and text
                                placeholder = st.empty()  # Create a placeholder for the spinner

                                # Start the spinner
                                with st.spinner(""):
                                    # Display the spinner with image and text in the placeholder
                                    placeholder.markdown(
                                        f"""
                                        <div style="display: flex; align-items: center;">
                                            <div class="spinner-border" role="status" style="margin-right: 8px;"></div>
                                            <img src="data:image/jpeg;base64,{image_base64}" alt="stetoscope" style="height: 24px; margin-right: 8px;"/>
                                            <span>Processing...</span>
                                        </div>
                                        """,
                                        unsafe_allow_html=True
                                    )
                                    # Simulate a delay or your processing logic
                                    time.sleep(3)

                                # Clear the placeholder once processing is complete
                                placeholder.empty()

                                container = st.chat_message("assistant").empty()
                                typewriter_effect(
                                    container, f"{message['time']}\n\n{message['message']}"
                                )
                                message["displayed"] = True
                            else:
                                with st.chat_message("assistant"):
                                    st.markdown(
                                        f"<div style='padding: 10px; border-radius: 10px; background-color: #f0f0f0; display: flex; align-items: center;'>"
                                        f"<div style='flex-grow: 1;'>"
                                        f"<p style='margin: 0; font-size: 16px; color: block;'>{message['time']}</p>"
                                        f"<p style='margin: 0;'>{message['message']}</p>"
                                        f"</div>"
                                        f"</div>",
                                        unsafe_allow_html=True,
                                    )

                if (
                    not st.session_state.button_pressed
                    and not st.session_state.follow_up_prompt
                ):
                    cols = st.columns(len(kidney_stone))
                    for i, prompt in enumerate(kidney_stone):
                        with cols[i % 3]:
                            if st.button(prompt, key=f"prompt_{i}"):
                                st.session_state.button_pressed = prompt
                                st.rerun()
                elif st.session_state.button_pressed:
                    current_time = datetime.now().strftime("%I:%M:%S %p")
                    user_message = st.session_state.button_pressed
                    st.session_state.chat_history_condition_chat.append(
                        {"role": "user", "message": user_message, "time": current_time}
                    )
                    if user_message == kidney_stone[0]:
                        assistant_message = (
                            "The symptoms of kidney stones typically include:\n\n"
                            "1. Severe pain in the back or side\n"
                            "2. Pain during urination\n"
                            "3. Blood in the urine\n"
                            "4. Nausea or vomiting\n"
                            "5. Frequent urination or urgency to urinate\n"
                            "6. Fever and chills (if an infection is present)\n"
                            "Please consult a doctor for a detailed diagnosis and treatment plan."
                        )

                    elif user_message == kidney_stone[1]:
                        assistant_message = (
                            "Prevention of kidney stones often involves:\n\n"
                            "1. Staying hydrated by drinking plenty of water\n"
                            "2. Reducing salt intake\n"
                            "3. Avoiding foods high in oxalates (e.g., spinach, nuts)\n"
                            "4. Eating calcium-rich foods\n"
                            "5. Avoiding excessive protein intake\n"
                            "6. Maintaining a healthy weight\n"
                            "Please consult a doctor for personalized advice."
                        )
                    elif user_message == kidney_stone[2]:
                        assistant_message = (
                            "Treatment options for large kidney stones typically include:\n\n"
                            "1. Shock wave lithotripsy (breaking up stones)\n"
                            "2. Ureteroscopy (removal of stones)\n"
                            "3. Surgery for large or complicated stones\n"
                            "Please consult a doctor for a treatment plan tailored to your condition."
                        )
                    else:
                        assistant_message = (
                            "Sorry, I do not have an answer for that specific question."
                        )
                    st.session_state.chat_history_condition_chat.append(
                        {
                            "role": "system",
                            "message": assistant_message,
                            "time": current_time,
                            "displayed": False,
                        }
                    )
                    st.session_state.button_pressed = None
                    st.session_state.follow_up_prompt = True
                    st.rerun()
                elif st.session_state.follow_up_prompt:
                    initial_prompt = st.empty()
                    initial_prompt.markdown(
                        '<div style="text-align: left; color: black; padding: 5px 0;">Do you have any other questions, I can assist you with?</div>',
                        unsafe_allow_html=True,
                    )
                    col1, col2 = st.columns([1, 10])
                    if col1.button(
                        "Yes", disabled=st.session_state.get("yes_selected", False)
                    ):
                        current_time = datetime.now().strftime("%I:%M:%S %p")
                        st.session_state.chat_history_condition_chat.append(
                            {
                                "role": "user",
                                "message": "You selected Yes",
                                "time": current_time,
                            }
                        )
                        st.session_state.chat_history_condition_chat.append(
                            {
                                "role": "system",
                                "message": "Please select the options:",
                                "time": current_time,
                            }
                        )
                        st.session_state.follow_up_prompt = False
                        st.rerun()
                    if col2.button("No"):
                        current_time = datetime.now().strftime("%I:%M:%S %p")
                        st.session_state.chat_history_condition_last.append(
                            {
                                "role": "user",
                                "message": " You selected No",
                                "time": current_time,
                            }
                        )
                        st.session_state.chat_history_condition_last.append(
                            {
                                "role": "system",
                                "message": "Please prioritize your health! Early treatment can lead to swift recovery. Make an appointment with a doctor soon. You've got this, stay strong!:) Take care!! See you around.",
                                "time": current_time,
                            }
                        )
                        st.session_state.yes_selected = True
                        st.rerun()
                    display_chat_history(st.session_state.chat_history_condition_last)

            if st.session_state.prostate_cancer:
                for message in st.session_state.chat_history_condition_chat:
                    if message["role"] == "user":
                        st.chat_message("user").markdown(
                            f"{message['time']}\n\n<div style='padding: 10px; border-radius: 10px;'>{message['message']}</div>",
                            unsafe_allow_html=True,
                        )
                    elif message["role"] == "system":
                        if message["message"] == "Please select the options:":
                            with st.chat_message("assistant"):
                                st.markdown(
                                    f"<div style='padding: 10px; border-radius: 10px; background-color: #f0f0f0; display: flex; align-items: center;'>"
                                    f"<div style='flex-grow: 1;'>"
                                    f"<p style='margin: 0; font-size: 16px; color: block;'>{message['time']}</p>"
                                    f"<p style='margin: 0;'>{message['message']}</p>"
                                    f"</div>"
                                    f"</div>",
                                    unsafe_allow_html=True,
                                )
                        else:
                            if not message.get("displayed", False):
                                # Use a placeholder to simulate a spinner with an image and text
                                placeholder = st.empty()  # Create a placeholder for the spinner

                                # Start the spinner
                                with st.spinner(""):
                                    # Display the spinner with image and text in the placeholder
                                    placeholder.markdown(
                                        f"""
                                        <div style="display: flex; align-items: center;">
                                            <div class="spinner-border" role="status" style="margin-right: 8px;"></div>
                                            <img src="data:image/jpeg;base64,{image_base64}" alt="stetoscope" style="height: 24px; margin-right: 8px;"/>
                                            <span>Processing...</span>
                                        </div>
                                        """,
                                        unsafe_allow_html=True
                                    )
                                    # Simulate a delay or your processing logic
                                    time.sleep(3)

                                # Clear the placeholder once processing is complete
                                placeholder.empty()

                                container = st.chat_message("assistant").empty()
                                typewriter_effect(
                                    container, f"{message['time']}\n\n{message['message']}"
                                )
                                message["displayed"] = True
                            else:
                                with st.chat_message("assistant"):
                                    st.markdown(
                                        f"<div style='padding: 10px; border-radius: 10px; background-color: #f0f0f0; display: flex; align-items: center;'>"
                                        f"<div style='flex-grow: 1;'>"
                                        f"<p style='margin: 0; font-size: 16px; color: block;'>{message['time']}</p>"
                                        f"<p style='margin: 0;'>{message['message']}</p>"
                                        f"</div>"
                                        f"</div>",
                                        unsafe_allow_html=True,
                                    )

                if (
                    not st.session_state.button_pressed
                    and not st.session_state.follow_up_prompt
                ):
                    cols = st.columns(len(prostate_cancer))
                    for i, prompt in enumerate(prostate_cancer):
                        with cols[i % 3]:
                            if st.button(prompt, key=f"prompt_{i}"):
                                st.session_state.button_pressed = prompt
                                st.rerun()
                elif st.session_state.button_pressed:
                    current_time = datetime.now().strftime("%I:%M:%S %p")
                    user_message = st.session_state.button_pressed
                    st.session_state.chat_history_condition_chat.append(
                        {"role": "user", "message": user_message, "time": current_time}
                    )
                    if user_message == prostate_cancer[0]:
                        assistant_message = (
                            "The risk factors for prostate cancer include:\n\n"
                            "1. Age (common in men over 50)\n"
                            "2. Family history of prostate cancer\n"
                            "3. Genetic mutations (e.g., BRCA1 or BRCA2 genes)\n"
                            "4. Diet high in processed or red meat\n"
                            "5. Obesity and lack of physical activity\n"
                            "6. Ethnicity (higher risk in African-American men)\n"
                            "Please discuss with a doctor to evaluate your risk."
                        )

                    elif user_message == prostate_cancer[1]:
                        assistant_message = (
                            "Early detection of prostate cancer typically involves:\n\n"
                            "1. Prostate-specific antigen (PSA) blood test\n"
                            "2. Digital rectal exam (DRE)\n"
                            "3. Biopsy if abnormalities are detected\n"
                            "4. Imaging tests (e.g., MRI or CT scans)\n"
                            "5. Genetic testing for high-risk individuals\n"
                            "6. Regular screening for those with higher risk factors\n"
                            "Please consult a doctor for appropriate screening."
                        )
                    elif user_message == prostate_cancer[2]:
                        assistant_message = (
                            "Common side effects of prostate cancer treatments include:\n\n"
                            "1. Urinary incontinence\n"
                            "2. Erectile dysfunction\n"
                            "3. Bowel dysfunction (e.g., diarrhea or rectal pain)\n"
                            "4. Fatigue from radiation or hormone therapy\n"
                            "5. Hot flashes and bone thinning (from hormone therapy)\n"
                            "6. Emotional distress or depression\n"
                            "Please consult a specialist to manage these side effects effectively."
                        )
                    else:
                        assistant_message = (
                            "Sorry, I do not have an answer for that specific question."
                        )
                    st.session_state.chat_history_condition_chat.append(
                        {
                            "role": "system",
                            "message": assistant_message,
                            "time": current_time,
                            "displayed": False,
                        }
                    )
                    st.session_state.button_pressed = None
                    st.session_state.follow_up_prompt = True
                    st.rerun()
                elif st.session_state.follow_up_prompt:
                    initial_prompt = st.empty()
                    initial_prompt.markdown(
                        '<div style="text-align: left; color: black; padding: 5px 0;">Do you have any other questions, I can assist you with?</div>',
                        unsafe_allow_html=True,
                    )
                    col1, col2 = st.columns([1, 10])
                    if col1.button(
                        "Yes", disabled=st.session_state.get("yes_selected", False)
                    ):
                        st.session_state.chat_history_condition_chat.append(
                            {
                                "role": "user",
                                "message": "You selected Yes",
                                "time": current_time,
                            }
                        )
                        st.session_state.chat_history_condition_chat.append(
                            {
                                "role": "system",
                                "message": "Please select the options:",
                                "time": current_time,
                            }
                        )
                        st.session_state.follow_up_prompt = False
                        st.rerun()
                    if col2.button("No"):
                        st.session_state.chat_history_condition_last.append(
                            {
                                "role": "user",
                                "message": "You selected No",
                                "time": current_time,
                            }
                        )
                        st.session_state.chat_history_condition_last.append(
                            {
                                "role": "system",
                                "message": "Please prioritize your health! Early treatment can lead to swift recovery. Make an appointment with a doctor soon. You've got this, stay strong!:) Take care!! See you around.",
                                "time": current_time,
                            }
                        )
                        st.session_state.yes_selected = True
                        st.rerun()
                    display_chat_history(st.session_state.chat_history_condition_last)

    # Declare a chat input globally
    chat_input = st.chat_input("Type your message here...", key="chat_input")


