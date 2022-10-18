#! /usr/bin/env python3
# coding: utf-8

# ClassAsymetric :

##################################################################################################################################

#### Imports :

from ClassParameters import Parameters
from ClassErrorsManager import ErrorsManager

class Asymetric(object):

    def __init__(self):
        
        print("\n ---> LOADING Asymetric's parameters <--- ")

        #### Parameters :

        self.AsymetricParameters = Parameters.Asymetric()

        #### ErrorsManager :

        ErrorsManager.Asymetric(self.AsysmetricParameters)

    def setupAsymetricKey(self):

        # Explain User how to setupAsymetricKey, which values are accepted :
        os.system("clear")
        print(self.AsymetricParameters['SetupAsymetricKey_InputsAccepted'])
        print("")
        print(self.AsymetricParameters['SetupAsymetricKey_Instructions'])
        
        cmd = input("\n(r)Randomly Generated, (t)Terminal, (f)FileSystem : ") # Ask user the way CryptoApp gets Asymetric Key (Randomly generated, User terminal, User filesystem)

        if cmd == "r": # Cas 1 : Randomly generated :

            # Call asymetricKeyGenerator() :
            AsymetricKey = Asymetric.asymetricKeyGenerator()

            # Save key generated in "AsymetricKey.txt" :
            with open(self.AsymetricParameters['File_AsymetricKey'],'w') as fic_ecri:
                fic_ecri.write(str(AsymetricKey))

        elif cmd == "t": # Cas 2 : Through the Terminal :

            AsymetricKey = int(input("\nAsymetric Key CryptoApp is going to use : \n"))

            # Check if User's input is acceptable :
            if -60 < AsymetricKey < 61:
                pass
            else:
                log.critical("\nAsymetricKey is not valid, please check instructions again.")
                sys.exit()

            # Save key generated in "AsymetricKey.txt" :
            with open(self.AsymetricParameters['File_AsymetricKey'],'w') as fic_ecri:
                fic_ecri.write(str(AsymetricKey))

        elif cmd == "f": # Cas 3 : Through the FileSystem :

            # Check if "AsymetricKey.txt" exist :
            if os.path.isfile(self.AsymetricParameters['File_AsymetricKey']):
                pass
            else:
                log.critical("\nAsymetricKey.txt is not here !")
                sys.exit()                

            # Check if "AsymetricKey.txt" is empty :
            if os.stat("AsymetricKey.txt").st_size == 0:
                log.critical("\nError FileAsymetricKey is empty !")
                sys.exit()

            # Check if "AsymetricKey.txt"'s content is acceptable :
            with open(self.AsymetricParameters['File_AsymetricKey'],'r') as fic_lect:
                AsymetricKey = int(fic_lect.read())
            if -60 < AsymetricKey < 61:
                pass
            else:
                log.critical("\nAsymetricKey is not valid, use terminal command instead.")
                sys.exit()

        else: # UnknowCommand :
            os.system("clear")
            modele = "\n*** Unknown command (%s)"
            print(modele%cmd)

    ### Sub-Function @setupAsymetricKey()
    def AsymetricKeyGenerator(): # Random generation method
        
        # AsymetricKeyGenerated = random.uniform(-60,60)
        # AsymetricKeyGeneratedSignedInt = math.floor(AsymetricKeyGenerated)
        
        return AsymetricKeyGeneratedSignedInt

    def getAsymetricKey(self):

        # Check if "AsymetricKey.txt" exist :
        if os.path.isfile(self.AsymetricParameters['File_AsymetricKey']):
            pass
        else:
            log.critical("\nAsymetricKey.txt is not here !")
            sys.exit()

        # Check if "AsymetricKey.txt" is empty :
        if os.stat("AsymetricKey.txt").st_size == 0:
            log.critical("\nError FileAsymetricKey is empty !")
            sys.exit()

        # Check if "AsymetricKey.txt"'s content is acceptable :
        with open(self.AsymetricParameters['File_AsymetricKey'],'r') as fic_lect:
            AsymetricKey = int(fic_lect.read())
        if -60 < AsymetricKey < 61:
            pass  
        else:
            log.critical("\nAsymetricKey is not valid, please check instructions again.")
            sys.exit()

        return AsymetricKey

    def getAsymetricDictionaries(self,AsymetricKey): # Maj Asymetric dictionnary with the new Asymetric Key :

        # JEUCAR = string.printable[:-5]

        # CARSUBSTI = JEUCAR[AsymetricKey:]+JEUCAR[:AsymetricKey]
        
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
        AsymetricDictionaries = Dictionary(DICO_ENCRYPT, DICO_DECRYPT)

        return AsymetricDictionaries


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



































































































