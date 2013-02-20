# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Pagina, Persona, ArchivoAdjunto
from django.core.mail import EmailMessage 

class AdminArchivoAdjunto(admin.StackedInline):
    model = ArchivoAdjunto
    extra = 0

class PaginaAdmin(admin.ModelAdmin):
    list_display = ('codigo','asunto','creador',)
    list_display_links = ('codigo','asunto',)
    exclude = ['creador']
    inlines = [
        AdminArchivoAdjunto,
    ]

    class Media:        
        js = ("grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js",
        	#"grappelli/tinymce_setup/tinymce_setup.js")
        	"js/jscontenido.js")

    def save_related(self, request, form, formsets, change):        
        super(PaginaAdmin,self).save_related(request,form, formsets, change)        
        mails = Persona.objects.values_list('email', flat=True).order_by('email')
        email = EmailMessage(subject=self.obj.asunto,
            body=self.obj.contenido,
            bcc=mails,)
        for archivo in self.obj.archivos.all():
            email.attach_file(archivo.archivo.path)
        email.content_subtype = "html"
        email.send()

    def save_model(self, request, obj, form, change):        
        obj.creador = request.user        
        obj.save()    
        self.obj = obj

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombres','email',)
    list_display_links = ('codigo','nombres',)    

admin.site.register(Pagina,PaginaAdmin)
admin.site.register(Persona,PersonaAdmin)