from django.db import models


def image_path(instance, filename):
    return 'news_image/{0}'.format(filename)


# Create your models here.
class NewsArticle(models.Model):
    title = models.TextField(null=False, default="News")
    content = models.TextField(null=False)
    image = models.ImageField(null=True, blank=True, upload_to=image_path)
    premium_content = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.title
