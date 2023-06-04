# edge-speak

This is a Flask-based web service that provides text-to-speech (TTS) and text translation functionalities. It utilizes the Microsoft Edge TTS API (free to use) for synthesizing speech and the Azure Translator API (2M chars/month free) for text translation.

## Demo

https://github.com/humanova/edge-speak/assets/22047571/8ffacff1-7fb5-4749-a9bf-8a146cc69f3b

## Endpoints
<br>

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
