import json

x = {
    "firstname" : "Ikenna",
    "lastname": "Remigius",
    "phone" : "+23479890908938",
    "address": "DreamLink Mile 50"
}

y = json.dumps(x)
print(x)
print(y)