from django.db import models
from cars import models as cmodels
from cloudinary.models import CloudinaryField

# Create your models here.

class Photo(models.Model):
    owner = models.ForeignKey(cmodels.Profile, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True)
    image = CloudinaryField('image')

    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" %(self.title, public_id)