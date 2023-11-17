from django.db import models



class Variant(models.Model):
    number=models.IntegerField(default=0)
    theme=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    themeNumber=models.IntegerField(default=0)
    tText=models.TextField(null=False, blank=True)
    tAnswer=models.IntegerField(default=0)
    tMod=models.DateTimeField(auto_now_add=True)
    variants=models.ManyToManyField(Variant,related_name="tasks")

    def __str__(self):
        return f"Задание(pk={self.pk}, название= {self.name!r})"