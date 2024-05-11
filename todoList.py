#اضافه کردنه وظیفه جدید
# نمایش لیست وظایف با توضیحات
#قابلیت حذف وظایف از لیست
#امکان به روز رسانی وضعت
#ذخیره وضعیت به پرورنده

import json

tasks = []
x   = 0
def addTask(titel,description,status,x): 
       
       tasks.append({
            "id": x,
           "titels": titel,
           "description" :description,
           "status": status
       }) 
       
       
def removeTask(choiseRemove):
        for task in tasks:
              if task["id"] == choiseRemove:
                    print(task["titels"])
                    tasks.remove(task)
                                      
def showAllTasks():
        print(tasks)

def chengStatusTask(chengeTask,newStatuse):
        for task in tasks:
              if task["id"] == chengeTask:
                    task["status"] = newStatuse
        
def seveInFileTask(file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)
        print(f'Books have been saved to {file_name}')

def loadTaskOld(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        tasksOld = json.load(file)
        tasks.append(tasksOld)
        print(f'Books have been loaded from {file_name}')        

while True:
    reqouest = input("1=addTask   2=removeTask   3=showAllTasks   4=chengStatusTask   5=seveInFileTask   6=loadTaskOld:")
    if reqouest =="1":
        x+=1    
        titelTask = input("enter your titel :")
        desscriptionTask =input("enter your description :")
        statusTask = input("enter your status .doing. or .done. :")
        if statusTask =="done" or statusTask =="doing":
            addTask(titelTask,desscriptionTask,statusTask,x)
        else :
             print("status is wrong")    

    elif reqouest =="2":    
        choiseRemove = int(input("enter your id Task to remove:"))
        removeTask(choiseRemove)

    elif reqouest =="3":    
        showAllTasks()

    elif reqouest =="4":
        chengeTask =int(input("enter your id to chenge statua :"))
        newStatuse = input("enter your new statuse :")
        if newStatuse == "done" or newStatuse =="doing":
            chengStatusTask(chengeTask ,newStatuse)
        else :
             print("status is wrong")    

    elif reqouest =="5":
        file_name = input("enter your file name:")
        seveInFileTask(file_name)
    
    elif reqouest =="6":
       file_name = input("enter your file name:")
       loadTaskOld(file_name)  
    else:
       print("error")        
    