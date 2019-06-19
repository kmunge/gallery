from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.kenya = Location(location = "kenya")

     # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kenya,Location))

    # Testing Save method
    def test_save_method(self):
        self.kenya.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    # Testing Delete method
    def test_delete_method(self):
        self.kenya.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.nature = Category(category = "nature")

     # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nature,Category))

    # Testing Save method
    def test_save_method(self):
        self.nature.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

    # Testing Delete method
    def test_delete_method(self):
        self.nature.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        # Location class test
        self.kenya = Location(location = "kenya")
        self.kenya.save_location()

        # Category class Test
        self.nature = Category(category = "nature")
        self.nature.save_category()
        # Image class Test
        self.image = Image(image = "",name="nature goodness", description = "I love this view", pub_date = "10/2/2019", location = self.kenya, category = self.nature)
        self.image.save_image()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    # Testing Save method
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    # Testing Delete method
    def test_delete_method(self):
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    # Testing getting image by id 
    def test_get_image_by_id(self):
        images = Image.get_image_by_id(self.image.id)
        self.assertTrue(images == self.image)

    # Testing Update method
    def test_update_method(self):
        image = Image.get_image_by_id(self.image.id)
        image.update_image("new_image")
        image = Image.get_image_by_id(self.image.id)
        self.assertTrue(image.image == "new_image")

    # Testing search_image_by_category method
    def test_search_image(self):
        images = Image.search_by_category('Nature')
        self.assertTrue(len(images)>0)
    
