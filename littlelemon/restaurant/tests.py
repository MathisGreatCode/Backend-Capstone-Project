from django.test import TestCase
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer
import datetime

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

class BookingTest(TestCase):
    def test_get_item(self):
        self.item = Booking.objects.create(name = "Henry", no_of_guests = 9, date= datetime.date(2023, 3, 29 ))
        self.assertEqual(str(self.item), "Henry's reservation for 9 guests on 2023-03-29")