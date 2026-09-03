# MAGI Simulation & Robotics Architecture

This directory houses the simulation environments, analytical kinematics solvers, locomotion algorithms, 3D robot models, and web-based interactive dashboards for the MAGI quadruped robot.

---

## Directory Organization

```text
simulation/
├── models/
│   ├── urdf/
│   │   └── SpiderQ.urdf          # 12-DOF Quadruped URDF model definition
│   └── meshes/
│       └── SpiderQ.glb           # 3D robot geometry mesh (GLB format)
│
├── python/
│   ├── kinematics/
│   │   ├── ik.py                 # Analytical 3-DOF inverse kinematics solver (LegIK3DOF)
│   │   └── fk.py                 # Forward kinematics reference module
│   │
│   ├── locomotion/
│   │   ├── gait.py               # Parametric stance/swing foot trajectory generator
│   │   └── MAGI_gait_learning.py # Crawl gait learning with terrain adaptation & noise injection
│   │
│   ├── pybullet/
│   │   ├── demo_pybullet.py      # PyBullet physics simulation environment loading SpiderQ
│   │   └── main.py               # Locomotion stepping loop and IK angle calculations
│   │
│   └── visualization/
│       ├── visualize_2D.py       # 2D Matplotlib sagittal & top-down leg animation
│       └── Visualize_3D.py       # Real-time 3D Matplotlib crawl gait animation
│
└── web/
    ├── index.html                # Main web simulation dashboard interface
    ├── style.css                 # Dark theme layout and responsive styles
    ├── dashboard.js              # 60 FPS animation & telemetry coordination loop
    ├── robot.js                  # Three.js 3D viewport renderer & IK solver
    ├── gait.js                   # Cubic Bezier foot trajectory generator
    ├── rl_train.js               # In-browser genetic algorithm gait optimizer
    ├── magi_fusion.js            # Decision engine & sensor fusion override logic
    ├── debug.html                # Component diagnostics interface
    ├── magi_standalone.html      # Bundled single-page offline simulator
    └── lib/
        ├── three.min.js          # Three.js 3D library
        ├── OrbitControls.js      # Three.js camera control
        └── chart.min.js          # Chart.js telemetry plotting library
```

---

## Quick Start Guide

### 1. Web Simulator
To launch the browser-based 3D simulation:
```bash
cd simulation/web
python -m http.server 8765
```
Open `http://localhost:8765` in your browser.

### 2. Python Physics Simulation (PyBullet)
```bash
pip install pybullet numpy
python simulation/python/pybullet/demo_pybullet.py
```

### 3. Matplotlib 3D Gait Visualization
```bash
pip install matplotlib numpy
python simulation/python/visualization/Visualize_3D.py
```

### 4. Reinforcement / Gait Learning Script
```bash
python simulation/python/locomotion/MAGI_gait_learning.py
```
