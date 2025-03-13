import pyttsx3
import threading
import queue
import time

class RealTimeTTS:
    def __init__(self, rate=200):
        self.rate = rate
        self.queue = queue.Queue()
        self.worker = threading.Thread(target=self._worker, daemon=True)
        self.worker.start()
    
    def _worker(self):
        while True:
            word = self.queue.get()
            if word is None:
                break
            engine = pyttsx3.init()
            engine.setProperty('rate', self.rate)
            engine.say(word)
            engine.runAndWait()
            engine.stop()
            self.queue.task_done()
    
    def speak_word(self, word):
        self.queue.put(word)
    
    def finish(self):
        self.queue.join()
    
    def shutdown(self):
        self.queue.put(None)
        self.worker.join()
