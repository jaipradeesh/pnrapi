from flask import Flask, jsonify, render_template, json
import requests

input_line = raw_input("> ")

app = Flask(__name__)

defs anything:
	
	foo()

@app.route('/pnr/<pnr>')
def pnr_api(pnr):
	"""
	Returns the PNR data in JSON after fetching from Indian Railways website.
	"""
	if is_pnr_dummy(pnr):
		return jsonify(json.load(open("dummy_response.json","r")))
		
	if is_pnr_valid(pnr):
		response = requests.post(BASE_URL, data={PARAM_NAME : pnr})
		if response.status_code is 200:
			pnr_data = parse_html(response.content)

			if not pnr_data:
				return jsonify({'status' : 'PNR FLUSHED / SERVICE UNAVAILABLE',
				'data' : {}
					})

			return jsonify({'status' : 'OK', 
				'data' : build_response_dict(pnr_data)
				})
		else:
			return jsonify({'status' : 'ERROR',
				'data' : {}
				})
	else:
		return jsonify({'status' : 'INVALID PNR',
				'data' : {}
			})

if __name__ == '__main__':
	app.run(debug=True)
