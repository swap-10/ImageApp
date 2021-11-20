from django.db import models

# Create your models here.

class Driver(models.Model):
    name = models.TextField()
    license = models.TextField()

class Car(models.Model):
    make = models.TextField()
    model = models.TextField()
    year = models.IntegerField()
    owner = models.ForeignKey("Driver", on_delete=models.SET_NULL, null=True)


class Accounts(models.Model):
    user_id = models.CharField(primary_key=True, max_length=30)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=64)
    mobile_num = models.CharField(max_length=12)
    dob = models.DateField()
    age_catg = models.IntegerField()
    location = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'accounts'

class Users(models.Model):
    user = models.OneToOneField(Accounts, models.DO_NOTHING, primary_key=True)
    user_name = models.CharField(max_length=30)
    user_desc = models.CharField(max_length=200, blank=True, null=True)
    pub_location = models.CharField(max_length=30, blank=True, null=True)
    age_catg = models.IntegerField()
    interests = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

class Albums(models.Model):
    album_id = models.CharField(primary_key=True, max_length=64)
    owner = models.ForeignKey('Users', models.DO_NOTHING)
    album_name = models.CharField(max_length=50)
    tags = models.CharField(max_length=200, blank=True, null=True)
    shared_list = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'albums'


class Friends(models.Model):
    rel_id = models.CharField(primary_key=True, max_length=64)
    origin = models.ForeignKey('Users', models.DO_NOTHING, related_name='friend_origin')
    friend = models.ForeignKey('Users', models.DO_NOTHING, related_name='friend_frienddeets')

    class Meta:
        managed = False
        db_table = 'friends'


class Gallery(models.Model):
    image_id = models.CharField(primary_key=True, max_length=64)
    owner = models.ForeignKey('Users', models.DO_NOTHING)
    size_img = models.FloatField()
    dim_w = models.IntegerField()
    dim_h = models.IntegerField()
    file_type = models.CharField(max_length=30)
    tags = models.CharField(max_length=200, blank=True, null=True)
    shared_list = models.CharField(max_length=500, blank=True, null=True)
    age_catg_allowed = models.IntegerField()
    copyright_status = models.BooleanField()
    album = models.ForeignKey(Albums, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gallery'


class TestTable(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    d_o_b = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'test_table'

