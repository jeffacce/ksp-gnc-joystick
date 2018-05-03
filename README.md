# ksp-gnc-joystick
Kerbal Space Program Phone Joystick

## Starting a server
1. Go into Kerbal Space Program (1.4.1 to be compatible with kRPC) and start flying a plane.
2. Start a kRPC server.
3. Use Flask with Python 3 to run `index.py`.
4. With your phone and the server on the same network, navigate your phone browser to `http://[your computer ip]:5000`.
5. Fly!

## Sensitivity
If your plane wobbles around or reacts sluggishly, tweak the `axis_scaling=(0.25, 0.1, 0.2)` on line 14 in `index.py` to something else. If your plane wobbles around, it's too sensitive and you should tune the sensitivity down. If your plane reacts slowly or struggles to reach an attitude, and the autopilot never uses the full range of controls, you should tune the sensitivity up in that axis.

The axes are in the order of (pitch, roll, yaw). Larger number <==> more sensitive (and vice versa).

Note: while the attitude autopilot stabilizes unstable plane designs to some extent, sometimes the problem is in the plane. Check manually if your plane flies, then hand it over to the script.
