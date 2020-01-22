from django.db import models

# Create your models here.
class Message(models.Model):
    user = models.CharField("留言者", max_length=50)
    subject = models.CharField("留言主題", max_length=200)
    content = models.TextField("留言內容")
    publication_date = models.DateTimeField("留言日期", auto_now=False, auto_now_add=True)

    def __str__(self):
        return '{}:{}'.format(self.user, self.subject)