import os
import pyaudio
from google.cloud import speech
from TextToAudio import RealTimeTTS

language_code = input("Enter language code (e.g., en-US): ").strip()
target_language = input("Enter target translation language (e.g., fr): ").strip()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Programming\CSC450Project\shatranz-52a90ba84f11.json"
client = speech.SpeechClient()
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    input=True,
    frames_per_buffer=1024
)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code=language_code,
)
streaming_config = speech.StreamingRecognitionConfig(
    config=config,
    interim_results=True
)

def generateAudio():
    while True:
        yield stream.read(1024)

def streamAudio():
    print("Listening... Speak now.")
    tts = RealTimeTTS(rate=200)
    requests = (speech.StreamingRecognizeRequest(audio_content=content)
                for content in generateAudio())
    responses = client.streaming_recognize(streaming_config, requests)
    printed_words = []
    for response in responses:
        for result in response.results:
            current_words = result.alternatives[0].transcript.strip().split()
            if len(current_words) > len(printed_words):
                new_words = current_words[len(printed_words):]
                for word in new_words:
                    tts.speak_word(word)
                    print(f"{word}")
                printed_words = current_words
            if result.is_final:
                printed_words = []

if __name__ == "__main__":
    streamAudio()
