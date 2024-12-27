import pandas as pd 
import datetime as dt 
from WindPy import w


class wdAPI:
	def __init__(self):
		if not w.isConnected():
			w.start()
		self.w = w
