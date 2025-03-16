import pyaudio
from google.cloud import texttospeech

class TextToAudio:
    def __init__(self, credentials, sample_rate=16000, channels=1):
        """
        Manages calling Google Text-to-Speech for single words
        and playing them out loud (raw PCM) via PyAudio.
        :param credentials: Google service account Credentials object.
        :param sample_rate: Playback sample rate (Hz).
        :param channels: number of output channels (1 for mono).
        """
        self.tts_client = texttospeech.TextToSpeechClient(credentials=credentials)
        self.sample_rate = sample_rate
        self.channels = channels

        # Set up PyAudio for speaker/headphone output
        self.p = pyaudio.PyAudio()
        self.output_stream = self.p.open(
            format=pyaudio.paInt16,
            channels=self.channels,
            rate=self.sample_rate,
            output=True
        )

    def speak_word(self, word: str):
        """
        Calls Google TTS on a single 'word' (or short phrase),
        then plays the result out loud immediately (no file saving).
        """
        synthesis_input = texttospeech.SynthesisInput(text=word)

        voice_params = texttospeech.VoiceSelectionParams(
            language_code="en-US",   # Hard-coded TTS language for demo
            name="en-US-Wavenet-D"
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16,
            sample_rate_hertz=self.sample_rate
        )

        # Perform the TTS request
        response = self.tts_client.synthesize_speech(
            input=synthesis_input,
            voice=voice_params,
            audio_config=audio_config
        )

        # Play the raw PCM data
        raw_audio = response.audio_content
        self.output_stream.write(raw_audio)
    