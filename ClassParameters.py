#! /usr/bin/env python3
# coding: utf-8

# ClassParameters :

#    Description : Permet de centraliser toutes les paramètres de CryptoApp. Cette Class sera intialiser au tout début, une seule fois.

##################################################################################################################################

#### Imports :

class Parameters(object):

    # def __init__(self):

    #     print("\n --- Parameters.__init__() Not Implemented yet --- ")

    def CryptoApp():

        CryptoAppParameters = {'DisplayFilePreview' : False, 
                                'DisplayUserPath' : False,
                                'File_IN' : "cryptoApp_in.txt",
                                'File_OUT' : "cryptoApp_out.txt"}

        return CryptoAppParameters
    
    def Cesar():

        CesarParameters = {'CesarDisplayFilePreview' : False, 
        'CesarDisplayUserPath' : False,
        'File_CesarKey' : "cesarKey.txt",
        'SetupCesarKey_InputsAccepted' : """
                [INFORMATION]
        Input XXX is accepted only if :
             
                -60 < XXX < 61 """,
        'SetupCesarKey_Instructions' : """Generate Cesar Key Randomly or with User's choice through TERMINAL or FILESYSTEM ?
        R Randomly generated
        T Through the TERMINAL
        F Through the FileSystem "cesarKey.txt". """}

        return CesarParameters

    def Symetric():

        print("\n --- Parameters.Symetric() Not Implemented yet --- ")

    def Asymetric():

        print("\n --- Parameters.Asymetric() Not Implemented yet --- ")

