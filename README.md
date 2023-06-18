# whisperChatgpt
send voice message and let chatgpt answer it
This code uses OpenAI's GPT-3.5 language model and Gradio library to create an interactive audio interface with a virtual assistant. The assistant can transcribe and respond to audio inputs in real-time.
The code initializes the OpenAI API by setting the API key. It also prepares the initial message for the assistant. The decipher function is the main method that takes an audio file as input, transcribes it using OpenAI's speech to text model, and generates a response from the assistant using the ChatCompletion model.
The code sets up a Gradio audio interface, allowing users to provide audio inputs through a microphone. The decipher function is connected to the interface as the processing function, and the output is displayed as text.
To run the code, you need to have the necessary dependencies installed (Gradio, OpenAI, etc.) and provide the OpenAI API key. The audio interface can be launched, and the assistant will transcribe and respond to the user's spoken input.
