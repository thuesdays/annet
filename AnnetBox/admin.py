from django.contrib import admin
from AnnetBox.models import Album, Client, Image, Slide, TextBlock, Tag, Personal, TypeWork, Award, Ticket, TicketStatus


class AlbumAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "created", "description", "public"]

class ClientAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone", "area", "type_work",
                    "first_visit", "next_visit", "description"]
    search_fields = ["first_name", "last_name", "phone"]

class ImageAdmin(admin.ModelAdmin):
    search_fields = ["client"]
    list_display = ["__unicode__", "client", "rating",  "albums_",  "thumbnail", "done", "public"]
    list_filter = ["albums", "client", "done"]

class SlideAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["__unicode__", "title", "public"]


class TagAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name"]

class TextBlockAdmin(admin.ModelAdmin):
    search_fields = ["tag"]
    list_display = ["tag", "text", "public"]

class TypeWorkAdmin(admin.ModelAdmin):
    search_fields = ["type_work"]
    list_display = ["type_work", "link", "price", "description", "public"]

class AwardAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "link", "thumbnail", "description", "public"]

class SignAdmin(admin.ModelAdmin):
    search_fields = ["type_work","first_name", "last_name"]
    list_display = ["first_name", "last_name", "email", "phone", "description","date", "time","type_work","status"]

class StatusTicketAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name"]

class PersonalAdmin(admin.ModelAdmin):
    search_fields = ["mobile1", "mobile2", "email","skype"]
    list_display = ["thumbnail", "mobile1", "mobile2", "email","skype", "group", "city", "adress1","adress2"]
    list_filter = ["mobile1", "mobile2", "email","skype"]



admin.site.register(Album, AlbumAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(TextBlock, TextBlockAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Personal, PersonalAdmin)
admin.site.register(TypeWork, TypeWorkAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Ticket, SignAdmin)
admin.site.register(TicketStatus, StatusTicketAdmin)