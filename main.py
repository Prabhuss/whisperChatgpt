import gradio as gr
import openai

openai.api_key = "<your openapi key>"
messages = [
{"role": "system", "content": "You are a helpful assistant."},
]

#Main method for deciphering audio
def decipher(audio):
    global messages


    # Transcribing audio using OpenAI's speech to text model
    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    print(transcript["text"])

    messages.clear()
    messages.append({"role": "user", "content": transcript["text"]})

    print(messages)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
)

    system_message = response["choices"][0]["message"]["content"]

    messages.append({"role": "assistant", "content": system_message})

    chat_transcript = ""
    for message in messages:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ": " + message['content'] + "\n\n"

    return chat_transcript
#Using Gradio's audio interface
interface = gr.Interface(fn=decipher, inputs=gr.Audio(source="microphone", type="filepath"), outputs="text")
interface.launch()
