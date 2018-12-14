from django.db import models
from django.urls import reverse, reverse_lazy
# Create your models here.

class Expence(models.Model):
    # Timestamps
    date = models.DateTimeField("Дата")
    amount = models.DecimalField("Расход за день", decimal_places=2, max_digits=5)
    purpose = models.CharField("Назначение", max_length=100, default=None)
    
    def __str__(self):
        return " {} ".format(self.date)

    def get_absolute_url(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('expence_edit', args=[str(self.pk)])

    def get_detail(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('expence_detail', args=[str(self.pk)])

    def get_delete(self):
        """
        Handy way of getting the url of the object to its delete view page
        """
        return reverse('expence_delete', args=[str(self.pk)])

    def get_class(self):
        """
        Handy way of getting the class of the object for the html templates
        """
        class_name = "Расход"
        return class_name

    class Meta:
        verbose_name_plural = "Expences"
