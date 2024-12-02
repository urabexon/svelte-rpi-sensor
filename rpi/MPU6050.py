#!/usr/bin/python
# ---coding: utf-8---
import smbus
import time
import json
import math
from time import sleep
from flask import Flask, requset, Markup, abort, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DEV_ADDR = 0x68         # device address
PWR_MGMT_1 = 0x6b       # Power Management 1
ACCEL_XOUT = 0x3b       # Axel X-axis
ACCEL_YOUT = 0x3d       # Axel Y-axis
ACCEL_ZOUT = 0x3f       # Axel Z-axis
TEMP_OUT = 0x41         # Temperature
GYRO_XOUT = 0x43        # Gyro X-axis
GYRO_YOUT = 0x45        # Gyro Y-axis
GYRO_ZOUT = 0x47        # Gyro Z-axis

bus = smbus.SMBus(1)
bus.write_byte_data(DEV_ADDR, PWR_MGMT_1, 0)

# 1byte read
def read_byte(addr):
    return bus.read_byte_data(DEV_ADDR, addr)

# 2byte read
def read_word(addr):
    high = read_byte(addr)
    low  = read_byte(addr + 1)
    return (high << 8) + low

# Sensor data read
def read_word_sensor(addr):
    val = read_word(addr)
    if(val < 0x8000):
        return val
    else:
        return val - 65536

# Get Temperature
def get_temp():
    temp = read_word_sensor(TEMP_OUT)
    # offset = -521 @ 35℃
    return (temp + 521) / 340.0 + 35.0

# Get Gyro data (raw value)
def get_gyro_data_lsb():
    x = read_word_sensor(GYRO_XOUT)
    y = read_word_sensor(GYRO_YOUT)
    z = read_word_sensor(GYRO_ZOUT)
    return [x, y, z]

# Get Gyro data (deg/s)
def get_gyro_data_deg():
    x, y, z = get_gyro_data_lsb()
    # Sensitivity = 131 LSB/(deg/s), @cf datasheet
    x = x / 131.0
    y = y / 131.0
    z = z / 131.0
    return [x, y, z]

# Get Axel data (raw value)
def get_accel_data_lsb():
    x = read_word_sensor(ACCEL_XOUT)
    y = read_word_sensor(ACCEL_YOUT)
    z = read_word_sensor(ACCEL_ZOUT)
    return [x, y, z]

# Get Axel data (G)
def get_accel_data_g():
    x, y, z = get_accel_data_lsb()
    # Sensitivity = 16384 LSB/G, @cf datasheet
    x = x / 16384.0
    y = y / 16384.0
    z = z / 16384.0
    return [x, y, z]

@app.route('/test', methods=['GET', 'POST'])
def test():
	if request.method == 'GET':
		temp = get_temp()
		gyro_x, gyro_y,gyro_z = get_gyro_data_deg()
		accel_x, accel_y,accel_z = get_accel_data_g()
		d = {"gx": '%.3f' % gyro_x, "gy": '%.3f' % gyro_y , "gz":'%.3f' % gyro_z, "ax": '%.3f' % accel_x, "ay":'%.3f' % accel_y, "az":'%.3f' % accel_z}
		return jsonify(d)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)