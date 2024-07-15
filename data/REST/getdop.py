import random

getdop_data = {
    "topology": [
        {
            "latitude": random.randint(0, 100),
            "longitude": random.randint(0, 100),
            "altitude": random.randint(0, 10000),
        },
        {
            "latitude": random.randint(0, 100),
            "longitude": random.randint(0, 100),
            "altitude": random.randint(0, 10000),
        },
        {
            "latitude": random.randint(0, 100),
            "longitude": random.randint(0, 100),
            "altitude": random.randint(0, 10000),
        }
    ],
    "area": [
        {
            "altitude": random.randint(0, 10000),
            "latitude": random.randint(0, 100),
            "longitude": random.randint(0, 100),
        },
        {
            "altitude": random.randint(0, 10000),
            "latitude": random.randint(0, 100),
            "longitude": random.randint(0, 100),
        },
        {
            "altitude": random.randint(0, 10000),
            "latitude": random.randint(0, 100),
            "longitude": random.randint(0, 100),
        },
        {
            "altitude": random.randint(0, 10000),
            "latitude": random.randint(0, 100),
            "longitude": random.randint(0, 100),
        }
    ],
    "hpoints": random.randint(2, 900),
    "vpoints": random.randint(2, 900),
    "hmtype": "gradient",
    "steps": [
        {
            "value": 0,
            "color": "rgb(0, 100, 0)"
        },
        {
            "value": 1,
            "color": "rgb(0, 100, 0)"
        },
        {
            "value": 2,
            "color": "rgb(0, 170, 0)"
        },
        {
            "value": 4,
            "color": "rgb(86, 255, 0)"
        },
        {
            "value": 7,
            "color": "rgb(170, 215, 0)"
        },
        {
            "value": 9,
            "color": "rgb(255, 255, 0)"
        },
        {
            "value": 21,
            "color": "rgb(255, 150, 0)"
        },
        {
            "value": 51,
            "color": "rgb(255, 20, 0)"
        }
    ],
    "usepseudomode": True
}
