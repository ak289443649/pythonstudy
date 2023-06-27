# request
import requests

def reqMethod():
    url = 'http://localhost:8899/api/record/saveRecordParam'
    data = {
        'name': '张三',
        'commonStr': '这是一个python探测器'
    }
    response = requests.post(url,data = data)
    print(response.status_code)
    print(response.text)

reqMethod()