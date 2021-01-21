# Dynamic Website Design for a Manufacturing Company
## AIM:
To design a dynamic website for a chip manufacturing company.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 7:
Create a database model and migrate the database.
### Step 8:
Retrieve data from database and display it in a dynamic webpage.
### Step 9:
Publish the website in the given URL.

## PROGRAM:

### base.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Silicon Private Limited</title>
    <link rel="stylesheet" href="{% static 'css/layout.css' %}">
    <link rel = "icon" href ="{% static 'img/titleicon.png' %}" type = "image/x-icon"> 
              
</head>

<body>
    <div class="container">
    <div class="banner">
        Silicon Private Limited.
    </div>
    <div class="menu">
        <div class="menuitem"><a href="/home">Home</a></div> 
        <div class="menuitem"><a href="/products">Products</a></div> 
        <div class="menuitem"><a href="/people">People</a></div>
        <div class="menuitem"><a href="/contactus">Contact Us</a></div> 
    </div><div class="content">
    {% block content %}    
    {% endblock  %}
    </div>
    <div class="footer">
        Copyright © 2021 Silicon Private Limited, Developed by Kavya.
    </div>
    </div>
</body>

</html>
```

### home.html
```
{% extends "website/base.html" %}

{% block content %}
    <div class="homecontent">    
    <h1>About Us</h1>
    <img src="/static/img/building2.jpeg" alt="Building">
    <div class="contenttext">
    Silicon Pvt Ltd, provides a broad range of semiconductor and infrastructure software applications. Some of Silicon's core technologies and products include:
    <ul>
        <li>Memory Chips</li>
        <li>SATA HDD</li>
        <li>SATA SSD </li>
        <li>Broadband Modems</li>
        <li>Wifi Devices</li>
        <li>Switching Devices</li>
        <li>Optical Sensors</li>
    </ul> 
    </div>
    </div>
{% endblock  %}
```

### products.html
```
{% block content %}

<div class="content">
    <div class="productitems">
        {% for product in products%}
        <div class="productitem">
            <div class="itemimage">
                <img src="{{ product.photo.url }}" alt="Item Photo">
            </div>
            <div class="itemname">{{ product.name }}</div>
            <div class="itemprice">Price: {{ product.price }}</div>
        </div>
        {% endfor %}
    </div>
</div>

{% endblock  %}
```

### people.html
```
{% extends "mywebsite/base.html" %}

{% block content %}

<div class="content">
    <div class="people">
        {% for people in persons%}
        <div class="crew">
            <div class="personimage">
                <img src="{{ people.photo.url }}" alt="Person Photo">
            </div>
            <div class="personname">{{ people.name }}</div>
            <div class="designation">Designation: {{ people.designation }}</div>
        </div>
        {% endfor %}
    </div>
</div>

{% endblock  %}
```

### contactus.html
```
{% extends "mywebsite/base.html" %}

{% block content %}
<div class="contactuscontent">
    <h1>CONTACT US</h1>
    <div class="contactustext">
        <h2> Alekhya (General Contact Manager)</h2>
        <h2>KPR Silicon Products Private Limited</h2>
        <h2>KPR Silicon Products India Contact Information, Email Address, Main Office Locations including headquarters address, office phone number, customer support helpline number and email id is available here with company bio data, network presence, as well as service locations</h2>
        <h2>Telangana,India - 500081</h2>
        <h2>contact number - 9989674537</h2>
        <h2>Email address - Siliconcompany@gmail.com</h2>
    </div>
</div>
{% endblock  %}
```

## OUTPUT:
![output](./static/img/output1.jpg)

![output](./static/img/output2.jpg)

![output](./static/img/output3.jpg)

![output](./static/img/output4.jpg)

### code validator report:
![output](./static/img/report1.jpg)

![output](./static/img/report2.jpg)

![output](./static/img/report3.jpg)

![output](./static/img/report4.jpg)

## RESULT:
Thus a website is designed for the chip manufacturing company and is hosted in the URL http://kavya.student.saveetha.in:8000/. HTML code is validated.
