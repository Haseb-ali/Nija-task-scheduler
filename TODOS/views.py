from django.contrib.messages.api import get_messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, response,JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Todos,TodosSerializer,TodoUserMedia,NotificationsSettings,Feedback,insight,insightserializer
import random
import json
import sys
from datetime import datetime, timedelta
from .form import ImageForm
def allTodos(request):
    is_userAuth=False;
    fullname=""
    username=""
    todos=""
    todayDate= datetime.now().strftime("%a / %d / %m / %y");

    userProfileImage=TodoUserMedia.objects.get(username="haseebali")
    print(userProfileImage.profile.url)
    if request.session.has_key('loginToken'):
        is_userAuth=True
        userData=User.objects.get(username=request.session['loginToken'])
        fullname=userData.first_name
        username=userData.username
        todos=Todos.objects.filter(author=request.session['loginToken'] ).order_by('-todo_add_time')
        
    return render(request,"all_todos.html",{'todos':todos,'is_userAuth':is_userAuth,'fullname':fullname,'prfileImage':userProfileImage.profile.url,'username':username,'todayDate':todayDate})
def getCompleted(request):
    is_userAuth=False;
    fullname=""
    username=""
    todos=""
    todayDate= datetime.now().strftime("%a / %d / %m / %y");
    
    userProfileImage=TodoUserMedia.objects.get(username="haseebali")
    print(userProfileImage.profile.url)
    if request.session.has_key('loginToken'):
        is_userAuth=True
        userData=User.objects.get(username=request.session['loginToken'])
        fullname=userData.first_name
        username=userData.username
        todos=Todos.objects.filter(author=request.session['loginToken'],todo_status="completed" ).order_by('-todo_add_time')
        
    return render(request,"complete_todos.html",{'todos':todos,'is_userAuth':is_userAuth,'fullname':fullname,'prfileImage':userProfileImage.profile.url,'username':username,'todayDate':todayDate})
def loadTodos(request):
    is_userAuth=False;
    fullname=""
    username=""
    todos=""
    todayDate= datetime.now().strftime("%a / %d / %m / %y");
    
    userProfileImage=TodoUserMedia.objects.get(username="haseebali")
    print(userProfileImage.profile.url)
    if request.session.has_key('loginToken'):
        is_userAuth=True
        userData=User.objects.get(username=request.session['loginToken'])
        fullname=userData.first_name
        username=userData.username
        todos=Todos.objects.filter(author=request.session['loginToken'] ,todo_add_date=datetime.today().strftime('%Y-%m-%d')).order_by('-todo_add_time')
        
    return render(request,"TODOS.html",{'todos':todos,'is_userAuth':is_userAuth,'fullname':fullname,'prfileImage':userProfileImage.profile.url,'username':username,'todayDate':todayDate})
def loadXday(request):
    is_userAuth=False;
    fullname=""
    username=""
    todos=""
    xday=request.GET['xday']
    todayDate= datetime.now().strftime("%a / %d / %m / %y");
    
    userProfileImage=TodoUserMedia.objects.get(username="haseebali")
    print(userProfileImage.profile.url)
    if request.session.has_key('loginToken'):
        is_userAuth=True
        userData=User.objects.get(username=request.session['loginToken'])
        fullname=userData.first_name
        username=userData.username
        todos=Todos.objects.filter(author=request.session['loginToken'] ,todo_add_date=xday).order_by('-todo_add_time')
        
    return render(request,"TODOS.html",{'todos':todos,'is_userAuth':is_userAuth,'fullname':fullname,'prfileImage':userProfileImage.profile.url,'username':username,'todayDate':todayDate})   
def loadTomorrowTodos(request):
    is_userAuth=False;
    fullname=""
    username=""
    todos=""
    todayDate= datetime.now().strftime("%a / %d / %m / %y");
    
    userProfileImage=TodoUserMedia.objects.get(username="haseebali")
    print(userProfileImage.profile.url)
    if request.session.has_key('loginToken'):
        is_userAuth=True
        userData=User.objects.get(username=request.session['loginToken'])
        fullname=userData.first_name
        username=userData.username
        tomorrow=datetime.today()+timedelta(1)
        todos=Todos.objects.filter(author=request.session['loginToken'] ,todo_add_date=tomorrow.strftime('%Y-%m-%d')).order_by('-todo_add_time')
        
    return render(request,"tomorrow_todos.html",{'todos':todos,'is_userAuth':is_userAuth,'fullname':fullname,'prfileImage':userProfileImage.profile.url,'username':username,'todayDate':todayDate})
        
def action(request):
    todoId=request.GET['todoId']
    response_back=""    
    Todos.objects.filter(todo_id=todoId).delete()
    insight_obj=insight.objects.filter(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d')) 
    if len(insight_obj)!=0:
            insight_objr=insight.objects.get(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d'))
            previous=insight_objr.deletetasks
            previous+=1
            insight_objr.deletetasks=previous
            insight_objr.save()
    else:
            try:
                insight.objects.create(username=request.session['loginToken'],deletetasks=1,date=datetime.now().strftime('%Y-%m-%d'))
            except:
                pass

    print(request.path)
    return redirect('/')    
def completeaction(request):
    print(request.path)
    todoId=request.GET['todoId']
    response_back=""    
    Todos.objects.filter(todo_id=todoId).delete()
    insight_obj=insight.objects.filter(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d')) 
    if len(insight_obj)!=0:
            insight_objr=insight.objects.get(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d'))
            previous=insight_objr.deletetasks
            previous+=1
            insight_objr.deletetasks=previous
            insight_objr.save()
    else:
            try:
                insight.objects.create(username=request.session['loginToken'],deletetasks=1,date=datetime.now().strftime('%Y-%m-%d'))
            except:
                pass
    return redirect('/completed_task')
def tomorrowaction(request):
    print(request.path)
    todoId=request.GET['todoId']
    response_back=""    
    Todos.objects.filter(todo_id=todoId).delete()
    insight_obj=insight.objects.filter(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d')) 
    if len(insight_obj)!=0:
            insight_objr=insight.objects.get(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d'))
            previous=insight_objr.deletetasks
            previous+=1
            insight_objr.deletetasks=previous
            insight_objr.save()
    else:
            try:
                insight.objects.create(username=request.session['loginToken'],deletetasks=1,date=datetime.now().strftime('%Y-%m-%d'))
            except:
                pass

    return redirect('/tomorrow')

def allaction(request):
    print(request.path)
    todoId=request.GET['todoId']
    response_back=""    
    Todos.objects.filter(todo_id=todoId).delete()
    insight_obj=insight.objects.filter(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d')) 
    if len(insight_obj)!=0:
            insight_objr=insight.objects.get(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d'))
            previous=insight_objr.deletetasks
            previous+=1
            insight_objr.deletetasks=previous
            insight_objr.save()
    else:
            try:
                insight.objects.create(username=request.session['loginToken'],deletetasks=1,date=datetime.now().strftime('%Y-%m-%d'))
            except:
                pass

    return redirect('/alltask')

def addTodos(request):
    todoText=request.GET['todoText']
    todo_priority=request.GET['todo_priority']
    added_time=request.GET['dotime']
    todoId=random.randrange(10*int(ord(todoText[random.randrange(len(todoText))])))
    added_date=request.GET['deadline']
    print(request.GET['deadline'])
    Todos.objects.create(todo_id=todoId,todo_text=todoText,todo_add_date=added_date,todo_priporty=todo_priority,todo_add_time=added_time,author=request.session['loginToken'])
    insight_obj=insight.objects.filter(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d')) 
    if len(insight_obj)!=0:
            insight_objr=insight.objects.get(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d'))
            previous=insight_objr.addtasks
            previous+=1
            insight_objr.addtasks=previous
            insight_objr.save()
    else:
            try:
                insight.objects.create(username=request.session['loginToken'],addtasks=1,date=datetime.now().strftime('%Y-%m-%d'))
            except:
                pass
    return redirect('/')

def search(request):
    is_userAuth=False;
    fullname=""
    username=""
    todos=""
    todayDate= datetime.now().strftime("%a / %d / %m / %y");
    userProfileImage=TodoUserMedia.objects.get(username="haseebali")
    print(userProfileImage.profile.url)
    if request.session.has_key('loginToken'):
        is_userAuth=True
        userData=User.objects.get(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d'))
        fullname=userData.first_name
        username=userData.username
        todos=Todos.objects.filter(author=request.session['loginToken'] ,todo_text__contains=request.GET['keyword'])
        insight_obj=insight.objects.filter(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d')) 
        if len(insight_obj)!=0:
            insight_objr=insight.objects.get(username=request.session['loginToken'])
            previous=insight_objr.searchtask
            previous+=1
            insight_objr.searchtask=previous
            insight_objr.save()
        else:
            try:
                insight.objects.create(username=request.session['loginToken'],searchtask=1,date=datetime.now().strftime('%Y-%m-%d'))
            except:
                pass
            
    return render(request,"TODOS.html",{'todos':todos,'is_userAuth':is_userAuth,'fullname':fullname,'prfileImage':userProfileImage.profile.url,'username':username,'todayDate':todayDate})
def saveEdit(request):
    todoId=request.GET['todo_id']
    update_todoText=request.GET['todo_text']
    todo_priority=request.GET['todo_priporty']
    update_time=datetime.now().date()
    try:
        todo=Todos.objects.get(todo_id=int(todoId))
        todo.todo_text=update_todoText
        todo.todo_priporty=todo_priority
        todo.todo_updated_time=update_time
        todo.save()
        insight_obj=insight.objects.filter(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d')) 
        if len(insight_obj)!=0:
            insight_objr=insight.objects.get(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d'))
            previous=insight_objr.edittasks
            previous+=1
            insight_objr.edittasks=previous
            insight_objr.save()
        else:
            try:
                insight.objects.create(username=request.session['loginToken'],edittasks=1,date=datetime.now().strftime('%Y-%m-%d'))
            except:
                pass

        return HttpResponse("Record successfully updated")
    except:
        return HttpResponse("Record not update")
    
def login(request):
    useremail=request.POST.get('lguseremail')
    password=request.POST.get('lgpassword')
    try:
        res=User.objects.get(username=useremail,password=password)
        request.session['loginToken']=useremail
        with open("DjangoTODOAPP\logs\system_logs.txt","a") as fr:
            fr.write("login Successfully"+" "+str(datetime.now())+"\n")
        insight_obj=insight.objects.filter(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d')) 
        print(len(insight_obj))
        if len(insight_obj)!=0:
            insight_objr=insight.objects.get(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d'))
            previous=insight_objr.logins
            previous+=1
            insight_objr.logins=previous
            insight_objr.save()
            print("here")
            
        else:
            try:
                insight.objects.create(username=request.session['loginToken'],logins=1,date=datetime.now().strftime('%Y-%m-%d'))
                print("created")
            except:
                print(sys.exc_info()[0])
        return redirect('/')
    except:
        errorMessage=str(sys.exc_info()[0])+" "+str(datetime.now())+"\n"
        with open("DjangoTODOAPP\logs\system_logs.txt","a")  as fr:
            fr.write(errorMessage)
        WRONG=100
    messages.add_message(request,WRONG,"invalid creditionals" ,extra_tags="wrongpassword")   
    response= redirect("/")
    response.set_cookie('rsp',"fale")
    return response    
def returnBackLoginMessages(request):
    messages.add_message(request,messages.INFO,"wow osm")
    storage = get_messages(request)
    print(len(storage))
    for message in storage:
        print(message)
    return HttpResponse(True);
def register(request):      
    username=request.GET.get('username')
    email=request.GET.get('email')
    fullname=request.GET['fullname']
    password=request.GET['rspassword']
    print(username)
    try:
        User.objects.create(username=username,email=email,first_name=fullname,password=password)
        with open("DjangoTODOAPP\logs\system_logs.txt","a") as fr:
            fr.write("Registration Done successfully "+str(datetime.now())+"\n")
        return HttpResponse("Registration Done successfully");
    except:
        with open("DjangoTODOAPP\logs\system_logs.txt","a") as fr:
            fr.write("Registration failed useremail already exit "+str(datetime.now())+"\n")
        suggestions=[]
        for n in range(4):
            suggestions.append(username+chr(random.randrange(ord('a'),ord('z')))+chr(random.randrange(ord('a'),ord('z')))+str(random.randrange(int(ord(username[int(random.randrange(int(len(username))))])*int(datetime.now().strftime("%S"))))))
        #print(json.dumps(suggestions))
        return HttpResponse(json.dumps(suggestions),status=404);

def getAll(request):
    todosObjects=[]
    todos=Todos.objects.all();
    for todo in todos:    
        todos_S =TodosSerializer(todo);
        todosObjects.append(todos_S.data)
    return HttpResponse(json.dumps(todosObjects))  
def fetchRecord(request):
    todoObjects=[]
    todoId=request.GET['todoId']
    todo=Todos.objects.get(todo_id=int(todoId))
    todo_S=TodosSerializer(todo)
    todoObjects.append(todo_S.data)
    return HttpResponse(json.dumps(todoObjects),status=200)
def setSession(request):
    request.session['loginToken']="haseeb"
    return redirect('/')
def deleteSession(request):
    del request.session['loginToken']
    return redirect('/')
def getProfileData(request):
    useremail=request.session['loginToken']
    userData=User.objects.get(username=useremail)
    #name=userData.first_name
    userdict = {
         'name':userData.first_name,
         'email':userData.email
     }
    j_data=json.dumps(userdict)
    return HttpResponse(j_data)
def updateInfo(request):
    name=request.GET['name']
    email=request.GET['email']
    user_object=User.objects.get(username=request.session['loginToken'])
    user_object.first_name=name
    user_object.email=email
    user_object.save();
    response={
        'name':user_object.first_name,
        'message':'information updated successfully'
    }
    j_response=json.dumps(response)
    return HttpResponse(j_response);
def changePassword(request):
    oldpass=request.GET['oldpass']
    newpass=request.GET['newpass']
    user=User.objects.filter(username=request.session['loginToken'],password=oldpass)
    print(len(user))
    if len(user)>0:
        userob=User.objects.get(username=request.session['loginToken'],password=oldpass)
        userob.password=newpass
        userob.save()
        insight_obj=insight.objects.filter(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d')) 
        print(len(insight_obj))
        if len(insight_obj)!=0:
            insight_objr=insight.objects.get(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d'))
            previous=insight_objr.changepassword
            previous+=1
            insight_objr.changepassword=previous
            insight_objr.save()
            print("here")
            
        else:
            try:
                insight.objects.create(username=request.session['loginToken'],logins=1,date=datetime.now().strftime('%Y-%m-%d'))
                print("created")
            except:
                print(sys.exc_info()[0])
        return HttpResponse("Password successfully changed")
    return HttpResponse("old password is wrong")
def updateUsername(request):
    username=request.GET['newusername']
    oldusername=request.GET['oldpass']
    user=User.objects.filter(username=username)
    if len(user)==0:
        userob=User.objects.get(username=request.session['loginToken'])
        userob.username=username
        userob.save()
        request.session['loginToken']=username
        insight_obj=insight.objects.filter(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d')) 
        print(len(insight_obj))
        if len(insight_obj)!=0:
            insight_objr=insight.objects.get(username=request.session['loginToken'])
            previous=insight_objr.logins
            previous+=1
            insight_objr.logins=previous
            insight_objr.save()
            print("here")
            
        else:
            try:
                insight.objects.create(username=request.session['loginToken'],logins=1,date=datetime.now().strftime('%Y-%m-%d'))
                print("created")
            except:
                print(sys.exc_info()[0])
        return HttpResponse("username updated successfully")
    return HttpResponse("username already exit")
def updateTaskNotification(request):
    user=NotificationsSettings.objects.filter(username=request.session['loginToken'])
    bit=request.GET['tasknotification']
    task=request.GET['task']
    print(task)
    print(bit)
    if bit=="0":
        bit=True
    else:
        bit=False
    if len(user)>0:
        notfi=NotificationsSettings.objects.get(username=request.session['loginToken'])
        if task=="tasknote":    
            notfi.task_notifications=bit
            notfi.save()
        elif task=="completenote":
            notfi.task_completedNotifiication=bit
            notfi.save()
        elif task=="emailnote":
            notfi.via_email=bit
            notfi.save()
        elif task=="sysnote":
            notfi.system_notifications=bit
            notfi.save()
    else:
        if task=="tasknote": 
            notfi=NotificationsSettings.objects.create(username=request.session['loginToken'],task_notifications=bit)
        elif task=="completenote":
            notfi=NotificationsSettings.objects.create(username=request.session['loginToken'],task_completedNotifiication=bit)
            
        elif task=="emailnote":
            notfi=NotificationsSettings.objects.create(username=request.session['loginToken'],via_email=bit)
            
        elif task=="sysnote":
            notfi=NotificationsSettings.objects.create(username=request.session['loginToken'],system_notifications=bit)
    return HttpResponse("updated");
        
    
def getNote(request):
    notifications=NotificationsSettings.objects.get(username=request.session['loginToken'])
    notificationObj={
        'task_notification':notifications.task_notifications,
        'complete_notification':notifications.task_completedNotifiication,
        'via_email':notifications.via_email,
        'sysem_notification':notifications.system_notifications
    }    
    j_data=json.dumps(notificationObj)
    return HttpResponse(j_data);
def saveFeedBack(request):
    topic=request.GET['topic']
    message=request.GET['message']
    Feedback.objects.create(username=request.session['loginToken'],title=topic,feedbackmessage=message)
    return HttpResponse("Thanku for providing your feedback!")
def setCompleted(request):
    todo_id=request.GET['id']
    todo=Todos.objects.get(author=request.session['loginToken'],todo_id=todo_id)
    todo.todo_status="completed"
    todo.save()
    insight_obj=insight.objects.filter(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d')) 
    if len(insight_obj)!=0:
            insight_objr=insight.objects.get(username=request.session['loginToken'],date=datetime.now().strftime('%Y-%m-%d'))
            previous=insight_objr.completetask
            previous+=1
            insight_objr.completetask=previous
            insight_objr.save()
    else:
            try:
                insight.objects.create(username=request.session['loginToken'],completetask=1,date=datetime.now().strftime('%Y-%m-%d'))
            except:
                pass
            
    return HttpResponse("Save successfully")
    
    
    
    
    
def InsightData(request):
    is_userAuth=False;
    fullname=""
    username=""
    todos=""
    insights=""
    todayDate= datetime.now().strftime("%a / %d / %m / %y");
    userProfileImage=TodoUserMedia.objects.get(username="haseebali")
    print(userProfileImage.profile.url)
    if request.session.has_key('loginToken'):
        is_userAuth=True
        userData=User.objects.get(username=request.session['loginToken'])
        insights=insight.objects.filter(username=request.session['loginToken']).order_by("-date");
        fullname=userData.first_name
        username=userData.username  
    return render(request,"insights.html",{'insights':insights,'is_userAuth':is_userAuth,'fullname':fullname,'prfileImage':userProfileImage.profile.url,'username':username,'todayDate':todayDate})    
def insightsdataset(request):
    months=['','Jan','Feb','March']
    dates=request.GET['drawdate'].replace('.',',')
    dates=dates.split(",")
    import datetime
    date=datetime.datetime(int(dates[2].split(" ")[1]),int(months.index(dates[0])),int(dates[1].split(" ")[1]))
    insights=insight.objects.get(date=date.strftime('%Y-%m-%d'))
    S_insights=insightserializer(insights)
    return HttpResponse(JsonResponse(S_insights.data))
