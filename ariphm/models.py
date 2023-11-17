from django.db import models



class Variant(models.Model):
    number=models.IntegerField(default=0)
    theme=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(null=False, blank=True)
    answer=models.IntegerField(default=0)
    variants=models.ManyToManyField(Variant,related_name="tasks")

    def __str__(self):
        return f"Задание(pk={self.pk}, название= {self.name!r})"

class taskList(models.Model):
    varNumber=models.IntegerField(default=0)
    number=models.IntegerField(default=0)
    text=models.TextField(null=False, blank=True)
    answer=models.IntegerField(default=0)
    succ=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Задание(pk={self.pk}, название= {self.name!r})"
