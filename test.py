from locust import HttpLocust, TaskSet

#def login(l):
#    l.client.post('/login', {'username':'ellen_key', 'password':'education'})

def index(l):
    l.client.get('/content')

def files(l):
    l.client.get('/Shared')

def forum(l):
    l.client.get('/board/')

def chatContent(l):
    l.client.get('/chat_content.html')

def diskUsage(l):
    l.client.get('/diskusage.html')

def chatPost(l):
    chatData = {
        'name':'Anonymous',
        'data':'test',
        'color':'def',
        'timestamp':1520970818
    }
    headers = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
    l.client.post('/cgi-bin/psowrte.py', data=chatData, headers=headers)

class UserBehavior(TaskSet):
    tasks = {chatContent:5, diskUsage:5, chatPost:1}

    def on_start(self):
        index(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
