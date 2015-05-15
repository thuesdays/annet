# -*- coding: UTF-8 -*-
from django.db import models
from PIL import Image as PImage
from django.dispatch import receiver
from annet.settings import MEDIA_ROOT
import os


class Album(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    public = models.BooleanField(default=False)

    def images(self):
        lst = [x.image.name for x in self.image_set.all()]
        lst = ["<a href='/media/works/%s'>%s</a>" % (x, x.split('/')[-1]) for x in lst]
        return ''.join([lst, ', '])

    images.allow_tags = True

    def __unicode__(self):
        return self.title


class Client(models.Model):

    MANIKUR = 'MK'
    PEDIKUR = 'PK'
    NARACH = 'NR'
    GELLAK = 'GL'
    FRENCH = 'FR'

    GOLOSEEVSKIY = 'GO'
    SVYATOSHUN = 'SV'
    SOLOMEN = 'SO'
    OBOLON = 'OB'
    PODOL = 'PO'
    PECHERSK = 'PC'
    SHEVCHEN = 'SH'
    DARNIC = 'DR'
    DESNYAN = 'DS'
    DNEPROV = 'DN'

    SELECT_AREA = ((GOLOSEEVSKIY, 'Голосеевский'),
                   (SVYATOSHUN, 'Святошинский'),
                   (SOLOMEN, 'Соломенский'),
                   (OBOLON, 'Оболонский'),
                   (PODOL, 'Подольский'),
                   (PECHERSK, 'Печерский'),
                   (SHEVCHEN, 'Шевченковский'),
                   (DARNIC, 'Дарницкий'),
                   (DESNYAN, 'Днепровский'),
                   (DNEPROV, 'Деснянский'))

    SELECT_TYPE_WORK = ((MANIKUR, 'Маникюр'),
                        (PEDIKUR, 'Педикюр'),
                        (NARACH, 'Наращивание гелем'),
                        (GELLAK, 'Гель-лак'),
                        (FRENCH, 'Френч'))

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=20)
    area = models.CharField(max_length=30, choices=SELECT_AREA)
    type_work = models.CharField(max_length=30, choices=SELECT_TYPE_WORK)
    first_visit = models.DateTimeField()
    next_visit = models.DateTimeField()
    description = models.TextField()

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


class Image(models.Model):
    image = models.FileField(upload_to="works")
    albums = models.ManyToManyField(Album, blank=True)
    done = models.DateTimeField()
    rating = models.IntegerField(default=80)
    client = models.ForeignKey(Client, null=True, blank=True)
    public = models.BooleanField()

    def save(self, *args, **kwargs):
        """Save image dimensions."""
        super(Image, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.image.name

    def albums_(self):
        list = []
        for x in self.albums.all():
            list.append(x.title)
        return ', '.join(list)


    def thumbnail(self):
        return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % (
            (self.image.name, self.image.name))

    thumbnail.allow_tags = True


class Slide(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    slide = models.FileField(upload_to="slide")
    public = models.BooleanField()

    def save(self, *args, **kwargs):
        """Save image dimensions."""
        super(Slide, self).save(*args, **kwargs)
        imageObj = PImage.open(MEDIA_ROOT + '/' + self.slide.name)
        imageObj = imageObj.resize((1024, 521), PImage.ANTIALIAS)
        imageObj.save(MEDIA_ROOT + '/' + self.slide.name)


    def __unicode__(self):
        return self.slide.name

    def images(self):
        lst = [x.image.name for x in self.image_set.all()]
        lst = ["%s" % (x for x in lst)]
        return ''.join([lst, ', '])

    images.allow_tags = True


class Tag(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)

    def __unicode__(self):
        return self.name


class TextBlock(models.Model):
    text = models.TextField()
    tag = models.ForeignKey(Tag, null=False, blank=False)
    public = models.BooleanField()

    def __unicode__(self):
        return self.text


class Personal(models.Model):
    photo = models.ImageField(upload_to="personal")
    mobile1 = models.CharField(max_length=20)
    mobile2 = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=40)
    group = models.TextField(max_length=80, null=True, blank=True)
    skype = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=20)
    adress1 = models.TextField(max_length=100)
    adress2 = models.TextField(max_length=80, null=True, blank=True)

    def __unicode__(self):
        return '%s %s %s' % (self.city, self.adress1, self.mobile1)

    def thumbnail(self):
        return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % (
            (self.photo.name, self.photo.name))

    thumbnail.allow_tags = True

    def save(self, *args, **kwargs):
        """Save image dimensions."""
        super(Personal, self).save(*args, **kwargs)
        imageObj = PImage.open(MEDIA_ROOT + '/' + self.photo.name)
        imageObj = imageObj.resize((200, 220), PImage.ANTIALIAS)
        imageObj.save(MEDIA_ROOT + '/' + self.photo.name)


class TypeWork(models.Model):
    type_work = models.CharField(max_length=60)
    link = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField()
    description = models.TextField(max_length=460, null=True, blank=True)
    public = models.BooleanField()

    def __unicode__(self):
        return '%s' % (self.type_work)


class Client(models.Model):

    GOLOSEEVSKIY = 'GO'
    SVYATOSHUN = 'SV'
    SOLOMEN = 'SO'
    OBOLON = 'OB'
    PODOL = 'PO'
    PECHERSK = 'PC'
    SHEVCHEN = 'SH'
    DARNIC = 'DR'
    DESNYAN = 'DS'
    DNEPROV = 'DN'

    SELECT_AREA = ((GOLOSEEVSKIY, 'Голосеевский'),
                   (SVYATOSHUN, 'Святошинский'),
                   (SOLOMEN, 'Соломенский'),
                   (OBOLON, 'Оболонский'),
                   (PODOL, 'Подольский'),
                   (PECHERSK, 'Печерский'),
                   (SHEVCHEN, 'Шевченковский'),
                   (DARNIC, 'Дарницкий'),
                   (DESNYAN, 'Днепровский'),
                   (DNEPROV, 'Деснянский'))

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=20)
    area = models.CharField(max_length=30, choices=SELECT_AREA)
    type_work = models.ForeignKey(TypeWork, null=True, blank=True)
    first_visit = models.DateTimeField()
    next_visit = models.DateTimeField()
    description = models.TextField()

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

class Award(models.Model):
    name = models.CharField(max_length=150)
    link = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(upload_to="personal", null=True, blank=True)
    description = models.TextField(max_length=460, null=True, blank=True)
    public = models.BooleanField()

    def thumbnail(self):
        return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % (
            (self.photo.name, self.photo.name))

    thumbnail.allow_tags = True

    def __unicode__(self):
        return '%s %s' % (self.name, self.link)


@receiver(models.signals.post_delete, sender=Slide)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.slide:
        if os.path.isfile(instance.slide.path):
            os.remove(instance.slide.path)

    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

class TicketStatus(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Ticket(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=40, null=True, blank=True)
    phone = models.CharField(max_length=20)
    type_work = models.ForeignKey(TypeWork, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    viewed = models.BooleanField()
    status = models.ForeignKey(TicketStatus)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name+ ' ' + self.phone

