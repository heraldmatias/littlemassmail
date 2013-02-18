# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Pagina, Persona
from django.core.mail import EmailMessage 

class PaginaAdmin(admin.ModelAdmin):
    list_display = ('codigo','asunto','creador',)
    list_display_links = ('codigo','asunto',)
    exclude = ['creador']

    class Media:        
        js = ("grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js",
        	#"grappelli/tinymce_setup/tinymce_setup.js")
        	"js/jscontenido.js")

    def save_model(self, request, obj, form, change):
        obj.creador = request.user
        mails = Persona.objects.values_list('email', flat=True).order_by('email')
        email = EmailMessage(subject=obj.asunto,
            body=obj.contenido,
            bcc=mails,)
            #headers = {'Reply-To': 'portalpresidenciaperu@gmail.com'})
        email.content_subtype = "html"
        email.send()
        obj.save()

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombres','email',)
    list_display_links = ('codigo','nombres',)    

admin.site.register(Pagina,PaginaAdmin)
admin.site.register(Persona,PersonaAdmin)