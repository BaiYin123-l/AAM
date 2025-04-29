import time

from src.Listeners import Listeners

a = Listeners()
a.start()
time.sleep(1)
a.stop()