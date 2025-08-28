

# pip install openai-whisper

import whisper

model = whisper.load_model("medium")

result = model.transcribe("spanish.mp3", 
                          language='es',
                          task="translate")

txt = result['text']
print(txt)















