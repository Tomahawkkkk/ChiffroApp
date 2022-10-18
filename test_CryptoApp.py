import string
import pytest
import CryptoApp_v1 as script

# - AppDeChiffrement : 

class Test_CryptoApp:

#   - Verifier la fonction 'encrypter', cas nominal :
	def test_encrypter_1(self):
		messageACrypter = 'Je m appelle Thomas'
		messagecrypte = script.Kontroleur.encrypter(self,messageACrypter,script.DICO_ENCRYPT)
		assert messagecrypte == 'Gb|j|7mmbiib|Qelj7p'

		#   - Verifier la fonction 'encrypter', cas avec plein de caractere aleatoire :
	def test_encrypter_2(self):
		messageACrypter = 'N4d,/;UokZ&jh_HtQ<@R\X7O=v2+T^Y~Dx9:IrL|Mz>nCJ3f0q'
		messagecrypte = script.Kontroleur.encrypter(self,messageACrypter,script.DICO_ENCRYPT)
		assert messagecrypte == 'K1a),.RlhW#ge\EqN/=O?U4L:s (Q[V{Au6-FoI_Jw;kzG0c}n'

		#   - Verifier la fonction 'decrypter', cas nominal :
	def test_decrypter_1(self):
		messageADecrypter = 'Gb|j|7mmbiib|Qelj7p'
		messagedecrypte = script.Kontroleur.decrypter(self,messageADecrypter,script.DICO_DECRYPT)
		assert messagedecrypte == 'Je m appelle Thomas'

		#   - Verifier la fonction 'encrypter', cas avec plein de caractere aleatoire :
	def test_decrypter_2(self):
		messageADecrypter = 'K1a),.RlhW#ge\EqN/=O?U4L:s (Q[V{Au6-FoI_Jw;kzG0c}n'
		messagedecrypte = script.Kontroleur.decrypter(self,messageADecrypter,script.DICO_DECRYPT)
		assert messagedecrypte == 'N4d,/;UokZ&jh_HtQ<@R\X7O=v2+T^Y~Dx9:IrL|Mz>nCJ3f0q'

# class A_Helper:
#     def __init__(self, fixture):
#         print "In class A_Helper"

#     def some_method_in_a_helper(self):
#         print "foo"

# @pytest.fixture(scope='class')
# def a_helper(fixture):
#     return A_Helper(fixture)

# class Test_class:
#     def test_some_method(self, a_helper):
#         a_helper.some_method_in_a_helper()
#         assert 0 == 0