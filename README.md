# PID Line Follower Simulation

A real-time robot simulation built in Python where a robot follows a circular 
track using a PID controller, with Gaussian sensor noise to simulate real hardware.

## What it does
- Robot senses its position on the track (with realistic noise)
- PID controller calculates steering correction in real time
- Live visualization using Pygame

## Skills demonstrated
- PID control theory (Kp, Ki, Kd tuning)
- Sensor noise modeling with NumPy
- Real-time simulation without physical hardware

## PID Tuning Results

| Setting | Behavior |
|---|---|
| Kp=5.0 | Aggressive, wiggles a lot |
| Kp=0.5 | Sluggish, drifts off track |
| Kp=2.0, Ki=0.01, Kd=0.5 | Smooth, stable following |

## How to run
```bash
pip install pygame numpy
python robot_sim.py
```

## Tech stack
Python, Pygame, NumPy
