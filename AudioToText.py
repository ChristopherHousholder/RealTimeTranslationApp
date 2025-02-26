import speech_recognition as sr
from langdetect import detect, DetectorFactory

# Set seed for consistent language detection results
DetectorFactory.seed = 0

def recognize_speech():
    """
    Captures audio from the microphone, detects the spoken language, 
    and converts the speech into text automatically.
    """
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening... Speak now:")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)  # Listen for input
        
        try:
            # Recognize speech without specifying a language (Google auto-detects)
            text = recognizer.recognize_google(audio)  # Auto-detect language
            detected_lang = detect(text)  # Detect the language from the text

            print(f"Detected Language: {detected_lang.upper()}")
            print(f"Transcribed Text: {text}")
            return detected_lang, text
        
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
            return None, None
        except sr.RequestError:
            print("Could not request results. Check your internet connection.")
            return None, None

if __name__ == "__main__":
    recognize_speech()
