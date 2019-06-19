from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length = 30)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()
    
    def delete_location(self):
        Location.objects.filter().delete()

    @classmethod
    def get_location(cls):
        found_location = cls.objects.all()
        return found_location


class Category(models.Model):
    category = models.CharField(max_length = 30)
    
    @classmethod
    def get_categories(cls):
        category = cls.objects.all()
        return category

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()
    
    def delete_category(self):
        Category.objects.filter().delete()


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 30)
    description = models.TextField(max_length = 60)
    pub_date = models.DateTimeField(auto_now_add = True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)


    @classmethod
    def get_images(cls):
        image = cls.objects.all()
        return image

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__category__icontains = search_term)
        return images
    
    @classmethod
    def filter_by_location(cls,location):
        images = Image.objects.filter(id = location)
        return images

    def save_image(self):
        self.save()

    def delete_image(self):
        Image.objects.filter().delete()

    def update_image(self, update):
        self.image = update
        self.save()

    @classmethod
    def get_image_by_id(cls, id):
        found_image = Image.objects.get(id=id)
        return found_image

    class Meta:
        ordering = ['image']



