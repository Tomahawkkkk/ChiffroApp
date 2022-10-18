#! /usr/bin/env python3
# coding: utf-8

# ClassSymetric :

##################################################################################################################################

#### Imports :

from ClassParameters import Parameters
from ClassErrorsManager import ErrorsManager

class Symetric(object):

    def __init__(self):
        
        print("\n ---> LOADING Symetric's parameters <--- ")

        #### Parameters :

        self.SymetricParameters = Parameters.Symetric()

        #### ErrorsManager :

        ErrorsManager.Symetric(self.SysmetricParameters)

    def setupSymetricKey(self):

        # Explain User how to setupSymetricKey, which values are accepted :
        os.system("clear")
        print(self.SymetricParameters['SetupSymetricKey_InputsAccepted'])
        print("")
        print(self.SymetricParameters['SetupSymetricKey_Instructions'])
        
        cmd = input("\n(r)Randomly Generated, (t)Terminal, (f)FileSystem : ") # Ask user the way CryptoApp gets Symetric Key (Randomly generated, User terminal, User filesystem)

        if cmd == "r": # Cas 1 : Randomly generated :

            # Call symetricKeyGenerator() :
            SymetricKey = Symetric.symetricKeyGenerator()

            # Save key generated in "SymetricKey.txt" :
            with open(self.SymetricParameters['File_SymetricKey'],'w') as fic_ecri:
                fic_ecri.write(str(SymetricKey))

        elif cmd == "t": # Cas 2 : Through the Terminal :

            SymetricKey = int(input("\nSymetric Key CryptoApp is going to use : \n"))

            # Check if User's input is acceptable :
            if -60 < SymetricKey < 61:
                pass
            else:
                log.critical("\nSymetricKey is not valid, please check instructions again.")
                sys.exit()

            # Save key generated in "symetricKey.txt" :
            with open(self.SymetricParameters['File_SymetricKey'],'w') as fic_ecri:
                fic_ecri.write(str(SymetricKey))

        elif cmd == "f": # Cas 3 : Through the FileSystem :

            # Check if "SymetricKey.txt" exist :
            if os.path.isfile(self.SymetricParameters['File_SymetricKey']):
                pass
            else:
                log.critical("\nSymetricKey.txt is not here !")
                sys.exit()                

            # Check if "SymetricKey.txt" is empty :
            if os.stat("SymetricKey.txt").st_size == 0:
                log.critical("\nError FileSymetricKey is empty !")
                sys.exit()

            # Check if "SymetricKey.txt"'s content is acceptable :
            with open(self.SymetricParameters['File_SymetricKey'],'r') as fic_lect:
                SymetricKey = int(fic_lect.read())
            if -60 < SymetricKey < 61:
                pass
            else:
                log.critical("\nSymetricKey is not valid, use terminal command instead.")
                sys.exit()

        else: # UnknowCommand :
            os.system("clear")
            modele = "\n*** Unknown command (%s)"
            print(modele%cmd)

    ### Sub-Function @setupSymetricKey()
    def symetricKeyGenerator(): # Random generation method
        
        # SymetricKeyGenerated = random.uniform(-60,60)
        # SymetricKeyGeneratedSignedInt = math.floor(SymetricKeyGenerated)
        
        return AsymetricKeyGeneratedSignedInt

    def getSymetricKey(self):

        # Check if "SymetricKey.txt" exist :
        if os.path.isfile(self.SymetricParameters['File_SymetricKey']):
            pass
        else:
            log.critical("\nSymetricKey.txt is not here !")
            sys.exit()

        # Check if "SymetricKey.txt" is empty :
        if os.stat("SymetricKey.txt").st_size == 0:
            log.critical("\nError FileSymetricKey is empty !")
            sys.exit()

        # Check if "SymetricKey.txt"'s content is acceptable :
        with open(self.SymetricParameters['File_SymetricKey'],'r') as fic_lect:
            SymetricKey = int(fic_lect.read())
        if -60 < SymetricKey < 61:
            pass  
        else:
            log.critical("\nSymetricKey is not valid, please check instructions again.")
            sys.exit()

        return SymetricKey

    def getSymetricDictionaries(self,SymetricKey): # Maj Symetric dictionnary with the new Symetric Key :

        # JEUCAR = string.printable[:-5] # We save the alphabets + some characters into a single variable (tabulations \t are ignored)

        # CARSUBSTI = JEUCAR[SymetricKey:]+JEUCAR[:SymetricKey]
        
        # # Creating each dictionary with the shifted characters (cleared).
        # DICO_ENCRYPT = {}
        # DICO_DECRYPT = {}
        # for i,k in enumerate(JEUCAR):
        #     v = CARSUBSTI[i]
        #     DICO_ENCRYPT[k] = v
        #     DICO_DECRYPT[v] = k
        # # The others \t, \n etc. stay the same
        # for c in string.printable[-5:]: # Careful about the ":"
        #     DICO_ENCRYPT[c] = c
        #     DICO_DECRYPT[c] = c

        Dictionary = collections.namedtuple('Dictionary', ['Encrypt', 'Decrypt'])
        SymetricDictionaries = Dictionary(DICO_ENCRYPT, DICO_DECRYPT)

        return SymetricDictionaries


    def encrypt(self,messageToEncrypt,dico_encrypt):
        # Explanation : Encrypt the real message thanks to the Dictionary given as an argument and return the encrypted text

        # Cancel all accents from message:
        unaccented_messageToEncrypt = unidecode.unidecode(messageToEncrypt)

        # # Starting encryption
        # messageEncrypted = []
        # for k in unaccented_messageToEncrypt:
        #     v = dico_encrypt[k]
        #     messageEncrypted.append(v)

        return ''.join(messageEncrypted)

    def decrypt(self,messageToDecrypt,dico_decrypt):
        # Explanation : Decrypt the encrypted text thanks to the Dictionary given as an argument and return the real message

        # Cancel all accents from message:
        unaccented_messageToDecrypt = unidecode.unidecode(messageToDecrypt)

        # # Starting decryptionn
        # messageDecrypted = []
        # for k in unaccented_messageToDecrypt:
        #     v = dico_decrypt[k]
        #     messageDecrypted.append(v)

        return ''.join(messageDecrypted)



































































































