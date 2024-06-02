from flask import Flask, render_template, request, jsonify
from scrape import scrape_kayak

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    origin = request.form.get('origin')
    destination = request.form.get('destination')
    outbound_date = request.form.get('outbound_date')
    return_date = request.form.get('return_date')

    if not all([origin, destination, outbound_date, return_date]):
        return jsonify({"error": "All fields are required"}), 400

    flight_results = scrape_kayak(origin, destination, outbound_date, return_date)
    if flight_results:
        return jsonify({"data": flight_results})
    else:
        return jsonify({"error": "No flight data found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
