from django.db import models
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from PyDictionary import PyDictionary

class VocabManager(models.Manager):

    def create_word(self,word,usage,book):
        wordobj = self.create(word=word[3:],usage=usage,book=book)
        return wordobj

class Vocab(models.Model):
    word = models.CharField("Word", max_length=255, default='undefined')
    usage = models.CharField("Context", max_length=2000, default='undefined')
    definition = models.CharField("Definition", max_length=2000, default='undefined')
    book = models.CharField("Book", max_length=255, default='undefined')
    prevent_cull = models.BooleanField(default=False)
    objects = VocabManager()

    def __str__(self):
        return self.word

