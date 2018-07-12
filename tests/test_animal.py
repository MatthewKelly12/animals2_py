import unittest
import sys
sys.path.append('../')
from animals import Animal
from animals import Dog
from decimal import Decimal


class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bob = Dog("Bob")

    def test_animal_creation(self):

        bob = Dog("Bob")

        self.assertIsInstance(bob, Dog)
        self.assertIsInstance(bob, Animal)

    def test_animal_can_set_legs(self):
        self.bob.set_legs(6)
        self.assertEqual(self.bob.legs, 6)

    def test_animal_set_species(self):
        self.bob.set_species("Yorkie Poo")
        self.assertEqual(self.bob.species, "Yorkie Poo")

    def test_animal_get_species(self):
        self.bob.set_species("Yorkie Poo")
        self.bob.get_species()
        self.assertEqual(self.bob.species, "Yorkie Poo")

    def test_animal_speed(self):
        self.bob.set_legs(7)
        self.bob.walk()
        self.assertEqual(self.bob.speed, 1.4)


if __name__=='__main__':
    unittest.main()