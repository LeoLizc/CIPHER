import unittest as ut
from codifier import *
from alphabet import changeAlphabet, getAlphabetFromKey

class TestCaesar(ut.TestCase):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def test_caesarCipher(self):
        self.assertEqual(caesarCipher('Hello, World!', 3, alphabet=self.alphabet), 'Khoor, Zruog!', 'need ')
        self.assertEqual(caesarCipher('Hello, World!', -3,alphabet=self.alphabet), 'Ebiil, Tloia!', 'hola')
        
    def test_cipherDefault(self):
        self.assertEqual(caesarCipher('Hello, World!',alphabet=self.alphabet), 'Khoor, Zruog!', 'need some fixes by default')
        self.assertEqual(caesarCipher('Hello, World!',alphabet=self.alphabet), caesarCipher('Hello, World!', 3,alphabet=self.alphabet), 'should be the same')


class TestSubstitution(ut.TestCase):
    def test_defaultAlphabet(self):
        self.assertEqual(keywordCipher('abcdefghijklmnopqrstuvwxyz', 'cipher'), 'cipherstuvwxyzabdfgjklmnoq', 'should be the same')
        self.assertEqual(keywordCipher('abcdefghijklmnopqrstuvwxyz', 'clave'), 'clavefghijkmnopqrstuwxyzbd', 'should be the same')
        self.assertEqual(keywordCipher('abcdefghijklmnopqrstuvwxyz', 'hola'), 'holabcdefgijkmnpqrstuvwxyz', 'should be the same')

    # def test_phrases(self):
    #     self.assertEqual(substitutionCipher('Hello, World!', 'hola'), changeAlphabet('Hello World!'), 'should be the same')
    #     self.assertEqual(substitutionCipher('Hello, World!', 'clave'), changeAlphabet('Hello World!', newAlphabet=getAlphabetFromKey('clave')), 'should be the same')