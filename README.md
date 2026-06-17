# Network Monitoring and Alert System

## Description

The Network Monitoring and Alert System is a Python-based application developed to monitor network devices continuously. The system checks device availability using network connectivity tests, stores monitoring information in a MySQL database, and generates alerts when devices become unreachable.

The project provides real-time monitoring capabilities and a web dashboard for displaying device information.

---

## Features

* Monitor network device availability
* Detect ONLINE and OFFLINE devices
* Measure response times
* Store monitoring data in MySQL database
* Generate alerts for unreachable devices
* Web dashboard for viewing device status
* Automated periodic monitoring

---

## Installation Steps

### 1. Install Python Packages

Run:

pip install flask mysql-connector-python ping3 schedule

### 2. Create MySQL Database

Create database:

CREATE DATABASE network_monitor;

Create required tables:

devices table

alerts table

### 3. Configure Database Connection

Update database credentials inside:

db.py

### 4. Run Monitoring Script

python monitor.py

### 5. Run Web Dashboard

python app.py

---

## Technologies Used

* Python
* MySQL
* Flask
* Ping3
* HTML
* SQL
* Networking Concepts
* Database Management

---

## How to Run

Step 1:

Run monitoring:

python monitor.py

Step 2:

Run dashboard:

python app.py

Step 3:

Open browser:

http://127.0.0.1:5000

---

## Future Improvements

* SNMP monitoring support
* Email notifications
* SMS alerts
* Device auto discovery
* Network traffic visualization
* Authentication system
* Graph analytics dashboard
* Docker deployment support

---

## Author

Oshara Gunasekara

Computer Networking Undergraduate
