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
```
{
    "nik": [
        "",
        "",
        ""
    ],
    "process": ""
}
```
- `nik` contains list of ID card (KTP)
- `process` as method how the ID card information will be returned. You can choose `limited` for the limited information or `full` for the rich information

### Respond API
```
{
    "message": "",
    "data": {
        "ID 1" : {
            "data": {
                "length": {
                    "value": "",
                    "valid": ""
                },
                "area": {
                    "value": {
                        "province": "",
                        "district": "",
                        "subdistrict": ""
                    },
                    "valid": ""
                },
                "dob": {
                    "value": {
                        "dob": "",
                        "age": ""

                    },
                    "valid": ""
                },
                "sex": {
                    "value": "",
                    "valid": ""
                },
                "computerized": {
                    "value": "",
                    "valid": ""
                }
            },
            "valid": ""
        }
    },
    "summary": {
        "number": "",
        "number_processed": "",
        "error": "",
        "valid_number": "",
        "valid": {
            "all_section": "",
            "section": {
                "length": "",
                "area": "",
                "dob": "",
                "gender": "",
                "computerized": ""
        }
    }
}
```