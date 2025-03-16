import sys
from google.oauth2 import service_account
from AudioToText import AudioToText
from TextToAudio import TextToAudio

def main():
    """
    1) Prompts for language codes.
    2) Streams mic audio to STT in near real time.
    3) For each new recognized word, calls TTS immediately.
    """
    # Path to your JSON credentials file
    CREDENTIALS_PATH = r"C:\Programming\CSC450Project\shatranz-52a90ba84f11.json"
    credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_PATH)

    # Prompt user
    language_code = input("Enter language code (e.g., en-US): ").strip()
    target_language = input("Enter target translation language (e.g., fr): ").strip()
    # (Translation is not implemented in this demo.)

    # Initialize AudioToText (STT)
    stt = AudioToText(credentials, language_code)

    # Initialize TextToAudio (TTS)
    tts = TextToAudio(credentials)

    print("Listening... Speak now.")

    # Keep track of words already recognized
    recognized_words = []

    # Start streaming STT responses
    responses = stt.get_responses()

    try:
        for response in responses:
            for result in response.results:
                transcript = result.alternatives[0].transcript.strip()
                current_words = transcript.split()

                # If new words appear, speak them immediately
                if len(current_words) > len(recognized_words):
                    new_words = current_words[len(recognized_words):]
                    for word in new_words:
                        tts.speak_word(word)
                        print(word, end=" ", flush=True)
                    recognized_words = current_words

                # When a final result is received, reset for the next phrase
                if result.is_final:
                    recognized_words = []
                    print()  # New line for next phrase
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()
