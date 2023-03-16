You can test the API for the menu items here:

restaurant/menu/
restaurant/menu/<int:pk>

To get a token go to: auth/token/login
use 'testuser' as username and 'ThisIsPassword' as password to obtain a token (or create a new user by goin to 'auth/users')

You can test the API for the bookings in Insomnia (don't forget to enter the user token):
restaurant/bookings
restaurant/bookings/<int:pk>