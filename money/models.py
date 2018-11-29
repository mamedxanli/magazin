#Django native imports
from django.db import models
from django.urls import reverse, reverse_lazy

# Import from our apps

class Money(models.Model):
    # Timestamps
    date = models.DateTimeField("Дата")
    amount = models.DecimalField("Продажа за день", decimal_places=2, max_digits=5)
    
    def __str__(self):
        return " {} ".format(self.date)

    def get_absolute_url(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('money_edit', args=[str(self.pk)])

    def get_detail(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('money_detail', args=[str(self.pk)])

    def get_delete(self):
        """
        Handy way of getting the url of the object to its delete view page
        """
        return reverse('money_delete', args=[str(self.pk)])

    def get_class(self):
        """
        Handy way of getting the class of the object for the html templates
        """
        class_name = "Выручка"
        return class_name

    class Meta:
        verbose_name_plural = "Money"
