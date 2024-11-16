from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Dictionary to store OTPs temporarily
otp_store = {}

# API to send OTP
@app.route('/send_otp', methods=['POST'])
def send_otp():
    data = request.json
    phone_number = data.get('phone_number')
    if not phone_number:
        return jsonify({'error': 'Phone number is required'}), 400

    # Generate 6-digit OTP
    otp = random.randint(100000, 999999)
    otp_store[phone_number] = otp

    # Here you would integrate an SMS service to send the OTP
    print(f"OTP for {phone_number}: {otp}")  # For debugging

    return jsonify({'message': 'OTP sent successfully', 'otp': otp})

if __name__ == '__main__':
    app.run(debug=True)
