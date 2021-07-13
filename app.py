# Import modules
import pandas as pd
import numpy as np
import os
from datetime import date
from flask import Flask, request, jsonify
from src.data import validator

# Current directory
current_dir = os.path.dirname(__file__)

# Config
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['DEBUG'] = True

# Read the helper data
df = pd.read_csv('data/csv/Admin Area Code - ID.csv', sep = ',', dtype = {'code': object})

# Main page
@app.route('/', methods = ['GET'])
def home():
    return '''<h1>API for Indonesian ID Card Identification</h1>
<p>Created by Audhi Aprilliant</p>'''

# NIK Identification
@app.route('/api/nik', methods = ['POST'])
def nik_identification():
	# Get the parameters
	params = request.get_json()
	NIKs = params['nik']
	process = params['process']

	# Variables for summaries
	sum_number = 0
	sum_valid_number = 0
	sum_length = 0
	sum_area = 0
	sum_dob = 0
	sum_gender = 0
	sum_computerized = 0

	# json objects
	errors = []
	data_full = {}
	data_limited = {}

	# Looping
	for i in range(len(NIKs)):
		try:
		    # Assign NIK into object
		    NIK = validator.identificationID(NIKs[i])
		    NIK_value = NIK.get_value()
		    
		    # NIK's length
		    stat_length, nik_length = NIK.checkLength()
		    # NIK's admin area
		    stat_area, nik_prov, nik_district, nik_subdistrict = NIK.checkAdminArea(data = df)
		    # NIK's DOB
		    stat_dob, nik_dob, nik_age = NIK.checkDOB()
		    # NIK's gender
		    stat_gender, nik_gender = NIK.checkGender()
		    # NIK's last computerized number
		    stat_comp, nik_comp = NIK.checkComputerizedNumber()
		    
		    # Summary
		    valid_all = stat_length & stat_area & stat_dob & stat_gender & stat_comp
		    sum_number += 1
		    sum_valid_number += valid_all
		    sum_length += stat_length
		    sum_area += stat_area
		    sum_dob += stat_dob
		    sum_gender += stat_gender
		    sum_computerized += stat_comp
		    
		    # Convert into json - data full
		    dic_data_full = {
		        NIK_value: {
		            'data': {
		                'length': {
		                    'value': NIK_value,
		                    'valid': stat_length
		                },
		                'area': {
		                    'value': {
		                        'province': nik_prov,
		                        'district': nik_district,
		                        'subdistrict': nik_subdistrict
		                    },
		                    'valid': stat_area
		                    },
		                'dob': {
		                    'value': {
		                        'dob': nik_dob,
		                        'age': nik_age
		                    },
		                    'valid': stat_dob
		                },
		                'gender': {
		                    'value': nik_gender,
		                    'valid': stat_gender
		                },
		                'computerized': {
		                    'value': nik_comp,
		                    'valid': stat_comp
		                }
		            },
		            'valid': valid_all
		        }
		    }
		    # Convert into json - data limited
		    dic_data_limited = {
		        NIK_value: valid_all
		    }
		    
		    # Append into json
		    data_full = {**data_full, **dic_data_full}
		    data_limited = {**data_limited, **dic_data_limited}
		except:
			errors.append(NIKs[i])
			continue

	# Convert into json - summary
	summary = {
		'number': len(NIKs),
	    'number_processed': sum_number,
	    'error': len(errors),
	    'valid': {
	    	'all_section': sum_valid_number,
	    	'section': {
		    	'length': sum_length,
		        'area': sum_area,
		        'dob': sum_dob,
		        'gender': sum_gender,
		        'computerized': sum_computerized
	    	}
	    }
	}
	# Convert into json - master
	json_data_full = {
		'message': 'success',
		'errors': errors,
		'data': data_full,
		'summary': summary
		}
	json_data_limited = {
		'message': 'success',
		'errors': errors,
		'data': data_limited,
		'summary': summary
		}

	# Return the json
	if process == 'full':
		return jsonify(
			json_data_full
			)
	elif process == 'limited':
		return jsonify(
			json_data_limited
			)
	else:
		return jsonify({
			'message': 'failed',
			'data': NIKs}
			)

if __name__ == '__main__':
    app.run(debug = True)