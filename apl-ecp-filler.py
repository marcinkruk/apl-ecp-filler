#!/usr/bin/python
import calendar
import datetime
import requests

def getworkdays(year, month):
    c = calendar.Calendar()
    m = []
    for day in c.itermonthdays4(year, month):
        if day[1] == month and day[3] != 5 and day[3] != 6:
            m.append(day)
    return m

def daytostr(day):
    return('{:04d}-{:02d}-{:02d}'.format(day[0], day[1], day[2]))

def createtask(project, task, duration, date): 
    return {'project': project,
        'task': task,
        'duration': duration,
        'date': date,
        'btn_submit': 'Submit'}

def fillmonth(year, month):
    loginreq = requests.post(loginurl, data=login, verify=aplcert)
    m = getworkdays(year, month)
    for day in m:
        requests.post(timeurl, data=createtask('23', '17', '0:15', daytostr(day)), cookies=loginreq.cookies, verify=aplcert)
        requests.post(timeurl, data=createtask('85', '336', '6:00', daytostr(day)), cookies=loginreq.cookies, verify=aplcert)
        requests.post(timeurl, data=createtask('23', '72', '1:45', daytostr(day)), cookies=loginreq.cookies, verify=aplcert)

def fillcurrentweek():
    loginreq = requests.post(loginurl, data=login, verify=aplcert)
    today = datetime.datetime.today()
    lastmonday = today - datetime.timedelta(days=today.weekday())
    for i in range(0, 5):
        day = lastmonday + datetime.timedelta(i)
        requests.post(timeurl, data=createtask('23', '17', '0:15', day), cookies=loginreq.cookies, verify=aplcert)
        requests.post(timeurl, data=createtask('85', '336', '6:00', day), cookies=loginreq.cookies, verify=aplcert)
        requests.post(timeurl, data=createtask('23', '72', '1:45', day), cookies=loginreq.cookies, verify=aplcert)

url = 'https://ecp.astripolska.net/'
loginurl = url + 'login.php'
timeurl = url + 'time.php'
aplcert = '/etc/ca-certificates/trust-source/anchors/astripolskaCA.crt'

login = {'login': 'xxx',
    'password': 'xxx',
    'btn_login': "Login"}

# fillmonth(2020, 7)
fillcurrentweek()
