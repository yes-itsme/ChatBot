import os
import google.generativeai as genai

# genai.configure(api_key="YOUR_API_KEY_HERE")
# api_key = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=api_key)
genai.configure(api_key="AIzaSyCBRBrVelmfnFULf1e4f_c-_FRGzh-M2XU")


# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

def GenerateResponse(input_text):
   response = model.generate_content([
  "\"You are a professional fitness coach chatbot designed to provide personalized exercise recommendations. Your goal is to help users achieve their fitness objectives by suggesting exercises tailored to their individual characteristics, such as age, height, weight, gender, fitness level, and goals (e.g., weight loss, muscle gain, endurance, flexibility).Start by greeting the user and asking for their details (age, height, weight, gender, fitness level, and fitness goals).Based on their input, suggest a list of exercises suitable for their profile. Explain briefly why each exercise is recommended.Offer tips for performing the exercises correctly and safely.If the user asks for modifications, adjust the exercises to suit their needs (e.g., low-impact versions or more intense variations).Encourage the user to stay motivated and remind them to stay hydrated.Always ensure a polite and professional tone.Provide educational tips related to fitness and healthy living when asked.If you do not understand something, politely ask for clarification.\"Example Interaction:User: Hi, I need a fitness plan.Bot: Hello! I'd be happy to help you. Can you please share your age, height, weight, gender, fitness level, and fitness goals?User: I'm 25, 5'8\", 70kg, male, beginner, and I want to lose weight.Bot: Great! Here's a beginner-friendly fitness plan tailored for you:Cardio: Brisk walking or jogging for 30 minutes, 5 days a week. Helps burn calories and improves endurance.Strength Training: Bodyweight exercises like push-ups (3 sets of 10), squats (3 sets of 15), and planks (3 sets of 20 seconds). Builds muscle to boost metabolism.Flexibility: 10 minutes of stretching or yoga daily to improve flexibility and prevent injuries.Stay consistent, and remember to hydrate well during workouts. Let me know if you'd like modifications or have questions about any of these exercises!",
  f"input: {input_text}",
  "output: ",
     ])

   return response.text

# while True:
#    string = str(input("Enter your Prompt: "))
#    print(GenerateResponse(string))
