from django.db import models


class climateData(models.Model):
    _id = models.AutoField(
        primary_key=True,
        unique=True,
        auto_created=True,
    )
    Time = models.DateTimeField("Time", max_length=32)
    Device_ID = models.CharField("Device ID", max_length=16)
    Device_Name = models.CharField("Device Name", max_length=64)
    Latitude = models.FloatField("Latitude")  # , max_length=16)
    Longitude = models.FloatField("Longitude")  # , max_length=16)
    Location = models.CharField("Location", max_length=32)
    TTN_metadata = models.TextField("TTN metadata")  # , max_length=255)
    TTN_payload_fields = models.TextField("TTN payload fields")  # , max_length=255)
    Temperature_C = models.FloatField("Temperatures (°C)")  # , max_length=5)
    Atmospheric_Pressure_kPa = models.FloatField(
        "Atmospheric Pressure (kPa)"
    )  # , max_length=5

    Lightning_Average_Distance_km = models.FloatField(
        "Lightning Average Distance (km)"
    )  # , max_length=9

    Lightning_Strike_Count = models.FloatField(
        "Lightning Strike Count"
    )  # , max_length=3)
    Maximum_Wind_Speed_ms = models.FloatField(
        "Maximum Wind Speed (m/s)"
    )  # , max_length=5

    Precipitation_mmH = models.FloatField("Precipitation mm/h")  # , max_length=9)
    Solar_Radiation_Wm2 = models.FloatField("Solar Radiation (W/m2)")  # , max_length=9)
    Vapor_Pressure_kPa = models.FloatField("Vapor Pressure (kPa)")  # , max_length=9)
    Humidity = models.FloatField("Humidity (%)")  # , max_length=9)
    Wind_Direction = models.FloatField("Wind Direction (°)")  # , max_length=9)
    Wind_Speed_ms = models.FloatField("Wind Speed (m/s)")  # , max_length=9)

    def __str__(self):
        return self.Device_ID

    def save(self, *args, **kwargs):
        if not self.pk:
            # check the maximum _id value in the database
            max_id = climateData.objects.aggregate(models.Max("_id"))["_id__max"]
            if max_id is None:
                max_id = 0
            # set the _id value of the new object to be max_id + 1
            self._id = max_id + 1
        super().save(*args, **kwargs)


# def __str__(self):
# return self.Device_Name
# return self.time + ' ' + self.deviceName + ' ' + self.deviceId + ' ' + self.latitude + ' ' + self.longitude + ' ' + self.location + ' ' + self.ttnPayloadFields + ' ' + self.temperature + ' ' + self.atmosPressure + ' ' + self.lightningDistance + ' ' + self.lightningCount + ' ' + self.maxWindSpeed + ' ' + self.precipitation + ' ' + self.radiation + ' ' + self.vaporPressure + ' ' + self.humidity + ' ' + self.name + ' ' +  ' ' + self.windDirection + ' ' + self.windSpeed
