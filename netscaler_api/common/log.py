from logging import Formatter
import time

class UTCFormatter(Formatter):
  converter = time.gmtime
