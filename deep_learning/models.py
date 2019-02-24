from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# # Later On Comments
class DeepLearning(models.Model):
    title = models.CharField(max_length = 255)
    post_date = models.DateTimeField()
    # Add format toolbar from bootcamp project
    code = models.TextField()
    body = models.TextField()
    output = models.ImageField(upload_to = 'images/')
    url = models.TextField()
    downloads = models.IntegerField(default = 0)
    site_user = models.ForeignKey(User,on_delete=models.CASCADE)
    def summary(self):
        return self.body[:100]
    def pub_date_pretty(self):
        return self.post_date.strftime('%b %e %Y')
    def __str__(self):
        return self.title
