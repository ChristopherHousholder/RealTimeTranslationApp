import speech_recognition as sr
from langdetect import detect, DetectorFactory

# Set seed for consistent language detection
DetectorFactory.seed = 0

def continuous_speech_recognition():
    """
    Continuously listens to speech, transcribes it per word,
    and detects the spoken language dynamically.
    """
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening... Speak now (Press Ctrl+C to stop)")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise

        while True:
            try:
                # Listen for a small chunk of speech
                audio = recognizer.listen(source, phrase_time_limit=1)  # Capture short segments
                
                # Recognize speech
                text = recognizer.recognize_google(audio)  # Auto-detect language
                
                # Detect the language
                detected_lang = detect(text)
                
                print(f"[{detected_lang.upper()}] {text}")
            
            except sr.UnknownValueError:
                print("[...] (Listening...)")  # Indicate waiting for input
            except sr.RequestError:
                print("Could not request results. Check your internet connection.")
                break  # Exit loop on network failure

if __name__ == "__main__":
    try:
        continuous_speech_recognition()
    except KeyboardInterrupt:
        print("\nExiting... Goodbye!")

