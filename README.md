# ksp-gnc-joystick
Kerbal Space Program Phone Joystick

## Dependencies Setup
1. Run 'virtualenv env' in the ksp-gnc-joystick directory to create a Python virtual environment
2. Run 'env/bin/activate' (Linux, Mac OS) or 'env/Scripts/activate' (Windows) to switch to the virtual environment
3. Run 'pip install -r requirements.txt' to install dependencies in this virtual environment (needed only the first time)

It is possible, but not recommended, to install these packages globally

## Starting a server
1. Go into Kerbal Space Program (1.4.1 to be compatible with kRPC) and start flying a plane.
2. Start a kRPC server.
3. Use Flask with Python 3 to run `index.py`. (If you want raw control, run `raw.py` instead.)
4. With your phone and the server on the same network, navigate your phone browser to `http://[your computer ip]:5000`.
5. Fly! (Raw control: hold phone in landscape. Right now only one side in landscape makes sense, and the other side is inverted because I haven't yet bothered to code that in. For pitch, tilt forward/aft; neutral point 45 degrees. For roll, tilt left/right; neutral point 0 degrees.)

## Sensitivity
If your plane wobbles around or reacts sluggishly, tweak the `axis_scaling=(0.25, 0.1, 0.2)` on line 14 in `index.py` to something else. If your plane wobbles around, it's too sensitive and you should tune the sensitivity down. If your plane reacts slowly or struggles to reach an attitude, and the autopilot never uses the full range of controls, you should tune the sensitivity up in that axis.

The axes are in the order of (pitch, roll, yaw). Larger number <==> more sensitive (and vice versa).

Note: while the attitude autopilot stabilizes unstable plane designs to some extent, sometimes the problem is in the plane. Check manually if your plane flies, then hand it over to the script.
