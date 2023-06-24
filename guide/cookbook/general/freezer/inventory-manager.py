## importing packages
import pandas as pd
from datetime import datetime
from subprocess import Popen
import time

## Defining a class for managing the freezer inventory.
class inventory():

	## Initialising the class
	def __init__(self):
		super(inventory, self).__init__()
		## importing data frame from csv file
		self.freezer = pd.read_csv('../../../../_data/cookbook/freezer.csv')
		self.interface()

	## Function to add new entries to data frame.
	def addEntry(self):
		item = input("What are you freezing?: ")
		quantity = input("How many " + item + " should we log?: ")
		while quantity not in ["1", "2", "3", "4", "5"]:
			print("Please enter an integer number between 1 and 5.")
			quantity = input("How many " + item + " should we log?: ")
		note = input("Anything to note?: ")
		while "," in note:
			print("Please avoid using ',' punctuation.")
			note = input("Anything to note?: ")
		shelf = input("Where did you put it? Choose a shelf from 1 to 4: ")
		now = datetime.now() # take current date and time
		date = now.strftime("%d-%b-%Y") # format date to dd-Mon-yyyy
		code = now.strftime("%j-%M%S") # generate code based on day of the year, with minutes and seconds.
		newEntry = pd.Series([item, int(quantity), note, shelf, date, code], index=self.freezer.columns)
		self.freezer = self.freezer.append(newEntry, ignore_index=True)
		self.save = self.freezer.to_csv(r'../../../../_data/cookbook/freezer.csv', index = None, header=True)
		print(item + " added to the inventory.")

	## Function to remove entries.
	def removeEntry(self):
		code = input("Enter the code of the item to be removed: ")
		for i in range(0, len(self.freezer.Code)):
			if code == self.freezer.Code[i]:
				if int(self.freezer.Quantity[i]) == 1:
					print(self.freezer.Item[i] + " is out of stock.")
					self.freezer = self.freezer.drop(index = i)
				elif int(self.freezer.Quantity[i]) > 1:
					self.freezer.Quantity[i] = 		int(self.freezer.Quantity[i]) - 1
					print(str(self.freezer.Quantity[i]) + self.freezer.Item[i] + " left.")
			else:
				pass
		self.save = self.freezer.to_csv(r'../../../../_data/cookbook/freezer.csv', index = None, header=True)

	## Function for the CLI.
	def interface(self):
		action = input("What would you like to do? Type add, remove, or quit: ")
		while action not in ["add", "remove", "quit"] or action == "":
			print("Enter a valid option: add, remove, or quit.")
			action = input("What would you like to do? Type add, remove, or quit: ")
		if action == "add":
			self.addEntry()
			self.interface()
		elif action == "remove":
			self.removeEntry()
			self.interface()
		else:
			commit = input("Would you like to push changes online after quitting? Type y or n: ")
			while commit not in ["y", "n"] or commit == "":
				print("Enter a valid option: y or n.")
				commit = input("Would you like to push changes online after quitting? Type y or n: ")
			if commit == "n":
				print("Changes will not be uploaded.")
			elif commit == "y":
				print("Upload request is registered.")
				Popen("deploy27", shell=True)
				time.sleep(30)

## +++Run script+++
inventory()