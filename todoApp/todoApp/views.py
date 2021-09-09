from json.encoder import JSONEncoder
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import MySQLdb
import json

def index(request):
    return redirect('view', permanent=1)

def getAllTasksAsHTML(request):
    tasks = getAllDataFromDB()
    code = ''
    if not tasks:
        code += """
        <tr>
            <td class="row border-0">
                <div class="col-12 text-center" style="overflow-wrap: break-word;">No tasks available!</div>
            </td>
        </tr>
        """
        return HttpResponse(code)

    for key,value in tasks.items():
        code += """
        <tr>
            <td class="row border-0">
                <div class="col-10" style="overflow-wrap: break-word;">{}</div>
                <div class="col-2 my-auto">
                    <button class="btn btn-sm btn-danger shadow float-right" onclick='removeTask({})' id='{}'>Delete</button>
                </div>
            </td>
        </tr>
        """.format(value,key,key)
    return HttpResponse(code) # this returns the html code

    #return HttpResponse(JSONEncoder().encode(tasks)) # this returns object as response in case u are using react or angular or some other framework in the front end

def view(request):
    tasks = getAllDataFromDB()
    return render(request,'view.html',{'tasks':tasks})

def create(request):
    # if a get request is made, redirect to the home page
    if(request.method == 'GET'): return redirect('/view')

    task = request.POST['task'] # get the task data from the front end
    if insertDataToTheDB(task): return HttpResponse('added')
    else: return HttpResponse('failed')

def remove(request):
    if request.method == 'GET': return redirect('views')
    if deleteItemInDB(request.POST['ID']): return HttpResponse('removed')
    return HttpResponse('failed')




''' DATABASE RELATED MYSQL FUNCTIONS '''

def insertDataToTheDB(task):
    # update user, passwd and db here
    dbconnect = MySQLdb.connect(user='root', passwd='123456', db='userregistration')
    cursor = dbconnect.cursor()
    
    # get the unique id for that task
    query = "select max(id) from todo_list;"
    cursor.execute(query)
    ID = cursor.fetchone()[0]
    if not ID: ID = 0
    ID += 1

    query = "insert into todo_list values ({}, '{}')".format(ID, task)

    try:
        cursor.execute(query)
        dbconnect.commit()
        dbconnect.close()
        return True

    except:
        dbconnect.rollback()
        dbconnect.close()
        return False

def getAllDataFromDB():
    # update user, passwd and db here
    dbconnect = MySQLdb.connect(user='root', passwd='123456', db='userregistration')
    cursor = dbconnect.cursor()
    query = "select * from todo_list;"
    cursor.execute(query)
    dbconnect.close()
    r = {}
    for i in cursor.fetchall(): r[i[0]] = i[1]
    return r

def deleteItemInDB(ID):
    # update user, passwd and db here
    dbconnect = MySQLdb.connect(user='root', passwd='123456', db='userregistration')
    cursor = dbconnect.cursor()
    query = "delete from todo_list where id='{}'".format(ID)

    try:
        cursor.execute(query)
        dbconnect.commit()
        dbconnect.close()
        return True

    except:
        dbconnect.rollback()
        dbconnect.close()
        return False
