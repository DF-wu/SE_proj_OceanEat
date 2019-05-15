from django.contrib import admin
from mysite import models

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('nickname', 'message', 'enabled', 'pub_time')
	#order_by('-pub_time',)

admin.site.register(models.User)
admin.site.register(models.Mood)
admin.site.register(models.Post, PostAdmin)


