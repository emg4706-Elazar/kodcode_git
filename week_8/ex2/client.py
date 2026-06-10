import requests

data = {
    "type": "Circle",
    "attributes": {
        "quoter": 4,
        "radius": 56
    }
}


new_data = {
    "type": "Rectangle",
    "attributes": {
        "length": 4,
        "width": 37
    }
}

#
# response1 = requests.post("http://127.0.0.1:8000/shapes", json=data)
# print(response1.json())
# print()

# response2 = requests.put("http://127.0.0.1:8000/shapes", json=new_data ,params={"shape_id": 1})
# print(response2.json())
# print()

response2 = requests.delete("http://127.0.0.1:8000/shapes",params={"shape_id": 5})
# print(response2.json())
# print()



response3 = requests.get("http://127.0.0.1:8000/shapes")
for s in response3.json():
    print(s)





