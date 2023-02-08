from django.db import models
from io import BytesIO
from PIL import Image

from django.core.files import File

ONE = "1"
TWO = "2"
THREE = '3'

TIME_CHOICES = [
    (TWO, "Каждые два часа"),
    (ONE, "Каждый час"),
    (THREE, "Каждые три часа"), ]


class Group(models.Model):
    name = models.CharField(max_length=125)
    chat_id = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(max_length=125)
    text = models.CharField(max_length=600)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    enable = models.BooleanField(default=False)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_image(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000/' + self.image.url
        return ''


    # Todo надо добавить сигнал для обновления миниатюры при смене фотографии
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return ''


    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


class Time(models.Model):
    time = models.CharField(max_length=30)

    def __str__(self):
        return str(self.time)


class Manager(models.Model):
    name = models.CharField(max_length=30)
    client_id = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)


class VacancySettings(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    time = models.ManyToManyField(Time)
    manager = models.ManyToManyField(Manager)

    random_time = models.ManyToManyField("RandomTime")

    from_time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name="from_time", null=True)
    to_time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name="to_time", null=True)

    period = models.CharField(
        max_length=20,
        choices=TIME_CHOICES,
        default=ONE,
    )

    last_send_manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name="last_send_manager",
                                          null=True)

    def get_time(self):
        for i in range(self.from_time.id, self.to_time.id + 1, int(self.period)):
            time = Time.objects.get(id=i)
            self.time.add(time)


class RandomTime(models.Model):
    time = models.TimeField(null=True)
