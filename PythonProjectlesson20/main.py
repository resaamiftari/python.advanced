from fastapi import FastAPI

app=FastAPI()

@app.get("/")

def root():
    return {
        "address": {
            "street": "pashko vasa",
            "city": "prishtine",
            "country": "kosove"

        },
        "contacts": [
            {
                "type": "email",
                "value": "donjeta@gmail.com"
            },
            {
                "type": "phone",
                "value": "555-123-4567"
            }
        ]
    }

@app.get("/users/")
def read_root():
    return {
        "message": "Hello There"
    }


