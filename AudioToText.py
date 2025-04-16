import pyaudio
from google.cloud import speech
from google.oauth2 import service_account

class AudioToText:
    def __init__(
        self,
        credentials,
        language_code,
        frames_per_buffer=1024,
        rate=16000,
        channels=1
    ):
        """
        Manages streaming microphone audio to Google Speech-to-Text.
        :param credentials: Google service account Credentials object.
        :param language_code: e.g. 'en-US'
        :param frames_per_buffer: PyAudio buffer size.
        :param rate: sample rate (Hz).
        :param channels: number of input channels (1 for mono).
        """
        self.credentials = credentials
        self.language_code = language_code
        self.frames_per_buffer = frames_per_buffer
        self.rate = rate
        self.channels = channels

        # Initialize the Speech-to-Text client
        self.stt_client = speech.SpeechClient(credentials=self.credentials)

        # Configure PyAudio for microphone input
        self.p = pyaudio.PyAudio()
        self.input_stream = self.p.open(
            format=pyaudio.paInt16,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.frames_per_buffer
        )

        # Build recognition config
        recognition_config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=self.rate,
            language_code=self.language_code
        )

        # Enable interim results for near-real-time transcripts
        self.streaming_config = speech.StreamingRecognitionConfig(
            config=recognition_config,
            interim_results=True
        )

    def audio_generator(self):
        """
        Continuously read chunks from the mic and yield them as
        StreamingRecognizeRequest for Google STT.
        """
        while True:
            chunk = self.input_stream.read(self.frames_per_buffer)
            yield speech.StreamingRecognizeRequest(audio_content=chunk)

    def get_responses(self):
        """
        Returns a streaming generator of STT responses.
        """
        return self.stt_client.streaming_recognize(
            self.streaming_config,
            self.audio_generator()
        )
