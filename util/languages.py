from lingua import Language, LanguageDetectorBuilder

# this list can be expanded
# restricting the set of languages is beneficial for the classification accuracy
languages = [Language.ENGLISH, Language.FRENCH, Language.GERMAN, Language.TURKISH, 
             Language.SPANISH, Language.CHINESE, Language.HINDI, Language.PORTUGUESE,
             Language.RUSSIAN, Language.KOREAN, Language.JAPANESE, Language.BENGALI]
lang_detector = LanguageDetectorBuilder.from_languages(*languages).build()


def detect_text_language(text):
  lang = lang_detector.detect_language_of(text)
  return str(lang.iso_code_639_1)[-2:].lower()