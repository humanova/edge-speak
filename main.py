import random 
import tempfile

import edge_tts
from edge_tts import VoicesManager
from flask import Flask, request, jsonify, send_file

from util import voices, languages

app = Flask(__name__)


@app.route("/tts", methods=["POST"])
async def text_to_speech():
  data = request.get_json()
  text = data.get("text", "")
  gender = data.get("gender", "female")  # optional argument
  rate = data.get("rate", "+15%")        # optional argument
  if not text:
    return jsonify({"error": "Text field is missing or empty"}), 400

  # detect the text language
  detected_language_code = languages.detect_text_language(text)

  try:
    # find a suitable voice
    possible_voices = voices.find_suitable_voice(detected_language_code, gender)

    communicate = edge_tts.Communicate(text, random.choice(possible_voices), rate=rate)
    with tempfile.NamedTemporaryFile(suffix=".mp3") as f:
      await communicate.save(f.name)

      return send_file(f.name, as_attachment=True, download_name="output.mp3", mimetype="audio/mpeg")
  except Exception as e:
    print(e)
    print(e.with_traceback)
    return jsonify({"error": "Couldn't synthesize audio."}), 500


if __name__ == "__main__":
  app.run(debug=True)
