# How to Create a Custom Chatbot Using Google AI Studio and Streamlit
Reference backend [youtube video part1](https://www.youtube.com/watch?v=SxUDPM0mGDY&t=2s).<br>
 frontend [youtube video part2](https://www.youtube.com/watch?v=j4Avy7UzPGw).



This guide will walk you through creating a chatbot using **Google AI Studio's Gemini API** and integrating it with **Streamlit** for a user-friendly interface.

---

## Step 1: Generate Your Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/tune).
2. Click on **Get API Key** to generate your **Gemini API Key**.
3. Grant access to Google Drive when prompted.

---

## Step 2: Create a Tuned Model

1. In the left panel, click **New Tuned Model**.
2. Navigate to [Create a Structured Prompt](https://aistudio.google.com/prompts/new_data).
3. Fill in the fields:
   - **Input Prompt**: Specify your chatbot's purpose. For example:
     ```
     You are a professional fitness coach chatbot. Act accordingly.
     ```
   - **Output Prompt**: Test your chatbot with a question like:
     ```
     Who are you?
     ```
     The chatbot should respond with:  
     ```
     I am a professional fitness coach chatbot.
     ```
4. Click on the `<> Code` button at the top and copy the generated code.

---

## Step 3: Build the Backend

1. Paste the copied code into a file named `backend.py` or `main.py`
2. Modify the code as follows:
   - Replace the `os.env` API key line with your actual API key:
     ```python
     genai.configure(api_key="Your_API_Key_Here")
     ```
   - Refactor the response generation into a function:
     ```python
     def GenerateResponse(input_text):
         response = model.generate_content([
             "you are a fitness bot",
             f"input: {input_text}",
             "output: ",
         ])
         return response.text
     ```
3. Test the function with a simple loop:
   ```python
   while True:
       string = str(input("Enter your Prompt: "))
       print(GenerateResponse(string))
<mark>Once verified, comment out the test loop.</mark
## Step 4: Create a User Interface with Streamlit
Visit Streamlit and sign in.
<mark>>Navigate to Docs > Tutorials > Work with LLMs or directly visit Build a Basic LLM Chat App.</mark
Choose a simple UI template, such as Simple Chat, and copy the full code.
Paste the code into a file named frontend.py.

##Step 5: Connect the Backend and Modify the UI
<mark>Import the backend into your frontend.py:</mark>

<mark>import backend</mark>
## Update the response generator function:

def response_generator(prompt):
    response = backend.GenerateResponse(prompt)
    return response
## Update the assistant message container:

# Display assistant response in chat message container
with st.chat_message("assistant"):<br>
    response = st.write_stream(response_generator(<mark>prompt)</mark>)
    
Step 6: Set Up the Environment
## Create a virtual environment: 
<mark>python -m venv env</mark>

## Install dependencies:

pip install google-generativeai<br>
pip install streamlit

## Step 7: Run the Application
## Run the Streamlit app using:

streamlit run frontend.py

## If your file is in a subdirectory, navigate to it and run:
<mark>
cd src<br>
streamlit run main.py </mark>

---

Congratulations! Your chatbot is now ready to use. You can interact with it via the Streamlit interface.
