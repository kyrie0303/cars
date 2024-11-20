from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

# Mock data voor development
MOCK_DATA = {
    "devices": [
        {
            "id": "dev001",
            "name": "Temperature Sensor A1",
            "type": "temperature",
            "status": "active",
            "locationId": "loc001",
            "lastMaintenance": "2024-01-15",
            "batteryLevel": 85,
            "firmwareVersion": "2.3.1"
        },
        {
            "id": "dev002",
            "name": "Humidity Sensor H1",
            "type": "humidity",
            "status": "active",
            "locationId": "loc001",
            "lastMaintenance": "2024-02-01",
            "batteryLevel": 92,
            "firmwareVersion": "1.9.4"
        },
        {
            "id": "dev003",
            "name": "Motion Detector M1",
            "type": "motion",
            "status": "maintenance",
            "locationId": "loc002",
            "lastMaintenance": "2023-12-20",
            "batteryLevel": 45,
            "firmwareVersion": "3.0.0"
        },
        {
            "id": "dev004",
            "name": "Light Controller L1",
            "type": "lighting",
            "status": "active",
            "locationId": "loc002",
            "lastMaintenance": "2024-01-30",
            "batteryLevel": 78,
            "firmwareVersion": "2.1.0"
        },
        {
            "id": "dev005",
            "name": "CO2 Sensor C1",
            "type": "air_quality",
            "status": "inactive",
            "locationId": "loc003",
            "lastMaintenance": "2024-01-10",
            "batteryLevel": 15,
            "firmwareVersion": "1.8.2"
        }
    ],
    "locations": [
        {
            "id": "loc001",
            "name": "Server Room A",
            "floor": "1st Floor",
            "building": "Main Building"
        },
        {
            "id": "loc002",
            "name": "Conference Room B",
            "floor": "2nd Floor",
            "building": "Main Building"
        },
        {
            "id": "loc003",
            "name": "Security Office",
            "floor": "Ground Floor",
            "building": "Main Building"
        }
    ]
}

def get_devices():
    """Haal alle apparaten op"""
    return MOCK_DATA["devices"]

def get_locations():
    """Haal alle locaties op"""
    return MOCK_DATA["locations"]

@app.route('/')
def index():
    """Homepage route"""
    try:
        devices = get_devices()
        locations = get_locations()
        
        # Maak een dictionary van locaties voor snelle lookup
        location_dict = {loc['id']: loc for loc in locations}
        
        # Voeg locatie informatie toe aan elk apparaat
        for device in devices:
            device['location'] = location_dict.get(device['locationId'], {
                'name': 'Onbekende locatie',
                'floor': 'Onbekend',
                'building': 'Onbekend'
            })
        
        return render_template('index.html', devices=devices, locations=locations)
    except Exception as e:
        print(f"Error in index route: {e}")
        return f"Er is een fout opgetreden: {str(e)}", 500

@app.route('/devices')
def devices():
    """Apparaten overzicht pagina"""
    try:
        devices = get_devices()
        locations = get_locations()
        location_dict = {loc['id']: loc for loc in locations}
        
        for device in devices:
            device['location'] = location_dict.get(device['locationId'], {
                'name': 'Onbekende locatie',
                'floor': 'Onbekend',
                'building': 'Onbekend'
            })
            
        return render_template('devices.html', devices=devices)
    except Exception as e:
        return f"Er is een fout opgetreden: {str(e)}", 500

@app.route('/locations')
def locations():
    """Locaties overzicht pagina"""
    try:
        locations = get_locations()
        return render_template('locations.html', locations=locations)
    except Exception as e:
        return f"Er is een fout opgetreden: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)