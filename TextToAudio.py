import pyttsx3
import threading
import time

class BufferedTTS:
    def __init__(self, rate=200, buffer_delay=0.1):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.buffer_delay = buffer_delay
        self.words_buffer = []
        self.buffer_lock = threading.Lock()
        self.flush_timer = None

    def flush_buffer(self):
        with self.buffer_lock:
            if self.words_buffer:
                text = ' '.join(self.words_buffer)
                self.words_buffer.clear()
            else:
                text = None
        if text:
            self.engine.say(text)
            self.engine.runAndWait()
        self.flush_timer = None

    def speak_word(self, word):
        with self.buffer_lock:
            self.words_buffer.append(word)
        if self.flush_timer is not None:
            self.flush_timer.cancel()
        self.flush_timer = threading.Timer(self.buffer_delay, self.flush_buffer)
        self.flush_timer.start()

    def finish(self):
        if self.flush_timer is not None:
            self.flush_timer.join()
