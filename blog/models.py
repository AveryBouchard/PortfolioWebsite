from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def summary(self):
        return self.body[:100] + "..."

    def __str__(self):
        return self.title
