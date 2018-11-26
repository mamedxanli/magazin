#Django native imports
from django.db import models
from django.urls import reverse, reverse_lazy

# Import from our apps

def save_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/clothes/<code>/<filename>
    return '{0}/{1}/{2}'.format("clothes", instance.code, filename)

class Clothes(models.Model):
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, default=None)

    # Model
    code = models.IntegerField("Код", primary_key=True)
    brand = models.CharField("Бренд", max_length=20, default=None)
    category = models.CharField("Категория", max_length=30, default=None)
    description = models.CharField("Описание", max_length=100, default=None)
    purchase_price = models.DecimalField("Закупочная цена", decimal_places=2, max_digits=5)
    selling_price = models.DecimalField("Цена продажи", decimal_places=2, max_digits=5)
    discount = models.DecimalField("Скидка", decimal_places=2, max_digits=5, default=0)
    size = models.CharField("Размер", max_length=5, default=None)
    quantity = models.IntegerField("Количество", default=1)
    image = models.FileField("Фото",blank=True, default=None, upload_to=save_directory_path)
    #image2 = models.FileField("Picture 2",blank=True, default=None, upload_to=save_directory_path)
    #somefile = models.FileField("Some file",blank=True, default=None, upload_to=save_directory_path)
    sold = models.BooleanField("Продано", default=False)

    def __str__(self):
        return " {} ".format(self.code)

    def get_absolute_url(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('clothes_edit', args=[str(self.pk)])

    def get_detail(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('clothes_detail', args=[str(self.pk)])

    def get_delete(self):
        """
        Handy way of getting the url of the object to its delete view page
        """
        return reverse('clothes_delete', args=[str(self.pk)])

    def get_class(self):
        """
        Handy way of getting the class of the object for the html templates
        """
        class_name = "Clothes"
        return class_name

    class Meta:
        verbose_name_plural = "Clothes"
