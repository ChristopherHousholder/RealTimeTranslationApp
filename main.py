import sys
from google.oauth2 import service_account
from TextToAudio import TextToAudio
from Translation import Translator

# Dynamic import based on language
language_code = input("Enter language code (e.g., en-US or ko): ").strip()
target_language = input("Enter target translation language (e.g., fr): ").strip()

if language_code.startswith("ko"):
    from WhisperAudioToText import WhisperAudioToText as AudioToText
else:
    from AudioToText import AudioToText

def main():
    """
    Real-time translator:
    - Google STT for non-Korean
    - Whisper for Korean
    - Translates and speaks full sentences/phrases
    """
    CREDENTIALS_PATH = r"C:\\Programming\\CSC450Project\\shatranz-52a90ba84f11.json"
    credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_PATH)

    translator = Translator(credentials)
    tts = TextToAudio()

    if language_code.startswith("ko"):
        stt = AudioToText(model_size="base", language="ko")
        print("Listening with Whisper (Korean)... Speak now.")
        for transcript in stt.get_transcripts():
            print("Processing:", transcript)
            translated = translator.translate_text(transcript, target_language)
            if translated.strip():
                tts.speak_word(translated)
                print(f"Translated: {transcript} → {translated}\n")
            else:
                print(f"Skipped empty translation from: {transcript!r}\n")
    else:
        stt = AudioToText(credentials, language_code)
        print("Listening with Google STT... Speak now.")
        spoken_words = set()
        responses = stt.get_responses()

        try:
            for response in responses:
                for result in response.results:
                    transcript = result.alternatives[0].transcript.strip()

                    if result.is_final:
                        print("Processing:", transcript)
                        translated = translator.translate_text(transcript, target_language)
                        if translated.strip():
                            tts.speak_word(translated)
                            print(f"Translated: {transcript} → {translated}\n")
                        else:
                            print(f"Skipped empty translation from: {transcript!r}\n")

        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)

if __name__ == "__main__":
    main()