import unittest
import verif

class TestStringMethods(unittest.TestCase):

#check if password is not null 
    def test_null(self):
        self.assertFalse(verif.password()) # check if password is not null 

# if the string is inf a 10 => not good
    def testInf(self):
        self.assertFalse(verif.password("Ab1$")) # password => "length password" || check if inf of 10
        
# if the string is greater than 20 => not good
    def testSup(self):
        self.assertFalse(verif.password("Ab1$vdifhvvkpdjviohfdvhfdohdhvfhddifv"))   #password => "length password" || check if sup of 20
        
# 1 caractere ($ & % ? @ # )
    def test_specialChar(self):
        self.assertFalse(verif.password("Ab1codshcudhs"))  # password check if number of special character is equal to 5
        
# mini one uppercase
    def test_upper(self):
        self.assertFalse(verif.password("a1saadapda$%&@?"))# check if password have mini one uppercase
        
# mini one lowercase
    def test_lower(self):
        self.assertFalse(verif.password("BONJOURAVOUS1$%&@?"))# check if password have mini one lowercase
        
# mini one number
    def test_number(self):
        self.assertFalse(verif.password("Csqmcyvpba&ss"))  # check if password have mini one number

if __name__ == '__main__':
    unittest.main()