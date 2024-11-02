import serial
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

# Configure the serial connection
arduino_port = '/dev/ttyUSB0'  # Replace with your Arduino's serial port
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Wait for the serial connection to initialize

def send_message_to_arduino(message):
    # Encode and send the message
    ser.write(message.encode('utf-8'))
    print("Message sent to Arduino:", message)

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the request path
        path = self.path[1:]  # Strip the leading '/'
        decoded_path = urllib.parse.unquote(path)  # Decode URL-encoded characters
        
        # Send the message to Arduino
        send_message_to_arduino(decoded_path)
        
        # Send HTTP response
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(f"Message '{decoded_path}' sent to Arduino.".encode("utf-8"))

def run_server():
    server_address = ('', 8547)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Server listening on port 8547...")
    httpd.serve_forever()

try:
    run_server()
except KeyboardInterrupt:
    print("Shutting down server...")
finally:
    ser.close()  # Close the serial connection on exit
