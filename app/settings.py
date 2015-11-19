import serial # oh I'm gonna be so very sorry for this

class Config(object):
	SERIAL_PORT = "/dev/ttyUSB0"
	SERIAL_BAUD = 2400
	SERIAL_PARITY = serial.PARITY_EVEN
	SERIAL_BITS = serial.SEVENBITS
	SERIAL_STOPBITS = serial.STOPBITS_TWO
	SERIAL_RTSCTS = True

class Development(Config):
	DEBUG = True

class Production(Config):
	DEBUG = False