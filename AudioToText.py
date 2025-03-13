import os
import pyaudio
from google.cloud import speech
from TextToAudio import BufferedTTS
import time

tts = BufferedTTS(rate=200, buffer_delay=0.1)

language_code = input("Enter language code (e.g., en-US, es-ES, fr-FR): ").strip() #Language Code

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Programming\CSC450Project\shatranz-52a90ba84f11.json" #I don't know how this will have to work for an executable yet

# |-------------------------------------------------- Google API Intialization (And Stuff) --------------------------------------------------|
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
    interim_results=True  # Enable continous input for the api
)

def generateAudio():
    while True:
        yield stream.read(1024) #yield audio chunks for input

def streamAudio():
    print("Listening... Speak now.")
    requests = (speech.StreamingRecognizeRequest(audio_content=content)
                for content in generateAudio())
    responses = client.streaming_recognize(streaming_config, requests)

    printed_words = []



# |-------------------------------------------------- Continousness --------------------------------------------------|
    # Honestly this section is pure genius (I'm so humble). This takes the interim audio (per "chunk") as its jumbled overprinted mess, 
    # puts it into a list of words already said then only prints then new ones. Yes it works for intentionally repeated words.
    #p.s. this took significantly longer than I had hoped...
    for response in responses:
        for result in response.results:
            current_words = result.alternatives[0].transcript.strip().split()
            if len(current_words) > len(printed_words):
                new_words = current_words[len(printed_words):]
                for word in new_words:
                    tts.speak_word(word)
                    print(word)
                printed_words = current_words
            if result.is_final:
                printed_words = []

if __name__ == "__main__":
    streamAudio()
