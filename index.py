import random
import os
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, jsonify, send_from_directory
# from flask_cache_buster import CacheBuster
import time
import string
import json
import krpc
from attitude_control import attitude_control
from threading import Timer

conn = krpc.connect(name='Fly-by-wire', address='127.0.0.1')
vessel = conn.space_center.active_vessel
attitude_pilot = attitude_control(vessel, conn, axis_scaling = (0.25, 0.1, 0.2))

fps = 30
last_update = -1
spf = 1 / fps


def update_and_steer(interval):
	Timer(interval, update_and_steer, [interval]).start()
	attitude_pilot.update()
	attitude_pilot.steer()


def angles_to_control_landscape(angles, raw=False):
	if 45 < angles[2] < 90:
		angles[2] = -90
	elif 0 < angles[2] < 45:
		angles[2] = 0
	pitch = (- 45 - angles[2])
	roll = angles[1]
	if not raw:
		pitch /= 45
		roll /= 90
	return pitch, roll


def angles_to_control_portrait(angles, raw=False):
	pitch, roll = angles[1], angles[2]
	if not raw:
		pitch /= 90
		roll /= 90
	return pitch, roll

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kab9hlasjdb023jlgkab0ksd89p1uaivopwb9012h'

config = {
     'extensions': ['.js', '.css', '.csv'],
     'hash_size': 10
}

update_and_steer(spf)

@app.route('/', methods=['GET'])
def index():
	return render_template(
		'index.html',
	)

@app.route('/attitude_update', methods=['POST'])
def attitude_update():
	global last_update
	if time.time() > last_update + spf:
		pitch, roll = angles_to_control_portrait(json.loads(tuple(request.form)[0]), raw=True)
		attitude_pilot.set_target([pitch, roll, 0])
		last_update = time.time()
	return jsonify({'success': True}, 200, {'ContentType': 'application/json'})

@app.route('/throttle_update', methods=['POST'])
def throttle_update():
	vessel.control.throttle = float(json.loads(tuple(request.form)[0])) / 100
	return jsonify({'success': True}, 200, {'ContentType': 'application/json'})

if __name__ == '__main__':
	app.run(host='0.0.0.0')
