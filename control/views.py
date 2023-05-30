from django.shortcuts import redirect
from django.http import HttpResponse
import json
from django.shortcuts import render
from django.http import JsonResponse
import firebase
config = {
    "apiKey": "AIzaSyCZXIiAUnUGJ1yCxc5Ym4n-gQen1nZ4FLc",
    "authDomain": "servo-4fa68.firebaseapp.com",
    "databaseURL": "https://servo-4fa68-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "servo-4fa68",
    "storageBucket": "servo-4fa68.appspot.com",
    "messagingSenderId": "382953766138",
    "appId": "1:382953766138:web:0f8bbf5accbc73287c5d43",
}

# here we are doing firebase authentication
app = firebase.initialize_app(config)
authe = app.auth()
database = app.database()
def table(request):
    devices= dict(database.child("device").get().val())
    auto= database.child("auto").get().val()
    if auto == 1:
        auto = "auto"
    else:
        auto = "manual"
    context={
        'devices':devices,
        'mode':auto,
    }
    print(devices)
    return render(request, 'deviceTable.html',context)

def update_status(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        device_key = data.get('deviceKey')
        new_status = data.get('newStatus')
        database.child("device").child(device_key).set(int(new_status))
        print(device_key)
        print(new_status)
        # Return a JSON response to indicate success
        response = {'status': 'success'}
        return JsonResponse(response)
    
def update_mode(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_mode = data.get('newMode')
        if new_mode == "auto":
            new_mode = 1
        else:
            new_mode = 0
        database.child("auto").set(new_mode)
        print(new_mode)
        # Return a JSON response to indicate success
        response = {'status': 'success'}
        return JsonResponse(response)
    
def fetch_data(request):
    # Retrieve the updated data from the database or any other source
    devices= dict(database.child("device").get().val())
    auto= database.child("auto").get().val()
    if auto == 1:
        auto = "auto"
    else:
        auto = "manual"

    # Prepare the response data
    data = {
        'devices': devices,
        'mode': auto,
    }

    return JsonResponse(data)
