from django.db import models
from user.models import User


# Create your models here.


class Board(models.Model):

    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    hit = models.IntegerField(default=0)
    regdate = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Board(%s, %s, %d, %s, %d)" % \
               (self.title, self.content, self.hit, str(self.regdate), self.user.id)
