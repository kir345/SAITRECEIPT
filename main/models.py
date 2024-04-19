from django.db import models
from autoslug import AutoSlugField
from django.shortcuts import reverse

class Topic(models.Model):
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from="title")

    def __str__(self):
        return self.title

class Receipt(models.Model):
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from="title")
    image = models.CharField(max_length=400)
    description = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()
    servings = models.CharField(max_length=5)
    time = models.CharField(max_length=5)
    calories = models.CharField(max_length=5)
    fat = models.CharField(max_length=5)
    carbs = models.CharField(max_length=5)
    protein = models.CharField(max_length=5)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # def get_url(self):
    #     return reverse("detail", kwargs={
    #         "slug":self.slug,
    #     }) 
    def get_absolute_url(self):
        return reverse('detail:detail', kwargs={"slug": self.slug,})
    