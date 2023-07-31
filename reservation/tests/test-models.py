from django.test import TestCase
from reservation.models import Menu

class MenuTest(TestCase):
    def test_get_tem(self):
        item = Menu.objects.create(title ="Flan", price = 20, inventory = 95)
        self.assertEqual(item, "Flan: 20")