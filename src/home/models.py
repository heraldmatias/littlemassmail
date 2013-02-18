# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Pagina(models.Model):
    codigo = models.AutoField(primary_key=True)    
    asunto = models.CharField(verbose_name='Asunto', max_length=150)    
    contenido = models.TextField(verbose_name='Contenido del mensaje')    
    creador = models.ForeignKey(User)

    def __unicode__(self):
    	return u'%s' % self.asunto
    
    def emails(self):
        print self.mails.split(',')
        return self.mails.split(',')

    class Meta:
    	verbose_name = 'Mensaje'
    	verbose_name_plural = 'Mensajes'

class Persona(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)

    def  __unicode__(self):
        return u'%s' % self.nombres

    class Meta:
        verbose_name = 'Destinatario'
        verbose_name_plural = 'Destinatarios'