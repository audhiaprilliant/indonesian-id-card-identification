# Module for data manipulation
import pandas as pd
# Module for linear algebra calculation
import numpy as np
# Module for timing
from datetime import datetime
from src.utils import helper

class identificationID:
    def __init__(self, ID):
        self.ID = ID
    # Get value
    def get_value(self):
        return str(self.ID)
    # Check length of ID
    def checkLength(self):
        length = len(str(self.ID))
        # check length
        status = False
        if length == 16:
            status = True
        return (status, length)
    # Check administrative area
    def checkAdminArea(self, data):
        admin_code = str(self.ID)[:6]
        # Check the admin area
        status = False
        prov, district, subdistrict = None, None, None
        bin_status = helper.binary_search(a = data['code'], x = admin_code)
        if bin_status:
            status = True
            # Get the values
            prov, district, subdistrict = data[data['code'] == admin_code].values.tolist()[0][1:]
        return (status, prov, district, subdistrict)
    # Check DOB
    def checkDOB(self):
        dob = str(self.ID)[6:12]
        dob_person = int(dob)
        # Check the woman's dob
        if dob_person > 400000:
            dob_person = dob_person - 400000
        # Convert into datetime
        try:
            dob_date = datetime.strptime(str(dob_person), '%d%m%y')
            if dob_date > datetime.now():
                dob_date = dob_date.replace(year = dob_date.year - 100)
        except:
            dob_date = None
        # Check age
        status = False
        age_int = None
        if dob_date != None:
            age = (datetime.now() - dob_date).days / 365.2425
            dob_date = dob_date.strftime('%d-%m-%Y')
            if age >= 17:
                age_int = int(age)
                status = True
        return (status, dob_date, age_int)
    # Check Gender
    def checkGender(self):
        gender = str(self.ID)[6:7]
        # Check status
        status = False
        sex = None
        if int(gender) in range(8):
            if int(gender) in range(4):
                sex = 'Man'
            else:
                sex = 'Woman'
            status = True
        return (status, sex)
    # Check computerized number
    def checkComputerizedNumber(self):
        last_num = str(self.ID)[12:]
        # Check last number
        status = False
        if status != '0000':
            status = True
        return (status, last_num)