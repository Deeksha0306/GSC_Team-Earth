const baseUrl = "http://127.0.0.1:5000";

function checkHealth() {
    fetch(baseUrl + "/api/health")
        .then(res => res.json())
        .then(data => {
            document.getElementById("health-status").innerText = data.message;
        });
}

function submitSensor() {
    const temp = document.getElementById("temp").value;
    const oil = document.getElementById("oil").value;

    fetch(baseUrl + "/api/sensor-data", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ temperature: temp, oil_quality: oil })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("sensor-result").innerText = data.alert || data.message;
    });
}