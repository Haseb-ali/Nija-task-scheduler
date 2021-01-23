from django.contrib import admin
from . models import Todos , TodoUserMedia,NotificationsSettings,Feedback,insight
@admin.register(Todos)
class TodosAdmin(admin.ModelAdmin):
    list_display=['todo_id','todo_text','todo_add_date','todo_priporty']
admin.site.register(TodoUserMedia)
@admin.register(NotificationsSettings)
class NotificationsSettingsAdmin(admin.ModelAdmin):
    list_display=['username','task_notifications','task_completedNotifiication','via_email','system_notifications']
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display=['username','title','feedbackmessage']
@admin.register(insight)
class insightAdmin(admin.ModelAdmin):
    list_display=['username','logins','changeusername','changepassword','addtasks','deletetasks','edittasks','completetask','searchtask','mostsearchkeywords','date']