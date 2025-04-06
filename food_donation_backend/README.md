
# 🍱 Food Donation Backend

This Flask backend powers the Food Donation Platform, supporting features like food quality monitoring, anonymous reporting, and feedback.

## 🚀 How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the server:

```
python app.py
```

3. Open browser at: `http://127.0.0.1:5000`

## 📡 Available API Endpoints

- `GET /` - Web UI with health check
- `GET /api/health` - Server health status
- `POST /api/sensor-data` - Receives IoT food data
- `POST /api/batch-report` - Logs batch reports
- `POST /api/whistleblower` - Anonymous reports
- `POST /api/verify-ingredient` - Verify ingredient safety
- `POST /api/feedback` - Submit food feedback
