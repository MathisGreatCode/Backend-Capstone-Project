from django.test import TestCase
from .models import MenuItem
from .serializers import MenuItemSerializer

# Create your tests here.
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=8, inventory=100)
        self.assertEqual(str(item), "IceCream : 8")

#class MenuViewTest(TestCase):
#    def setUp(self):
#        self.items = [MenuItem.objects.create(title="Chocolate Cake", price=7, inventory=100),
#                 MenuItem.objects.create(title="Cookies", price=3, inventory=200),
#                 MenuItem.objects.create(title="pancakes", price=8, inventory=100) ]
#
  #  def test_getall(self):
   #     serialized_data = [MenuItemSerializer(item) for item in self.items]
    #    self.assertEqual(serialized_data, MenuItemView(self.items???request?) )