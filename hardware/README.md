# 🦾 MAGI Hardware & Mechanical Subsystem

Comprehensive manufacturing, mechanical CAD, bill of materials (BOM), 3D printable components, and ROS 2 URDF package for the 12-DOF MAGI Quadruped Robot.

---

## 📐 Directory Structure

```
hardware/
├── cad/                              Master 3D CAD Projects
│   ├── MAGI.3mf                      Full 3MF assembly project with slicing presets & plate layouts
│   └── Ass servo.SLDPRT              SolidWorks servo bracket assembly part
├── bom/                              Bill of Materials & Sourcing
│   └── bom-export-20260817T145942.csv Itemized component list, quantities, and specifications
├── stl/                              Production 3D Print Meshes
│   ├── 42zlmowk6v3y-Body_Frame.stl   Main chassis enclosure
│   ├── 3ozjznhu8j9f-Bottom_Cover.stl Base plate with ventilation & mount points
│   ├── s4yj81t6fxf0-Top_Cover.stl    Top canopy enclosure
│   ├── 3255p1l9eea4-Leg.stl          3-DOF leg links (Coxa, Femur, Tibia)
│   ├── 81e22so03fes-Leg-Body_Connector.stl Hip joint pivot bracket
│   ├── u01tkdwts72r-Foot.stl         High-grip foot contact interface
│   └── y3t8uh5qiyna-Camera_Cover.stl Forward multispectral camera hood
├── docs/                             Mathematical & Kinematic Specifications
│   └── leg_FK_IK_math_and_python.pdf Forward & Inverse Kinematics analytical derivation
└── urdf/                             ROS 2 Robot Description Package
    └── MAGI_Assembly_URDF_description/
        ├── urdf/                     MAGI_Assembly_URDF.urdf & .xacro
        ├── meshes/                   Visual and collision STL/DAE meshes
        ├── launch/                   ROS 2 launch files (display.launch.py)
        ├── rviz/                     RViz configuration profiles
        ├── CMakeLists.txt            Colcon build descriptor
        └── package.xml               Ament package metadata
```

---

## 🖨️ 3D Printing Recommendations

| Parameter | Recommended Specification |
|---|---|
| **Material** | **PLA** or **ABS/ASA** (PLA is not recommended due to heat dissipation near MG996R servos) |
| **Layer Height** | 0.20 mm (Standard Quality) |
| **Infill Density** | 40% – 50% (Gyroid or Cubic for multidirectional rigidity) |
| **Perimeters / Walls** | Minimum 4 perimeters (Crucial for servo mount screw threads) |
| **Top / Bottom Layers** | 5 top, 5 bottom layers |
| **Supports** | Tree supports enabled on 55° overhangs for leg brackets |

---

## 🔩 Bill of Materials (BOM) Highlights

| Component | Part / Spec | Quantity | Purpose |
|---|---|:---:|---|
| **Main SBC** | Raspberry Pi 4B (4 GB) | 1 | Runs MAGI OS & 3 AI inference models |
| **Microcontroller** | ESP32-WROOM-32 (38-pin) | 1 | 240 MHz dual-core real-time IK solver |
| **Servo Motors** | TowerPro MG996R Metal Gear (11 kg-cm) | 12 | 3-DOF joint actuation per leg |
| **PWM Driver** | PCA9685 16-Channel 12-bit I²C | 1 | Offloads servo PWM generation from MCU |
| **IMU** | MPU-6050 (6-DOF Gyro + Accel) | 1 | Pitch/roll orientation & fall detection |
| **Power Converter** | UMR / UCTRONICS Step-down Buck Converter (5V / 8A) | 1 | Dedicated high-amperage servo power |
| **Battery** | 3S LiPo (11.1V, 2200–3000 mAh) | 1 | Main system power source |
| **Fasteners** | M3 & M2.5 Stainless Steel Bolts & Locknuts | Assorted | Chassis & servo horn fastening |

Full itemized export available in [`hardware/bom/bom-export-20260817T145942.csv`](bom/bom-export-20260817T145942.csv).

---

## 🤖 ROS 2 URDF Integration

The `hardware/urdf/MAGI_Assembly_URDF_description/` package provides standard ROS 2 kinematics descriptions:

```bash
# Build the URDF package in your ROS 2 colcon workspace:
cd ~/ros2_ws
colcon build --packages-select MAGI_Assembly_URDF_description
source install/setup.bash

# Visualize the robot model and TF trees in RViz:
ros2 launch MAGI_Assembly_URDF_description display.launch.py
```
