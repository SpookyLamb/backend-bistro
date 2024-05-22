import os
import django
from django.conf import settings
# Use this by running:
# python standalone_script.py
os.environ["DJANGO_SETTINGS_MODULE"] = "django_restaurant.settings"
django.setup()
# Now you have django, so you can import models and do stuff as normal
### NOTE
# DO NOT CHANGE CODE ABOVE THIS LINE
# WORK BELOW

# Must Have
    # All restaurant data served from the backend API

# Should Have
    # Add the ability to enter an order for pickup
        # Add foods with quantities
        # Marking order as complete
        # Track order by customer

# Could Have
    # Expanded order functionality
        # Group order - label order items with “tag” or “name” of person in a group order  - example:  first person ordered ‘x, y, z’, second person ordered ‘a, b, c’
        # Handle delivery in addition to pickup
            # Add service charge to price
            # Show address on map
            # Customer can add delivery instructions
        # Select spiciness level for each food
        # Allow customer to make notes about each food item
    # Customer Reviews

# Wish List
    # ETA for Delivery based on location/time of day.
    # Driver’s Table so you can see who is delivering your order
        # Ratings for driver(s)
    # Customer can save multiple addresses (home/work) for delivery
    # Some items only available for pickup || delivery || in person.
