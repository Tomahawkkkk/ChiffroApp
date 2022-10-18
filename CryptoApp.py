#! /usr/bin/env python3
# coding: utf-8

# CryptoApp :

##################################################################################################################################

#### Imports :

import os
#import pdb # Python DeBugger, mettre en commentaire l'import si je n'utilise pas pdb.set_trace()
import string
import logging as log
import unidecode # Currently used to cancel "Accents" in french message.
from ClassParameters import Parameters
from ClassErrorsManager import ErrorsManager
from ClassCesar import Cesar as cesar
from ClassSymetric import Symetric as symetric
from ClassAsymetric import Asymetric as asymetric

##################################################################################################################################

#### Initial interface :

Initial_Instructions = """
************************************************
		CryptoApp : 

************************************************

Insert the command you are looking for :
ENC Encrypt a message
DOK Decrypt a message (knowing the encrypt method &&& the Key)
DKO Decrypt a message (knowing the encrypt method BUT NOT the Key)
BRK Break the encryption (NOT knowing the encrypt method &&& NOT knowing the Key)
I   Go back to those Instructionss again
Q   To Quit. """

Encrypt_Instructions = """
Which method should I use to ENCRYPT your message ?
CE Cesar
VI Vigenere 
MJ Masque jetable (Vernam)
Q  To Quit. """

Decrypt_Instructions = """
Which method should I used to DECRYPT your message ?
CD CESAR Decryption
VD VIGENERE Decryption 
MD Masque jetable (Vernam)
Q  To Quit. """

Break_Instructions = """
Which method should I use to BREAK your message ?
FA FrequencyAnalysis
IC IndexOfCoincidence 
LW LikelyWord
DI Dictionary
BF Brut Force
Q  To Quit. """

Final_Instructions = """
How should I take your input ?
T Through the TERMINAL
F Through the FileSystem "cryptopy_in.txt"
I Go back to instructions
Q To QUIT. """

confirm_Quit_Instructions = "Do you really want to quit (y/n)?"

##################################################################################################################################

class CryptoApp(object):

	def __init__(self):

		#### Parameters :

		self.CryptoAppParameters = Parameters.CryptoApp()

		#### ErrorsManager :

		ErrorsManager.CryptoApp(self.CryptoAppParameters)

		# Init Kontroleur :
		self.gerer_menu()

#### Main CryptoApp's function : Check keyboard input and lauch the process associated

	def gerer_menu(self):

		while True:

############################################# Initialisation Part ###########################################################

####### Class Initialisation :

			# Class initialisation :
			Cesar = cesar()
			Symetric = symetric()
			Asymetric = asymetric()

			print(Initial_Instructions)
			cmd = input("\n(enc)Encrypt,(dok)DecryptWithKey,(dko)DecryptWithoutKey,(brk)BreakEncryption,(i)Instructions,(q)Quit : ")

############################################## Encryption Part #############################################################

			if cmd == "enc": 
####### Encryption Part :
				os.system("clear")
				print(Encrypt_Instructions)
				cmd = input("\n(ce)sar,(sy)metric,(asy)metric,(q)Quit : ")
				
				if cmd == "ce": 
####### Encryption Part : Cesar :

					# CesarKey initialisation :
					Cesar.setupCesarKey()

					# CesarDictionaries initialisation :
					CesarKey = Cesar.getCesarKey()
					CesarDictionaries = Cesar.getCesarDictionaries(CesarKey)

					cmd = input("\nPress ENTER") # Permet d'afficher les messages d'erreurs avant qu'ils soient "clear"

					os.system("clear")
					print(Final_Instructions)
					cmd = input("\n(t)TerminalInputOuput,(f)FileInputOutput,(i)Instructions,(q)Quit : ")

					if cmd == "t": 
####### Encryption Part : Cesar : Terminal :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nEncryption Part/Cesar/Terminal")

						messageToEncrypt = input(" Message to encrypt : \n")
						messageEncrypted = Cesar.encrypt(messageToEncrypt,CesarDictionaries[0])
						print(" Message encrypted :")
						print(messageEncrypted)
						break

					elif cmd == "f": 
####### Encryption Part : Cesar : FileSystem :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nEncryption Part/Cesar/FileSystem")

						with open(File_IN,'r') as fic_lect:
							messageToEncrypt = fic_lect.read()
		
						messageEncrypted = Cesar.encrypt(messageToEncrypt,CesarDictionaries[0])
		
						with open(File_OUT,'w') as fic_ecri:
							fic_ecri.write(messageEncrypted)
						break

				if cmd == "sy": 
####### Encryption Part : Symetric :
					os.system("clear")
					print(Final_Instructions)
					cmd = input("\n(t)TerminalInputOuput,(f)FileInputOutput,(i)Instructions,(q)Quit : ")

					if cmd == "t": 
####### Encryption Part : Symetric : Terminal :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nEncryption Part/Symetric/Terminal")

						print("\n --- Not Implemented yet --- ")
						break

					elif cmd == "f": 
####### Encryption Part : Symetric : FileSystem :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nEncryption Part/Symetric/FileSystem")

						print("\n --- Not Implemented yet --- ")
						break

				if cmd == "mj": 
####### Encryption Part : Asymetric :
					os.system("clear")
					print(Final_Instructions)
					cmd = input("\n(t)TerminalInputOuput,(f)FileInputOutput,(i)Instructions,(q)Quit : ")

					if cmd == "t": 
####### Encryption Part : Asymetric : Terminal :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nEncryption Part/Asymetric/Terminal")

						print("\n --- Not Implemented yet --- ")
						break

					elif cmd == "f":
####### Encryption Part : Asymetric : FileSystem :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nEncryption Part/Asymetric/FileSystem")

						print("\n --- Not Implemented yet --- ")
						break

############################################ Decryption Part "OK" ##########################################################
#################################### Knowing the Encrypt method &&& the Key ################################################

			if cmd == "dok":
####### Decryption Part OK :
				os.system("clear")
				print(Decrypt_Instructions)
				cmd = input("\n(cd)CESAR Decryption,(sd)SYMETRIC Decryption,(ad)Asymetric Decryption,(q)uit : ")	
				
				if cmd == "cd":
####### Decryption Part : Cesar/Known KEY :

					# CesarDictionaries initialisation :
					CesarKey = Cesar.getCesarKey()
					CesarDictionaries = Cesar.getCesarDictionaries(CesarKey)

					os.system("clear")
					print(Final_Instructions)
					cmd = input("\n(t)TerminalInputOuput,(f)FileInputOutput,(i)Instructions,(q)Quit : ")

					if cmd == "t":
####### Decryption Part : Cesar/Known KEY : Terminal :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nDecryption Part/Cesar/Known KEY/Terminal")

						messageToDecrypt = input(" Message to decrypt : \n")
						messageDecrypted = Cesar.decrypt(messageToDecrypt,CesarDictionaries[1])
						print(" Message decrypted :")
						print(messageDecrypted)
						break

					elif cmd == "f":
####### Decryption Part : Cesar/Known KEY : FileSystem :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nDecryption Part/Cesar/Known KEY/FileSystem")

						with open(File_IN,'r') as fic_lect:
							messageToDecrypt = fic_lect.read()
		
						messageDecrypted = Cesar.decrypt(messageToDecrypt,CesarDictionaries[1])

						with open(File_OUT,'w') as fic_ecri:
							fic_ecri.write(messageDecrypted)

						break

				if cmd == "sd": 
####### Decryption Part : Symetric/Known KEY :
					os.system("clear")
					print(Final_Instructions)
					cmd = input("\n(t)TerminalInputOuput,(f)FileInputOutput,(i)Instructions,(q)Quit : ")

					if cmd == "t":
####### Decryption Part : Symetric/Known KEY : Terminal :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nDecryption Part/Symetric/Known KEY/Terminal")

						print("\n --- Not Implemented yet --- ")
						break

					elif cmd == "f":
####### Decryption Part : Symetric/Known KEY : FileSystem :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nDecryption Part/Symetric/Known KEY/FileSystem")

						print("\n --- Not Implemented yet --- ")
						break

				if cmd == "ad":
####### Decryption Part : Asymetric/Known KEY :
					os.system("clear")
					print(Final_Instructions)
					cmd = input("\n(t)TerminalInputOuput,(f)FileInputOutput,(i)Instructions,(q)Quit : ")

					if cmd == "t":
####### Decryption Part : Asymetric/Known KEY : Terminal :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nDecryption Part/Asymetric/Known KEY/Terminal")

						print("\n --- Not Implemented yet --- ")
						break

					elif cmd == "f":
####### Decryption Part : Asymetric/Known KEY : FileSystem :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nDecryption Part/Asymetric/Known KEY/FileSystem")

						print("\n --- Not Implemented yet --- ")
						break

############################################ Decryption Part "KO" ##########################################################
################################# Knowing the Encrypt method BUT NOT the Key) ##############################################

# [ NOT THE PRIORITY ]

			if cmd == "dko":
####### Decryption Part KO :
				os.system("clear")
				print(Decrypt_Instructions)
				cmd = input("\n(cd)CESAR Decryption,(sd)SYMETRIC Decryption,(ad)ASYMETRIC Decryption,(q)uit : ")	

				if cmd == "cd":
####### Decryption Part : Cesar/Unknown KEY :
					os.system("clear")
					print(Final_Instructions)
					cmd = input("\n(t)TerminalInputOuput,(f)FileInputOutput,(i)Instructions,(q)Quit : ")

					if cmd == "t":
####### Decryption Part : Cesar/Unknown KEY : Terminal :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nDecryption Part/Cesar/Unknown KEY/Terminal")

						print("\n --- Not Implemented yet --- ")
						break

					elif cmd == "f":
####### Decryption Part : Cesar/Unknown KEY : FileSystem :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nDecryption Part/Cesar/Unknown KEY/FileSystem")

						print("\n --- Not Implemented yet --- ")
						break

				if cmd == "sd":
####### Decryption Part : Symetric/Unknown KEY :
					os.system("clear")
					print(Final_Instructions)
					cmd = input("\n(t)TerminalInputOuput,(f)FileInputOutput,(i)Instructions,(q)Quit : ")

					if cmd == "t": 
####### Decryption Part : Symetric/Unknown KEY : Terminal :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nDecryption Part/Symetric/Unknown KEY/Terminal")

						print("\n --- Not Implemented yet --- ")
						break

					elif cmd == "f":
####### Decryption Part : Symetric/Unknown KEY : FileSystem :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nDecryption Part/Symetric/Unknown KEY/FileSystem")

						print("\n --- Not Implemented yet --- ")
						break

				if cmd == "ad":
####### Decryption Part : Asymetric/Unknown KEY :
					os.system("clear")
					print(Final_Instructions)
					cmd = input("\n(t)TerminalInputOuput,(f)FileInputOutput,(i)Instructions,(q)Quit : ")

					if cmd == "t":
####### Decryption Part : Asymetric/Unknown KEY : Terminal :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nDecryption Part/Asymetric/Unknown KEY/Terminal")

						print("\n --- Not Implemented yet --- ")
						break

					elif cmd == "f":
####### Decryption Part : Asymetric/Unknown KEY : FileSystem :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nDecryption Part/Asymetric/Unknown KEY/FileSystem")

						print("\n --- Not Implemented yet --- ")
						break

############################################## Breaking Part ###############################################################
########################### NOT knowing the encrypt method &&& NOT knowing the Key #########################################

# [ NEED A DATASET of crypted data with different level ]

			if cmd == "brk": 
####### Breaking Part :
				os.system("clear")
				print(Break_Instructions)
				cmd = input("\n(fa)FrequencyAnalysis,(ic)IndexOfCoincidence,(lw)LikelyWord,(di)Dictionary,(bf)Brute Forc,(q)uit : ")

				if cmd == "fa": 
####### Breaking Part : FrequencyAnalysis :
					os.system("clear")
					print(Final_Instructions)
					cmd = input("\n(t)TerminalInputOuput,(f)FileInputOutput,(i)Instructions,(q)Quit : ")

					if cmd == "t":
####### Breaking Part : FrequencyAnalysis : Terminal :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nBreaking Part/FrequencyAnalysis/Terminal")

						print("\n --- Not Implemented yet --- ")
						break

					elif cmd == "f":
####### Breaking Part : FrequencyAnalysis : FileSystem :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nBreaking Part/FrequencyAnalysis/FileSystem")

						print("\n --- Not Implemented yet --- ")
						break

				if cmd == "ic":
####### Breaking Part : IndexOfCoincidence :
					os.system("clear")
					if self.CryptoAppParameters['DisplayUserPath']:
							print(Final_Instructions)

					cmd = input("\n(t)TerminalInputOuput,(f)FileInputOutput,(i)Instructions,(q)Quit : ")

					if cmd == "t":
####### Breaking Part : IndexOfCoincidence : Terminal :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nBreaking Part/IndexOfCoincidence/Terminal")

						print("\n --- Not Implemented yet --- ")
						break

					elif cmd == "f":
####### Breaking Part : IndexOfCoincidence : FileSystem :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nBreaking Part/IndexOfCoincidence/FileSystem")

						print("\n --- Not Implemented yet --- ")
						break

				if cmd == "lw":
####### Breaking Part : LikelyWord :
					os.system("clear")
					print(Final_Instructions)
					cmd = input("\n(t)TerminalInputOuput,(f)FileInputOutput,(i)Instructions,(q)Quit : ")

					if cmd == "t":
####### Breaking Part : LikelyWord : Terminal :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nBreaking Part/LikelyWord/Terminal")

						print("\n --- Not Implemented yet --- ")
						break

					elif cmd == "f":
####### Breaking Part : LikelyWord : FileSystem :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nBreaking Part/LikelyWord/FileSystem")

						print("\n --- Not Implemented yet --- ")
						break

				if cmd == "di":
####### Breaking Part : Dictionary :
					os.system("clear")
					print(Final_Instructions)
					cmd = input("\n(t)TerminalInputOuput,(f)FileInputOutput,(i)Instructions,(q)Quit : ")

					if cmd == "t":
####### Breaking Part : Dictionary : Terminal :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nBreaking Part/Dictionary/Terminal")

						print("\n --- Not Implemented yet --- ")
						break

					elif cmd == "f":
####### Breaking Part : Dictionary : FileSystem :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nBreaking Part/Dictionary/FileSystem")

						print("\n --- Not Implemented yet --- ")
						break

				if cmd == "bf":
####### Breaking Part : BruteForce :
					os.system("clear")
					print(Final_Instructions)
					cmd = input("\n(t)TerminalInputOuput,(f)FileInputOutput,(i)Instructions,(q)Quit : ")

					if cmd == "t":
####### Breaking Part : BruteForce : Terminal :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nBreaking Part/BruteForce/Terminal")

						print("\n --- Not Implemented yet --- ")
						break

					elif cmd == "f":
####### Breaking Part : BruteForce : FileSystem :
						os.system("clear")
						if self.CryptoAppParameters['DisplayUserPath']:
							print("\nBreaking Part/BruteForce/FileSystem")

						print("\n --- Not Implemented yet --- ")
						break

			elif cmd == "i":
####### Instructions Part :
				os.system("clear")
				if self.CryptoAppParameters['DisplayUserPath']:
					print("\nMainInterface/Instructions")

				print(Initial_Instructions)

			elif cmd == "q":
####### Quit Part :
				os.system("clear")
				if self.CryptoAppParameters['DisplayUserPath']:
					print("\nMainInterface/Quit")

				if confirm_Quit():
					print("\nCryptoApp is shutting off\n")
					break

			else:
####### UnknowCommand Part :
				os.system("clear")
				if self.CryptoAppParameters['DisplayUserPath']:
					print("\nMainInterface/UnknowCommand")

				modele = "\n*** Unknown command (%s)"
				print(modele%cmd)

### Section Fonctions
def confirm_Quit():
	""" On sort seulement si saisie de la lettre n minuscule par renvoi de False. """
	confi = input(confirm_Quit_Instructions)
	if confi == 'n':
		return False
	else:
		return True

##############################################################################################################

#### Main Section
# Si tu importe ce script, Python charge toutes les fonctions et variables sans rien executer de la section principale.
if __name__ == "__main__": # Fonctionne si import en modules

	cryptoApp = CryptoApp()

