from django.db import models


class stations(models.Model):
    _id = models.AutoField(
        primary_key=True,
        unique=True,
        auto_created=True,
    )
    deviceName = models.CharField("deviceName", max_length=64)
    deviceID = models.CharField("deviceID", max_length=16)
    latitude = models.FloatField("latitude")  # , max_length=16)
    longitude = models.FloatField("longitude")  # , max_length=16)
    location = models.CharField("location", max_length=32)
    state = models.CharField("state", max_length=16)
    lastReading = models.DateField("lastReading", max_length=32)
    newStation = models.BooleanField("newStation", max_length=5)

    def __str__(self):
        return self.deviceName

    def save(self, *args, **kwargs):
        if not self.pk:
            # check the maximum _id value in the database
            max_id = stations.objects.aggregate(models.Max("_id"))["_id__max"]
            if max_id is None:
                max_id = 0
            # set the _id value of the new object to be max_id + 1
            self._id = max_id + 1
        super().save(*args, **kwargs)
