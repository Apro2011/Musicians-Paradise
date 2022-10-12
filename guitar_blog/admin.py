from django.contrib import admin


from .models import Musician


# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    model = Musician
    exclude = ("music_1_votes", "music_2_votes", "music_3_votes", "music_1_users",
                        "music_2_users", "music_3_users",)


admin.site.register(Musician, MyModelAdmin)



