# install package
# py -m pip install pyautogui pyttsx3 pydirectinput flask opencv-python


import pyautogui
import pyttsx3
import pydirectinput
import time

from flask import Flask, request
from int_to_idr import intToIDR

app = Flask(__name__)

@app.route('/', methods=['POST'])

def index():

	getResponseData = request.json 

	# created_at (string): The timestamp when the event occurred. It follows the ISO 8601 format: YYYY-MM-DDTHH:MM:SS±HH:MM.
	# transaction_id (string): The unique identifier for the transaction.
	# type (string): The type of event that occurred. In this case, it is a "tip" event.
	# supporter_name (string): The name of the supporter who send the tip.
	# supporter_avatar (string): The URL of the supporter's avatar image.
	# supporter_message (string): A message left by the supporter (optional).
	# media (object): A media object containing additional details about the media (Media Share feature).
	# unit (string): The unit of creator.
	# unit_icon (string): The URL of the icon image representing the unit.
	# quantity (number): The quantity of the unit associated with the tip.
	# price (float): The total price of the unit in the tip.
	# net_amount (float): The net amount received after deductions, such as payment fee and service fee.

	# Get Data from Trakteer Webhook API

	createdAt = getResponseData['created_at']	
	transactionId = getResponseData['transaction_id']
	type = getResponseData['type']
	supporterName = getResponseData['supporter_name']
	supporterAvatar = getResponseData['supporter_avatar']
	supporterMessage = getResponseData['supporter_message']
	media = getResponseData['media']
	unit = getResponseData['unit']
	unitIcon = getResponseData['unit_icon']
	quantity = getResponseData['quantity']
	price = getResponseData['price']
	net_amount = getResponseData['net_amount']


	# Add this code, if you want your computer read the support.

	# engine = pyttsx3.init()
	# engine.getProperty('rate')
	# engine.setProperty('rate', 125)
	# engine.say("Traktiran dari" + supporterName)
	# engine.runAndWait()
	# engine.stop()
	
	timeOut = time.time() + 10

	# Write data on log
	print('Traktiran dari: ' + supporterName)
	print('Unit: ' + str(quantity) + ' ' + unit)
	print('Sebesar: Rp.' + intToIDR(price) )

	if price <= 5000:
		while time.time() < timeOut:
			pydirectinput.keyDown('W')
		pydirectinput.keyUp('W')

	elif price <= 10000:
		while time.time() < timeOut:
			pydirectinput.press('F')

	elif price <= 25000:
		while time.time() < timeOut:
			pydirectinput.press('X')
	
	elif price <= 50000:
		if supporterMessage:
			# type something on valorant / game chat
			pydirectinput.keyDown('shift')
			pydirectinput.keyDown('enter')
			pydirectinput.keyUp('enter')
			pydirectinput.keyUp('shift')
			pyautogui.write(supporterMessage + ' from ' + supporterName)
			pydirectinput.press('enter')

	elif price <= 100000:
		while time.time() < timeOut:
			pydirectinput.keyDown('ctrl')
		pydirectinput.keyUp('ctrl')

	elif price > 100000:
		pydirectinput.click()


	return ('success', 200)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080)


