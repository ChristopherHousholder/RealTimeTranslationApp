import numpy as np
import sounddevice as sd
from TTS.api import TTS

class TextToAudio:
    def __init__(self, model_name="tts_models/en/vctk/vits", speaker="p225"):
        """
        Uses Coqui TTS for speaking text out loud.
        :param model_name: The TTS model to load
        :param speaker: Speaker ID (required for multi-speaker models like VITS)
        """
        self.tts = TTS(model_name=model_name)
        self.sample_rate = self.tts.synthesizer.output_sample_rate
        self.speaker = speaker

    def speak_word(self, word: str):
        """
        Converts a word/phrase into audio and plays it immediately.
        """
        waveform = self.tts.tts(word, speaker=self.speaker)
        waveform = np.array(waveform, dtype=np.float32)
        sd.play(waveform, samplerate=self.sample_rate)
        sd.wait()
