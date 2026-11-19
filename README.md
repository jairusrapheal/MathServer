# Ex.03 Design a Website for Server Side Processing
## Date:14/11/2026

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
<html>
<head>
    <title>CALCULATION</title>
</head>
<body>
    <h1>JAIRUS RAPHEAL</h1>
    <br>
    <h1>churnrate</h1>
    <form method="POST">
        {% csrf_token %}
        <label>
            initial customer count:
            <input type="number"
            value="{{ initial }}"
            name="length">
        </label>
        <br>
        <br>
         <label>
            costemer lost count:
            <input type="number"
            value="{{ costemers }}"
            name="breath">
             
        </label>
        <br>
        <br>
        <input type="submit" value="calculate">
        <br>
        <br>
         <label>
            area:
            <input type="number "
            value="{{ a }}">
        </label>
        <br>
        <br>
    </form>
</body>
</html>

views.py
from django.shortcuts import render

def churnrate(request):
    initial= float(request.POST.get('length', '0'))
    costemers= float(request.POST.get('breath', '0'))

    a = (initial/costemers)*100 if request.method == 'POST' else 0

    print("initial customer count =",initial)
    print("costemer lost count =",costemers)
    print("churnrate =", a)

    return render(
        request,
        'myapp/mathserv.html',
        {'initial': initial, 'costemers': costemers, 'a': a}
    )

urls.py

from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.churnrate, name='churnrate'),
]

```

## OUTPUT - SERVER SIDE:

![alt text](<Screenshot (16).png>)

## OUTPUT - WEBPAGE:

![alt text](<Screenshot (15).png>)
## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.
