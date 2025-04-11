import sys
from google.oauth2 import service_account
from AudioToText import AudioToText
from TextToAudio import TextToAudio
from Translation import Translator

def main():
    """
    1) Prompts for language codes.
    2) Streams mic audio to STT in near real time.
    3) Buffers unprocessed words until two are available, then translates and speaks them as a pair.
    4) If a final result is received with leftover words, processes them immediately.
    """
    # Path to your JSON credentials file
    CREDENTIALS_PATH = r"C:\Programming\CSC450Project\shatranz-52a90ba84f11.json"
    credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_PATH)

    # Prompt user for the source and target languages
    language_code = input("Enter language code (e.g., en-US): ").strip()
    target_language = input("Enter target translation language (e.g., fr): ").strip()

    # Initialize AudioToText (STT), Translator, and TextToAudio (TTS)
    stt = AudioToText(credentials, language_code)
    translator = Translator(credentials)
    tts = TextToAudio(credentials)

    print("Listening... Speak now.")

    # This list stores the words already processed
    recognized_words = []
    responses = stt.get_responses()

    try:
        for response in responses:
            for result in response.results:
                transcript = result.alternatives[0].transcript.strip()
                current_words = transcript.split()

                # Compute the new words that haven't been processed yet
                new_words = current_words[len(recognized_words):]

                # Only process if we have at least two new words
                if len(new_words) >= 2:
                    # If the number of new words is odd, process the even part and keep the leftover word
                    if len(new_words) % 2 == 0:
                        process_count = len(new_words)
                    else:
                        process_count = len(new_words) - 1

                    # Process new words in pairs
                    for i in range(0, process_count, 2):
                        pair = " ".join(new_words[i:i+2])
                        print("Processing pair:", pair)
                        translated_pair = translator.translate_text(pair, target_language)
                        tts.speak_word(translated_pair)
                        print("Translated:", translated_pair)

                    # Update recognized_words with only the words that have been processed
                    recognized_words.extend(new_words[:process_count])

                # When a final result is received, process any leftover words immediately.
                if result.is_final:
                    remaining_words = current_words[len(recognized_words):]
                    if remaining_words:
                        leftover_phrase = " ".join(remaining_words)
                        print("Processing final remaining:", leftover_phrase)
                        translated_phrase = translator.translate_text(leftover_phrase, target_language)
                        tts.speak_word(translated_phrase)
                        print("Translated final:", translated_phrase)
                    # Reset the buffer for the next phrase
                    recognized_words = []
                    print()  # New line for clarity

    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()
