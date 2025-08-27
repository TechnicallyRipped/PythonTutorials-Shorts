

# pip install openai-whisper

import whisper

#All models: tiny, base, small, medium, large
model = whisper.load_model("base")

result = model.transcribe("example_audio.mp3")
print(result)

txt = result['text']

with open('audio_to_text.txt','w') as file:
    file.write(txt)














