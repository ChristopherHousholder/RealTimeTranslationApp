# WhisperAudioToText.py
import pyaudio
import torch
import whisper
import queue
import threading

class WhisperAudioToText:
    def __init__(self, model_size="base", language="ko", rate=16000, frames_per_buffer=1024):
        self.model = whisper.load_model(model_size)
        self.language = language
        self.rate = rate
        self.frames_per_buffer = frames_per_buffer

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.frames_per_buffer
        )

        self.audio_queue = queue.Queue()
        self.running = True

    def _record(self):
        while self.running:
            data = self.stream.read(self.frames_per_buffer, exception_on_overflow=False)
            self.audio_queue.put(data)

    def get_transcripts(self):
        """
        Yields complete transcriptions (non-streaming).
        """
        recorder = threading.Thread(target=self._record)
        recorder.start()

        audio_buffer = bytearray()

        try:
            while True:
                chunk = self.audio_queue.get()
                audio_buffer.extend(chunk)

                if len(audio_buffer) > self.rate * 5:  # ~5 seconds
                    audio_np = torch.frombuffer(audio_buffer, dtype=torch.int16).float() / 32768.0
                    result = self.model.transcribe(audio_np, language=self.language)
                    transcript = result["text"].strip()
                    yield transcript
                    audio_buffer.clear()
        except GeneratorExit:
            self.running = False
            recorder.join()
