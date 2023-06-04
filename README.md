# edge-speak

This is a Flask-based web service that provides text-to-speech (TTS) and text translation functionalities. It utilizes the Microsoft Edge TTS API (free to use) for synthesizing speech and the Azure Translator API (2M chars/month free) for text translation.

## Demo

https://github.com/humanova/edge-speak/blob/35200e984dbe0a9a940828d91506268cb2ee3dbe/media/esdemo.mp4
## Endpoints

### POST /tts
```
Content-Type: application/json

{
  "text": "A group of owls is called a parliament.",
  "gender": "female",
  "rate": "+15%"
}
```

Returns an MP3 audio file as a response.

<br>

### POST /translate
```
Content-Type: application/json

{
  "text": "Lot sowy jest cichy.",
  "target_language": "tr"
}
```
Returns a JSON object containing the translation result.
```
{
  "translation": {
    "detectedLanguage": {
      "language": "pl",
      "score": 1.0
    },
    "translations": [
      {
        "text": "Der Flug der Eule ist lautlos.",
        "to": "de"
      }
    ]
  }
}
```