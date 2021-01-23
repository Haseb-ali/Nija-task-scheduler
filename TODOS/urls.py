from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.loadTodos,name='loadTodos'),
    path('tomorrow',views.loadTomorrowTodos),
    path('alltask',views.allTodos),
    path('addtodo',views.addTodos,name="addtodo"),
    path('action',views.action,name='action'),
    path('savechanges',views.saveEdit,name="saveEdit"),
    path('login',views.login,name="login"),
    path('registration',views.register,name="register"),
    path('fetchall',views.getAll,name="fetchall"),
    path('fetchrecord',views.fetchRecord,name="fetchrecord"),
    path('setSession',views.setSession,name="setSession"),
    path('deleteSession',views.deleteSession,name="deleteSessiom"),
    path('getprfiledata',views.getProfileData,name="getprfiledata"),
    path('getloginrs',views.returnBackLoginMessages,name="getloginrs"),
    path('updateinfo',views.updateInfo,name="updateinfo"),
    path('changepassword',views.changePassword,name="changePassword"),
    path('updateusername',views.updateUsername,name="updateusername"),
    path('updatetasknot',views.updateTaskNotification,name="updatetasknot"),
    path('getNote',views.getNote,name="getNote"),
    path('savefeedback',views.saveFeedBack,name="savefeedback"),
    path('setCompleted',views.setCompleted,name="setCompleted"),
    path("completed_tasks",views.getCompleted,name="completed_tasks"),
    path('completeaction',views.completeaction),
    path('tomorrowaction',views.tomorrowaction),
    path('allaction',views.allaction),
    path("Xday",views.loadXday,name="loadXday"),
    path('search',views.search),
    path('Insights',views.InsightData),
    path('insightsdataset',views.insightsdataset),    
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
