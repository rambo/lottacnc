from flask import Flask
import serial

serialport = None

def init_serial(app):
	global serialport

	parity = app.config['SERIAL_PARITY']

	serialport = serial.serial_for_url(app.config['SERIAL_PORT'], app.config['SERIAL_BAUD'], timeout=1)
	serialport.bytesize = app.config['SERIAL_BITS']
	serialport.stopbits = app.config['SERIAL_STOPBITS']
	serialport.parity = app.config['SERIAL_PARITY']
	serialport.rtscts = app.config['SERIAL_RTSCTS']

app = Flask(__name__)
app.config.from_object('app.settings.Production')
app.config.from_pyfile('lotta.cfg', silent=True)
app.config.from_envvar('LOTTA_SETTINGS', silent=True)

init_serial(app)

from app import views