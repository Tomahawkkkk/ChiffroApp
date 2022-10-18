#! /usr/bin/env python3
# coding: utf-8

# ClassCesar :

##################################################################################################################################

#### Imports :

import os
import sys
#import pdb # Python DeBugger, put this line in commentary if I am not using pdb.set_trace()
import string
import logging as log
import unidecode # Currently used to cancel "Accents" in french message.
import collections # Currently used for CesarDictionaries
import random  # Curently used for cesarKeyGenerator()
import math # Curently used for cesarKeyGenerator()
from ClassParameters import Parameters
from ClassErrorsManager import ErrorsManager

class Cesar(object):

    def __init__(self):
        
        print("\n ---> LOADING Cesar's parameters <--- ")

        #### Parameters :

        self.CesarParameters = Parameters.Cesar()

        #### ErrorsManager :

        ErrorsManager.Cesar(self.CesarParameters)

    def setupCesarKey(self):

        # Explain User how to setupCesarKey, which values are accepted :
        os.system("clear")
        print(self.CesarParameters['SetupCesarKey_InputsAccepted'])
        print("")
        print(self.CesarParameters['SetupCesarKey_Instructions'])
        
        cmd = input("\n(r)Randomly Generated, (t)Terminal, (f)FileSystem : ") # Ask user the way CryptoApp gets Cesar Key (Randomly generated, User terminal, User filesystem)

        if cmd == "r": # Cas 1 : Randomly generated :

            # Call cesarKeyGenerator() :
            CesarKey = Cesar.cesarKeyGenerator()

            # Save key generated in "cesarKey.txt" :
            with open(self.CesarParameters['File_CesarKey'],'w') as fic_ecri:
                fic_ecri.write(str(CesarKey))

        elif cmd == "t": # Cas 2 : Through the Terminal :

            CesarKey = int(input("\nCesar Key CryptoApp is going to use : \n"))

            # Check if User's input is acceptable :
            if -60 < CesarKey < 61:
                pass
            else:
                log.critical("\nCesarKey is not valid, please check instructions again.")
                sys.exit()

            # Save key generated in "cesarKey.txt" :
            with open(self.CesarParameters['File_CesarKey'],'w') as fic_ecri:
                fic_ecri.write(str(CesarKey))

        elif cmd == "f": # Cas 3 : Through the FileSystem :

            # Check if "cesarKey.txt" exist :
            if os.path.isfile(self.CesarParameters['File_CesarKeyFile_CesarKey']):
                pass
            else:
                log.critical("\ncesarKey.txt is not here !")
                sys.exit()                

            # Check if "cesarKey.txt" is empty :
            if os.stat("cesarKey.txt").st_size == 0:
                log.critical("\nError FileCesarKey is empty !")
                sys.exit()

            # Check if "cesarKey.txt"'s content is acceptable :
            with open(self.CesarParameters['File_CesarKey'],'r') as fic_lect:
                CesarKey = int(fic_lect.read())
            if -60 < CesarKey < 61:
                pass
            else:
                log.critical("\nCesarKey is not valid, use terminal command instead.")
                sys.exit()

        else: # UnknowCommand :
            os.system("clear")
            modele = "\n*** Unknown command (%s)"
            print(modele%cmd)

    ### Sub-Function @setupCesarKey()
    def cesarKeyGenerator(): # Random generation method
        
        CesarKeyGenerated = random.uniform(-60,60)
        CesarKeyGeneratedSignedInt = math.floor(CesarKeyGenerated)
        
        return CesarKeyGeneratedSignedInt

    def getCesarKey(self):

        # Check if "cesarKey.txt" exist :
        if os.path.isfile(self.CesarParameters['File_CesarKey']):
            pass
        else:
            log.critical("\ncesarKey.txt is not here !")
            sys.exit()

        # Check if "cesarKey.txt" is empty :
        if os.stat("cesarKey.txt").st_size == 0:
            log.critical("\nError FileCesarKey is empty !")
            sys.exit()

        # Check if "cesarKey.txt"'s content is acceptable :
        with open(self.CesarParameters['File_CesarKey'],'r') as fic_lect:
            CesarKey = int(fic_lect.read())
        if -60 < CesarKey < 61:
            pass  
        else:
            log.critical("\nCesarKey is not valid, please check instructions again.")
            sys.exit()

        return CesarKey

    def getCesarDictionaries(self,CesarKey): # Maj Cesar dictionnary with the new Cesar Key :

        JEUCAR = string.printable[:-5] # We save the alphabets + some characters into a single variable (tabulations \t are ignored)

        CARSUBSTI = JEUCAR[CesarKey:]+JEUCAR[:CesarKey] # Here we cut the lasts characters and paste them at the beginning to introduce the shift needed for Cesar method thanks to the CesarKey provided
        
        # Creating each dictionary with the shifted characters (cleared).
        DICO_ENCRYPT = {}
        DICO_DECRYPT = {}
        for i,k in enumerate(JEUCAR):
            v = CARSUBSTI[i]
            DICO_ENCRYPT[k] = v
            DICO_DECRYPT[v] = k
        # The others \t, \n etc. stay the same
        for c in string.printable[-5:]: # Careful about the ":"
            DICO_ENCRYPT[c] = c
            DICO_DECRYPT[c] = c

        Dictionary = collections.namedtuple('Dictionary', ['Encrypt', 'Decrypt'])
        CesarDictionaries = Dictionary(DICO_ENCRYPT, DICO_DECRYPT)

        return CesarDictionaries


    def encrypt(self,messageToEncrypt,dico_encrypt):
        # Explanation : Encrypt the real message thanks to the Dictionary given as an argument and return the encrypted text

        # Cancel all accents from message:
        unaccented_messageToEncrypt = unidecode.unidecode(messageToEncrypt)

        # Starting encryption
        messageEncrypted = []
        for k in unaccented_messageToEncrypt:
            v = dico_encrypt[k]
            messageEncrypted.append(v)

        return ''.join(messageEncrypted)

    def decrypt(self,messageToDecrypt,dico_decrypt):
        # Explanation : Decrypt the encrypted text thanks to the Dictionary given as an argument and return the real message

        # Cancel all accents from message:
        unaccented_messageToDecrypt = unidecode.unidecode(messageToDecrypt)

        # Starting decryptionn
        messageDecrypted = []
        for k in unaccented_messageToDecrypt:
            v = dico_decrypt[k]
            messageDecrypted.append(v)

        return ''.join(messageDecrypted)



































































































