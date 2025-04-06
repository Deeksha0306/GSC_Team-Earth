
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>🍱 Food Donation Backend</title>
        <style>
            body {
                background: linear-gradient(to right, #ffecd2 0%, #fcb69f 100%);
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: #333;
                text-align: center;
                padding-top: 80px;
                margin: 0;
            }
            h1 {
                font-size: 3em;
                color: #ff5722;
                animation: slideIn 1s ease;
            }
            p {
                font-size: 1.2em;
                margin-top: 20px;
            }
            button {
                background-color: #ff5722;
                color: white;
                padding: 12px 24px;
                font-size: 1em;
                border: none;
                border-radius: 8px;
                margin-top: 30px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            button:hover {
                background-color: #e64a19;
            }
            @keyframes slideIn {
                from { opacity: 0; transform: translateY(-30px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
        <h1>🍱 Food Donation Backend</h1>
        <p>Status: <strong id="status">Checking...</strong></p>
        <button onclick="checkStatus()">Check Health</button>
        <script>
            async function checkStatus() {
                const res = await fetch('/api/health');
                const data = await res.json();
                document.getElementById('status').innerText = data.message;
            }
            checkStatus();
        </script>
    </body>
    </html>
    '''

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy", "message": "System up and running!"})

@app.route('/api/sensor-data', methods=['POST'])
def sensor_data():
    data = request.json
    alert = ""
    if data['temperature'] > 45:
        alert = "⚠️ Food temperature too high!"
    if data['oil_quality'] < 50:
        alert += " ⚠️ Oil quality poor!"
    return jsonify({"status": "ok", "alert": alert})

@app.route('/api/batch-report', methods=['POST'])
def batch_report():
    data = request.json
    suspicious = data['hygiene_score'] < 3 or "expired" in data['ingredients']
    return jsonify({
        "status": "received",
        "flagged": suspicious,
        "message": "Batch logged successfully." if not suspicious else "⚠️ Flagged for inspection."
    })

@app.route('/api/whistleblower', methods=['POST'])
def report_issue():
    issue = request.json['message']
    return jsonify({"status": "reported", "message": "✅ Report submitted anonymously."})

@app.route('/api/verify-ingredient', methods=['POST'])
def verify_ingredient():
    ingredient = request.json['name']
    if ingredient.lower() in ['unregistered', 'unknown']:
        return jsonify({"verified": False, "message": "❌ Not FSSAI verified."})
    return jsonify({"verified": True, "message": "✅ Ingredient verified."})

@app.route('/api/feedback', methods=['POST'])
def food_feedback():
    rating = request.json['rating']
    return jsonify({"message": "Thanks for the feedback!", "rating": rating})

if __name__ == '__main__':
    app.run(debug=True)
