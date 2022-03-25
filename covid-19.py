import requests
from win10toast import ToastNotifier
import json
import time

def update():
    r = requests.get('http://coronavirus-19-api.herakuapp.com/all')
    data = r.json()
    text = f"Comfirmed Cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}"

    while True:
        toast = ToastNotifier()
        toast.show_toast("Covid-19 Updates",text,duration-20)
        time.sleep(60)
update()
