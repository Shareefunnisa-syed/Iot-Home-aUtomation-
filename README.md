 ---------- IoT Home Automation using ESP32 and Flask ---------

--> This project implements a local IoT-based smart monitoring system using an ESP32 microcontroller and a DHT11 temperature-humidity sensor.  
--> The ESP32 collects environmental data and transmits it via HTTP POST to a Python Flask server hosted on a PC or Raspberry Pi.  
--> The Flask server processes the incoming data and renders it on a dynamic web dashboard using HTML and Jinja2 templating.  
--> This system offers a cost-effective and scalable approach for smart home applications without depending on cloud services.

Features  
--> Real-Time Monitoring: Continuously tracks temperature and humidity with sensor readings updated every few seconds.  
--> Wireless Communication: Utilizes Wi-Fi and HTTP protocol to send sensor data from ESP32 to the local server.  
--> Web Dashboard: Displays sensor values in a clean, user-friendly interface accessible via browser on the same network.  
--> Offline Operation: Fully functional on a local network without the need for external APIs or cloud platforms.  
--> Easy Setup: Organized code structure with minimal dependencies for fast deployment and testing.  
--> Scalable Architecture: Can be extended to include multiple sensors or actuator controls (e.g., fan, light, alert system).

Requirements  
--> ESP32 Development Board (e.g., DOIT ESP32 DEVKIT V1)  
--> DHT11 or DHT22 Temperature & Humidity Sensor  
--> Arduino IDE (with ESP32 board support installed)  
--> Python 3.x  
--> Flask (`pip install flask`)  
--> Local Wi-Fi Network  
--> Web Browser (for accessing the dashboard)
