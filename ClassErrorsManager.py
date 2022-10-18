#! /usr/bin/env python3
# coding: utf-8

# ClassErrorsManager :

#    Description : Permet de centraliser toutes les gestions d'erreurs de CryptoApp.

##################################################################################################################################

#### Imports :

import os
import logging as log

class ErrorsManager(object):

    # def __init__(self):

    def CryptoApp(ParametersCryptoApp):

        # Check if File_In exist :
        try:
            with open(ParametersCryptoApp['File_IN'],'r') as fileIn:
                if ParametersCryptoApp['DisplayFilePreview']:
                    preview = fileIn.read()
                    print("\nFile_IN has been found. Here is a preview: {%s}" % preview)

        except FileNotFoundError :
            log.critical("\nFile_IN was not found ... It is being automatically generated ...\n")
            open("cryptoApp_in.txt","w+") # Générer cryptoApp_in.txt

        finally :
            fileIn.close()

        # Check if File_Out exist :
        try:
            with open(ParametersCryptoApp['File_OUT'],'r') as fileOut:
                if ParametersCryptoApp['DisplayFilePreview']:
                    preview = fileOut.read()
                    print("\nFile_OUT has been found, here is a preview: {%s}" % preview)

        except FileNotFoundError :
            log.critical("\nFile_OUT was not found ... It is being automatically generated ...\n")
            open("cryptoApp_out.txt","w+") # Générer cryptoApp_out.txt

        finally :
            fileOut.close()

        cmd = input("\n@CryptoApp --> No errors reported\nPress ENTER")
        os.system("clear")

    def Cesar(ParametersCesar):

        # Check if File_CesarKey exist :
        try:
            with open(ParametersCesar['File_CesarKey'],'r') as fileCesarKey:
                if ParametersCesar['CesarDisplayFilePreview']:
                    preview = fileCesarKey.read()
                    print("\nFile_CesarKey has been found. Here is a preview: {%s}" % preview)

        except FileNotFoundError :
            log.critical("\nFile_CesarKey has not been found ... It is being automatically generated ...")
            open("cesarKey.txt","w+") # Génère cesarKey.txt

        finally :
            fileCesarKey.close()

        cmd = input("\n@ClassCesar --> No errors reported\nPress ENTER")
        os.system("clear")

    def Symetric(ParametersSymetric):

        # Check if File_SymetricKey exist :
        try:
            with open(ParametersSymetric['File_SymetricKey'],'r') as fileSymetricKey:
                if ParametersSymetric['SymetricDisplayFilePreview']:
                    preview = fileSymetricKey.read()
                    print("\nFile_SymetricKey has been found. Here is a preview: {%s}" % preview)

        except FileNotFoundError :
            log.critical("\nFile_SymetricKey has not been found ... It is being automatically generated ...")
            open("symetricKey.txt","w+") # Génère symetricKey.txt

        finally :
            fileSymetricKey.close()

        cmd = input("\n@ClassSymetric --> No errors reported\nPress ENTER")
        os.system("clear")

    def Asymetric(ParametersAsymetric):

        # Check if File_AsymetricKey exist :
        try:
            with open(ParametersAsymetric['File_AsymetricKey'],'r') as fileAsymetricKey:
                if ParametersAsymetric['AsymetricDisplayFilePreview']:
                    preview = fileAsymetricKey.read()
                    print("\nFile_AsymetricKey has been found. Here is a preview: {%s}" % preview)

        except FileNotFoundError :
            log.critical("\nFile_AsymetricKey has not been found ... It is being automatically generated ...")
            open("asymetricKey.txt","w+") # Génère asymetricKey.txt

        finally :
            fileAsymetricKey.close()

        cmd = input("\n@ClassAsymetric --> No errors reported\nPress ENTER")
        os.system("clear")




































































































