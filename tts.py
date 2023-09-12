from gtts import gTTS
from flask import Flask, send_file
import uuid

app = Flask(__name__)

@app.route('/text_to_speech')
def text_to_speech():
    text = input("Enter the text you want to convert to speech: ")
    lang = input("Enter the language code (like 'en' for English, 'es' for Spanish, etc.): ")
    tts = gTTS(text=text, lang=lang)
    filename = f"output_{uuid.uuid4().hex}.mp3"
    tts.save(filename)
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)



