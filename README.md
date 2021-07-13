## API for Indonesia ID Card Identification

### Prerequisites
- Python3 and pip3

### How to run this API
- Open your favourite terminal
- Install module dependencies `pip install -r requirements.txt`
- Export the flask app
  `export FLASK_APP=app.py`
- Run the flask API
  `flask run`

### Deployment using Docker
Dockerfile is at `./Dockerfile`

---
### Request body
- Open Postman
- Create a POST request on http://127.0.0.1:5000/api/nik
- Sample of request body:
```
{
    "nik": [
        "1234567891234567"
    ],
    "process": "full"
}
```
- `nik` contains list of ID card (KTP)
- `process` as method how the ID card information will be returned. You can choose `limited` for the limited information or `full` for the rich information

### Response API
If you choose `limited`, the response API will be as the following output
```
{
    "message": "success",
    "errors": [],    
    "data": {
        "1234567891234567": false
    },
    "summary": {
        "number": 1,
        "number_processed": 1,
        "error": 0,
        "valid": {
            "all_section": 0,
            "section": {
                "length": 1,
                "area": 0,
                "dob": 0,
                "gender": 1,
                "computerized": 1
            }
        }
    }
}
```
If you choose `full`, the response API will be as the following output
```
{
    "message": "success",
    "errors": [],
    "data": {
        "1234567891234567": {
            "data": {
                "length": {
                    "value": "1234567891234567",
                    "valid": true
                },
                "area": {
                    "value": {
                        "province": "None",
                        "district": "None",
                        "subdistrict": "None"
                    },
                    "valid": false
                },
                "dob": {
                    "value": {
                        "dob": "None", 
                        "age": "None"
                    }, 
                    "valid": false
                },
                "gender": {
                    "value": "Woman", 
                    "valid": true
                },
                "computerized": {
                    "value": "4567", 
                    "valid": true
                }
            },
            "valid": false
        }
    },
    "summary": {
        "number": 1,
        "number_processed": 1,
        "error": 0,
        "valid": {
            "all_section": 0,
            "section": {
                "length": 1,
                "area": 0,
                "dob": 0,
                "gender": 1,
                "computerized": 1
            }
        }
    }
}
```
But, if something error in the process, the following response will appear.
```
{
    "message": "failed",
    "data": [
        "1234567891234567"
    ]
}
```