from django.db import models

class Pupil(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='https://img.freepik.com/free-photo/happy-young-female-student-holding-notebooks-from-courses-smiling-camera-standing-spring-clothes-against-blue-background_1258-70161.jpg')
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.name
