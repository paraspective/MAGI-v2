<p align="center">
  <img src="media/magi_quadruped.png" alt="MAGI 12-DOF Quadruped Robot" width="100%" />
</p>

<div align="center">

# MAGI

### Multispectral Autonomous Ground Intelligence

**A 12-DOF Quadruped Robot with Edge AI, Custom ROS2-Grade ZeroMQ OS, and Evolutionary Gait Training**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi%204B%20(4GB)-c51a4a.svg)](#hardware-architecture)
[![MCU](https://img.shields.io/badge/MCU-ESP32--WROOM--32%20(240MHz)-orange.svg)](#firmware--esp32-joint-controller)
[![Middleware](https://img.shields.io/badge/Middleware-Custom%20ZeroMQ%20(22MB%20RAM)-795299.svg)](#magi-os--the-tri-core-brain)
[![Simulation](https://img.shields.io/badge/Simulator-Three.js%20WebGL%20%2B%20PyBullet-brightgreen.svg)](#simulation--evolutionary-gait-training)
[![Research Paper](https://img.shields.io/badge/Paper-IEEE%20Format-yellow.svg)](#-research-reports--academic-publications)

---

*Named after the [MAGI supercomputer](https://evangelion.fandom.com/wiki/MAGI) from Neon Genesis Evangelion — three independent consensus nodes that each reason autonomously across isolated CPU cores and fuse their outputs into a single deterministic decision.*

</div>

---

## 📑 Table of Contents

1. [Executive Summary & Core Problem Solved](#-executive-summary)
2. [Tri-Core Cognitive Architecture (Celebi, Gengar, Lugia / Melchior, Balthasar, Caspar)](#-the-tri-core-cognitive-architecture)
3. [Research Reports & Academic Publications](#-research-reports--academic-publications)
   - [IEEE Conference Paper](#1-ieee-conference-paper)
   - [Architectural Context & ZeroMQ Benchmarks](#2-architectural-context--zeromq-benchmarks)
   - [Analytical Kinematics Derivation (FK & IK)](#3-analytical-forward--inverse-kinematics-derivation)
   - [Mechanical Engineering & Agricultural Feasibility Report](#4-mechanical-engineering--agricultural-feasibility-report)
   - [Multispectral Pathology & Saliency Analysis](#5-multispectral-pathology--saliency-analysis)
4. [Hardware Architecture & Electrical Topology](#-hardware-architecture)
5. [MAGI OS — Embedded Intelligence Platform](#-magi-os--embedded-intelligence-platform)
6. [Firmware & 7-Stage Progressive Hardware Bringup](#-firmware--esp32-joint-controller)
7. [Simulation & Evolutionary Gait Training](#-simulation--evolutionary-gait-training)
8. [End-to-End System Integration & Data Flow](#-end-to-end-system-integration--data-flow)
9. [Project Classification Matrix (Past · Present · Future)](#-project-classification-matrix)
10. [Quick Start & Deployment Guide](#-quick-start--deployment-guide)

---

## 🌟 Executive Summary

**MAGI (Multispectral Autonomous Ground Intelligence)** is an end-to-end autonomous quadrupedal robotics platform designed to solve a critical limitation in precision agriculture:

> **The Core Challenge:** Run **three concurrent deep learning models** and high-frequency real-time inverse kinematics on a **$35 single-board computer (Raspberry Pi 4B, 4GB RAM)** with **zero cloud offloading**, **no discrete GPU**, and **without the prohibitive RAM and latency overhead of ROS 2 / DDS**.

Traditional agricultural monitoring relies on either:
- **Unmanned Aerial Vehicles (UAVs):** Occluded by dense crop foliage; cannot perform under-canopy inspection.
- **Wheeled Ground Vehicles (UGVs):** Confined to flat tractor ruts; fail on muddy furrows, rocks, and uneven crop beds.
- **Industrial Quadrupeds (Boston Dynamics Spot, ANYbotics ANYmal):** Cost \$50,000–\$150,000+ and require high-power workstation GPUs (e.g., NVIDIA Jetson AGX Orin) drawing 50–100W+.

MAGI demonstrates that a **12-DOF walking quadruped** can execute multispectral plant pathology diagnostics, dynamic anomaly classification, and autonomous locomotion entirely within a **30.6% memory footprint (~1252 MB)** on a standard Raspberry Pi 4B and dual-core ESP32.

### What Sets MAGI Apart

| Metric / Feature | Traditional Robotics Stack | MAGI Autonomous Platform |
|---|---|---|
| **Middleware** | ROS 2 Humble + Fast-DDS (~200 MB RAM, 42.4s boot) | **Custom ZeroMQ XPUB/XSUB (22 MB RAM, 7.8s boot)** |
| **Inference Hardware** | NVIDIA Jetson AGX Orin / Discrete GPU | **ARM Cortex-A72 CPU-only with XNNPACK FP16** |
| **Cognitive Framework** | Monolithic multi-threaded process | **3 Isolated Core-Pinned Processes (Evangelion MAGI Trinity)** |
| **Video Ingestion** | DDS image serialization (~35 ms latency) | **POSIX Shared Memory Zero-Copy (~0.2 ms latency)** |
| **Kinematics Engine** | Numerical IK convergence (Eigen / KDL) | **ESP32 Closed-Form Analytical IK (<0.80 µs / leg)** |
| **Gait Optimization** | Hand-tuned trial-and-error PID | **Browser WebGL Genetic Algorithm + PyBullet RL** |
| **Bill of Materials** | > \$10,000 | **< \$350 (Accessible for Smallholder Farmers)** |

---

## 🧠 The Tri-Core Cognitive Architecture

The cognitive framework is inspired by the **MAGI supercomputer** from *Neon Genesis Evangelion* (originally Melchior-1, Balthasar-2, Caspar-3) and implemented under specialized project node codenames (**Celebi**, **Gengar**, and **Lugia**).

Rather than running inference inside a shared Python runtime with Global Interpreter Lock (GIL) thrashing, each system runs as an **independent Linux process pinned to a dedicated physical ARM Cortex-A72 CPU core**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       RASPBERRY PI 4B CPU TOPOLOGY                          │
├─────────────────┬─────────────────┬──────────────────┬──────────────────────┤
│  CORE 0 (I/O)   │  CORE 1 (AI-1)  │  CORE 2 (AI-2)   │    CORE 3 (FUSION)   │
├─────────────────┼─────────────────┼──────────────────┼──────────────────────┤
│  Sensor Hub     │  MELCHIOR       │  BALTHASAR       │  CASPAR              │
│  Camera Capture │  (Celebi)       │  (Gengar)        │  (Lugia)             │
│  ZeroMQ Broker  │  Pathology AI   │  Scene Anomaly   │  Decision & Locomotion│
│  Watchdog & TF  │  MobileNetV2    │  EfficientNet    │  Rule & FSM Engine   │
│  ~180 MB RAM    │  ~300 MB RAM    │  ~200 MB RAM     │  ~150 MB RAM         │
└─────────────────┴─────────────────┴──────────────────┴──────────────────────┘
```

### 1. MAGI-1: Melchior / Celebi (Object & Foliar Pathology AI)
- **CPU Assignment:** Core 1
- **Model Architecture:** 6-Channel MobileNetV2 / YOLOv8-nano (Quantized Float16 TFLite with ARM NEON XNNPACK acceleration)
- **Function:** Real-time in-canopy disease detection (early blight, late blight, leaf curl, powdery mildew) and pest identification.
- **Spectral Pipeline:** Combines RGB with **Excess Green Index ($\text{ExG} = 2G - R - B$)**, **Green-Red Vegetation Index ($\text{GRVI} = \frac{G - R}{G + R}$)**, and **CIE Lightness ($L^*$)**.
- **Soil Pre-Filtering:** Decomposes frame into a $4 \times 3$ grid; tiles with $\text{ExG} < \tau_{\text{soil}}$ bypass neural inference, saving **35%–50% inference compute**.
- **Lifecycle Gating:** Stays in low-power `INACTIVE` state until activated by Gengar upon canopy detection, reducing continuous CPU draw by **34%** and thermal dissipation by **8°C**.

### 2. MAGI-2: Balthasar / Gengar (Scene Context & Anomaly Detection)
- **CPU Assignment:** Core 2
- **Model Architecture:** EfficientNet-Lite TFLite + Dynamic Anomaly Classifier
- **Function:** Macro-level environmental classification, furrow alignment, dynamic terrain slip estimation, and canopy presence confirmation.
- **Continuous Monitoring:** Computes a real-time multimodal anomaly score combining softmax entropy and IMU variance:
  $$\text{Anomaly} = \min\left(1.0, \frac{\mathcal{H}(\text{Softmax})}{3.0} \times (1 + \|\mathbf{a}_{\text{IMU}}\|)\right)$$
- When Gengar confirms `"stable_plant"`, it triggers a lifecycle transition on Melchior/Celebi to begin detailed foliar scanning.

### 3. MAGI-3: Caspar / Lugia (Sensor Fusion & Locomotion Dispatcher)
- **CPU Assignment:** Core 3
- **Architecture:** Asynchronous Deterministic Priority FSM & Probabilistic Fusion Engine
- **Function:** Fuses detections from Celebi, scene states from Gengar, 6-axis IMU pitch/roll, and ToF distance telemetry into unified robot commands.
- **Deterministic Priority Arbitration:**
  - **Priority 10 (EMERGENCY):** Obstacle distance $< 200\text{ mm}$ $\rightarrow$ Immediate servo halt (`STOP\n`), body drop.
  - **Priority 9 (HARDWARE):** Hardware emergency bumper hit $\rightarrow$ Kill PWM power rail.
  - **Priority 6 (ALERT):** Anomaly $> 0.70$ or steep slope $\rightarrow$ Shift to low-clearance stability crawl (`GAIT crawl\n`, `SPEED 30\n`).
  - **Priority 4 (TRACK):** Foliar infection detected $\rightarrow$ Halt crawl, pitch chassis forward to focus camera (`INSPECT\n`).
  - **Priority 0 (IDLE):** Path clear $\rightarrow$ Continuous forward diagonal trot (`GAIT trot\n`, `SPEED 60\n`).

---

## 🔬 Research Reports & Academic Publications

All formal theoretical models, simulation data, and experimental benchmarks are documented in [`paper/`](paper/) and [`docs/research/`](docs/research/):

### 1. IEEE Conference Paper
- **Manuscript:** [`paper/main.tex`](paper/main.tex), [`paper/references.bib`](paper/references.bib)
- **Title:** *"Edge-Optimized Spectral Masking with Lifecycle-Gated Inference for Real-Time Agricultural Diagnostics on a Resource-Constrained Quadruped"*
- **Authors:** Paras Dharmadhikari, Swayam Lute, AjayKumar Nagpure, Monali Chaudhari (*Dept. of Electronics & Telecommunication Engineering, VESIT, Mumbai*)
- **Key Contributions:**
  1. Complete design of the 12-DOF physical quadruped running fully decentralized edge intelligence on a Raspberry Pi 4B and ESP32.
  2. Proof that lifecycle-gated execution yields a **34% drop in average CPU consumption** and **8°C cooler operation** during continuous field trials.
  3. Formal derivation and physical verification of closed-form inverse kinematics executing in $<0.80\,\mu\text{s}$ per limb.

### 2. Architectural Context & ZeroMQ Benchmarks
- **Whitepaper:** [`docs/research/MAGI_ Complete Architectural Context.pdf`](docs/research/MAGI_%20Complete%20Architectural%20Context.pdf)
- **Detailed Findings:**
  - **Memory Footprint:** Linux OS + ZeroMQ + Sensor Hub + 3 AI nodes consume **1252 MB** out of 4096 MB, leaving **2844 MB of free memory headroom (69.4% unallocated)**.
  - **IPC Latency:** ZeroMQ IPC unix sockets achieve $<15\,\mu\text{s}$ message delivery latency vs $120\text{--}450\,\mu\text{s}$ for ROS 2 Fast-DDS.
  - **Startup Time:** MAGI boots from power-on to full AI inference in **7.8 seconds**, compared to **42.4 seconds** for a standard Ubuntu + ROS 2 Humble installation.

```
System Latency Comparison (Boot & IPC):
┌────────────────────────────────────────────────────────┐
│ ROS 2 Humble Boot: 42.4s                               │
├───────────────────────────────┐                        │
│ MAGI OS Boot: 7.8s            │                        │
└───────────────────────────────┴────────────────────────┘
```

### 3. Analytical Forward & Inverse Kinematics Derivation
- **Mathematical Whitepaper:** [`docs/research/leg_FK_IK_math_and_python.pdf`](docs/research/leg_FK_IK_math_and_python.pdf)
- **Kinematic Formulation:**
  For a 3-DOF leg with coxa length $L_1 = 30\text{ mm}$, femur length $L_2 = 90\text{ mm}$, and tibia length $L_3 = 90\text{ mm}$, targeting foot tip $\mathbf{P} = [x, y, z]^T$:
  $$\theta_1 = \text{atan2}(y, x)$$
  $$d = \sqrt{x^2 + y^2} - L_1, \quad L = \sqrt{d^2 + z^2}$$
  $$\theta_3 = \pi - \arccos\left(\frac{L_2^2 + L_3^2 - L^2}{2 L_2 L_3}\right)$$
  $$\theta_2 = \text{atan2}(-z, d) - \arccos\left(\frac{L_2^2 + L^2 - L_3^2}{2 L_2 L}\right)$$
- **Execution Performance:** Because this formulation uses closed-form trigonometry rather than iterative numerical Jacobian inversion, it executes in **$<0.80\,\mu\text{s}$ on the ESP32 (240 MHz)**, guaranteeing deterministic 50 Hz loop execution.
- **Cubic Bézier Swing Trajectories:**
  $$\mathbf{B}(t) = (1-t)^3 \mathbf{P}_0 + 3(1-t)^2 t \mathbf{P}_1 + 3(1-t) t^2 \mathbf{P}_2 + t^3 \mathbf{P}_3, \quad t \in [0, 1]$$
  Guarantees zero vertical touchdown velocity, eliminating mechanical shock on 3D printed joints.

### 4. Mechanical Engineering & Agricultural Feasibility Report
- **Project Report:** [`docs/research/MAGI_Project_Final__.pdf`](docs/research/MAGI_Project_Final__.pdf)
- **Mechanical Specifications:**
  - Total Robot Mass: $1.85\text{ kg}$ (chassis, 12 servos, dual buck converters, 3S LiPo, Pi 4B, ESP32).
  - Maximum Dynamic Payload: $1.20\text{ kg}$ (sensors, multispectral camera arrays, micro-spray nozzle).
  - Servo Torque Budget: TowerPro MG996R generates $11.0\text{ kg}\cdot\text{cm}$ stall torque at $6.0\text{ V}$. Maximum static joint load during single-leg stance phase is $5.4\text{ kg}\cdot\text{cm}$, providing a **Safety Factor of $2.03$**.
  - Infill & Material: PETG at 40% gyroid infill for high torsional stiffness and UV/moisture resistance in farm fields.

### 5. Multispectral Pathology & Saliency Analysis
- **Algorithms & Visualizers:** [`perception/analysis/Heatmap_algo.ipynb`](perception/analysis/Heatmap_algo.ipynb), [`perception/analysis/visauls.py`](perception/analysis/visauls.py)
- **Spectral Preprocessing Chain:**
  1. *Spatial Downsampling:* $640 \times 480 \rightarrow 224 \times 224$ (8× data reduction).
  2. *CLAHE Spectral Normalization:* Contrast Limited Adaptive Histogram Equalization on L-channel ($8 \times 8$ grid, clip limit 2.0) removes uneven canopy shadows.
  3. *ImageNet Channel Normalization:* Standardized zero-mean unit-variance transformation.
- **Field Diagnostic Accuracy:**

| Preprocessing Stage | Accuracy | F1 Score | Latency on Cortex-A72 |
|---|---|---|---|
| Raw uint8 (No Preprocessing) | 89.3% | 0.882 | 187.2 ms |
| + Spatial Downsampling (224×224) | 90.1% | 0.891 | 183.5 ms |
| + CLAHE Spectral Normalization | 95.4% | 0.948 | 186.1 ms |
| + Float32 Rescaling | 95.7% | 0.951 | 186.8 ms |
| **+ Full Spectral Masking Pipeline** | **96.8%** | **0.964** | **124.6 ms (with XNNPACK)** |

---

## ⚡ Hardware Architecture

```
                          ┌───────────────────────────┐
                          │   3S LiPo Battery 11.1V   │
                          │   5200mAh 35C (XT60)      │
                          └─────────────┬─────────────┘
                                        │
                         ┌──────────────┴──────────────┐
                         ▼                             ▼
              XL4016 DC-DC Buck             LM2596 5V Buck
              6.0V / 20A (Peak)             5.0V / 3A Logic
                         │                             │
                         ▼                             ▼
              ┌─────────────────────┐       ┌─────────────────────┐
              │   PCA9685 Driver    │       │   Raspberry Pi 4B   │
              │   (12 PWM Channels) │       │   4GB LPDDR4        │
              └──────────┬──────────┘       │   MAGI OS Brain     │
                         │                  └──────────┬──────────┘
                  12× MG996R                           │
                  Metal-Gear Servos                    │ UART (115200 baud)
                         ▲                             │ GPIO 16 (RX) / 17 (TX)
                         │ I2C (400 kHz)               ▼
              ┌──────────┴──────────┐       ┌─────────────────────┐
              │   MPU-6050 6-Axis   │◄──────│   ESP32-WROOM-32    │
              │   IMU (Shared I2C)  │  I2C  │   Joint Controller  │
              └─────────────────────┘       └─────────────────────┘
```

### Component Bill of Materials

| Subsystem | Part | Specification | Quantity | Role |
|---|---|---|---|---|
| **High-Level Compute** | Raspberry Pi 4B | 4GB LPDDR4, Quad Cortex-A72 @ 1.5GHz | 1 | Runs MAGI OS, ZeroMQ broker, 3 AI models |
| **Joint Controller** | ESP32-WROOM-32 | Dual-core Tensilica Xtensa @ 240MHz | 1 | Real-time IK solver, Bézier generator, UART |
| **Actuators** | TowerPro MG996R | Metal gears, 11 kg·cm torque @ 6V | 12 | 3 DOF per leg × 4 legs |
| **PWM Driver** | PCA9685 | 16-channel 12-bit I2C @ 0x40 (400 kHz) | 1 | Hardware PWM servo signal generator |
| **IMU** | MPU-6050 | 3-axis accelerometer + 3-axis gyro (0x68) | 1 | Pitch/roll balance & terrain anomaly telemetry |
| **Servo Power** | XL4016 Step-Down | DC-DC Buck converter, 6.0V / 20A continuous | 1 | Dedicated high-amperage servo rail |
| **Logic Power** | LM2596 Step-Down | DC-DC Buck converter, 5.0V / 3A | 1 | Regulated power for Raspberry Pi 4B & ESP32 |
| **Battery** | Turnigy 3S LiPo | 11.1V, 5200 mAh, 35C continuous discharge | 1 | Main onboard power supply |
| **Camera** | USB / Pi Camera | V4L2 640×480 BGR @ 30 fps | 1 | Shared memory video acquisition |
| **Structure** | PETG 3D Printed | 40% Gyroid Infill, 0.2mm layer height | 1 set | Lightweight chassis, coxa, femur, tibia links |

---

## 💻 MAGI OS — Embedded Intelligence Platform

MAGI OS delivers a full ROS 2 development paradigm with **89% less overhead** by stripping away Java, DDS XML daemons, and heavy visualization packages:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                             MAGI OS ARCHITECTURE                            │
├─────────────────────────────────────────────────────────────────────────────┤
│  PROCESS LAYER (Core-Pinned Isolation)                                      │
│    Core 0: Sensor Hub + Camera Streaming (POSIX SHM)                        │
│    Core 1: Melchior (Celebi) — Foliar Pathology Diagnostics                 │
│    Core 2: Balthasar (Gengar) — Scene Classification & Motion Anomaly       │
│    Core 3: Caspar (Lugia) — Fusion & Locomotion Decision Engine             │
├─────────────────────────────────────────────────────────────────────────────┤
│  MESSAGING & MIDDLEWARE (Custom ZeroMQ Implementation)                      │
│    • message_bus.py    XPUB/XSUB Broker (Ports 5555/5556, msgpack, 8 MB RAM)│
│    • messages.py       Native Typed DataClasses (10x faster than JSON)       │
│    • lifecycle.py      4-State FSM (UNCONFIGURED/INACTIVE/ACTIVE/FINALIZED) │
│    • qos.py            QoS Profiles (RELIABLE, BEST_EFFORT, TRANSIENT_LOCAL)│
│    • param_server.py   Live Key-Value Runtime Configuration (Port 5558)     │
│    • diagnostics.py    Node Health Aggregator (1 Hz heartbeat on /diag)     │
│    • transforms.py     Quaternion Coordinate Transformation Tree            │
│    • recorder.py       Lightweight SQLite ROSBag-equivalent Telemetry Logger│
├─────────────────────────────────────────────────────────────────────────────┤
│  HARDWARE INTERFACES (pigpio, smbus2, spidev, pyserial, V4L2)               │
├─────────────────────────────────────────────────────────────────────────────┤
│  BASE: Headless Raspberry Pi OS Lite (64-bit Bookworm, Linux 6.x)           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Complete RAM Budget Breakdown

```
Total Memory Allocation: 1252 MB / 4096 MB (30.6% Utilized)
┌──────────────────────────┬────────────┬──────────────────────────────────────┐
│ Subsystem / Component    │ Memory     │ Implementation Details               │
├──────────────────────────┼────────────┼──────────────────────────────────────┤
│ Linux Kernel & Daemons   │ 180 MB     │ Stripped Bookworm 64-bit base        │
│ ZeroMQ XPUB/XSUB Broker  │ 8 MB       │ C-bindings msgpack pub/sub           │
│ ROS2-Equivalent Services │ 14 MB      │ Param server, diag, TF, recorder     │
│ Sensor Hub & Camera I/O  │ 80 MB      │ Hardware pollers & V4L2 capture      │
│ Shared Memory Buffers    │ 320 MB     │ 3-buffer zero-copy mmap frame pool   │
│ MAGI-1 Celebi (TFLite)   │ 300 MB     │ MobileNetV2 6-channel quantized FP16 │
│ MAGI-2 Gengar (TFLite)   │ 200 MB     │ EfficientNet-Lite scene classifier   │
│ MAGI-3 Lugia (Fusion)    │ 150 MB     │ Priority arbitration rule engine     │
├──────────────────────────┼────────────┼──────────────────────────────────────┤
│ TOTAL ACTIVE FOOTPRINT   │ 1252 MB    │ Ultra-stable continuous operation    │
│ FREE HEADROOM BUDGET     │ 2844 MB    │ Available for caching & OS buffers   │
└──────────────────────────┴────────────┴──────────────────────────────────────┘
```

---

## 🛠️ Firmware & ESP32 Joint Controller

The ESP32 firmware ([`firmware/magi_esp32/`](firmware/magi_esp32/)) handles hard real-time kinematics and motor coordination at 50 Hz.

### The 7-Stage Progressive Hardware Bringup Suite
To guarantee electrical safety, calibrate servo angles, and prevent brownouts before walking, MAGI includes a 7-stage firmware test suite:

1. **[`01_pca9685_scan`](firmware/pca9685_test/tests/01_pca9685_scan/main.cpp):** I2C bus scanner discovering PCA9685 at `0x40` and MPU-6050 at `0x68`.
2. **[`02_servo_sweep`](firmware/pca9685_test/tests/02_servo_sweep/main.cpp):** Full range pulse sweep ($500\,\mu\text{s} \rightarrow 2500\,\mu\text{s}$) to calibrate mechanical limits of each MG996R servo.
3. **[`03_all_servos`](firmware/pca9685_test/tests/03_all_servos/main.cpp):** Simultaneous 12-channel wave motion validating the XL4016 6V/20A power rail under full dynamic load.
4. **[`04_imu_read`](firmware/pca9685_test/tests/04_imu_read/main.cpp):** 6-axis gyro/accel telemetry verification with 100 Hz complementary filtering ($0.98 \times \text{gyro} + 0.02 \times \text{accel}$).
5. **[`05_uart_loopback`](firmware/pca9685_test/tests/05_uart_loopback/main.cpp):** 115200 baud ASCII command validation between Raspberry Pi (`uart_test.py`) and ESP32.
6. **[`06_ik_solver`](firmware/pca9685_test/tests/06_ik_solver/main.cpp):** Standalone analytical inverse kinematics solver unit test achieving $<0.80\,\mu\text{s}$ per leg.
7. **[`07_gait_crawl`](firmware/pca9685_test/tests/07_gait_crawl/main.cpp):** Closed-loop crawl gait trajectory execution on physical hardware.

### High-Speed ASCII UART Protocol

| Command | Format | Example | Action Executed by ESP32 |
|---|---|---|---|
| Set Gait | `GAIT <mode>\n` | `GAIT trot\n` | Switches between `crawl`, `trot`, `bound`, and `stand` |
| Set Speed | `SPEED <0-100>\n` | `SPEED 65\n` | Scales stride frequency and step cycle duration |
| Direct Move | `MOVE a0,a1,...,a11\n` | `MOVE 90,45,90...\n` | Direct joint angle override (degrees) |
| Emergency Halt | `STOP\n` | `STOP\n` | Disables PWM pulses; robot enters safe resting pose |
| Home / Calibrate | `HOME\n` | `HOME\n` | Centers all 12 servos at neutral standing angles |
| Request Telemetry | `IMU\n` | `IMU\n` | Responds: `IMU ax,ay,az,gx,gy,gz\n` |
| Health Status | `STATUS\n` | `STATUS\n` | Responds: `OK gen=N temp=C\n` |

---

## 🎮 Simulation & Evolutionary Gait Training

The digital twin ([`simulation/`](simulation/)) allows gait policy development in both browser WebGL and PyBullet physics without risk of hardware wear:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         SIM-TO-REAL GAIT PIPELINE                           │
├─────────────────────────────────────────────────────────────────────────────┤
│  1. BROWSER WebGL DIGITAL TWIN (simulation/index.html)                      │
│     • Three.js 3D Interactive Kinematics & Phase Debugger                   │
│     • Client-Side Genetic Algorithm (50–100 agents, 5-level curriculum)     │
│                                                                             │
│  2. EVOLUTIONARY GAIT OPTIMIZATION (rl_train.js & MAGI_gait_learning.py)   │
│     • Direct Gene Mode: 12 gait parameters evolved per terrain type         │
│     • NNPolicy Mode: 8→16→12 Feedforward Neural Net policy (~300 weights)   │
│     • Multi-Objective Fitness Function:                                     │
│       Fitness = + (v_fwd × 10.0) − 3.5 × (|pitch| + |roll|)                 │
│                 − 0.08 × Σ(Δθ_joints²) + 5.0 × SymmetryScore                │
│                                                                             │
│  3. EXPORT & REAL-WORLD DEPLOYMENT                                          │
│     • Best Genome / Weights exported to JSON (`gait_config.yaml`)           │
│     • Loaded into ESP32 `gait_engine.cpp` for cubic Bézier execution        │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Supported Gait Dynamics

| Gait Mode | Duty Factor | Flight Phase | Phase Sequence | Optimal Field Application |
|---|---|---|---|---|
| **Crawl** | **75%** | None (Static Stability) | $\text{FR} \rightarrow \text{FL} \rightarrow \text{BL} \rightarrow \text{BR}$ | Muddy furrows, rock traversing, steep crop beds |
| **Trot** | **60%** | None (Dynamic Stability)| Diagonal pairs: $(\text{FR}+\text{BL}) \rightarrow (\text{FL}+\text{BR})$ | Level ground scouting, standard furrow inspection |
| **Bound** | **35%** | Yes | Front pair $\rightarrow$ Rear pair | Obstacle clearance, ditch traversal |
| **Gallop** | **40%** | Yes | Staggered rapid impulse bursts | Emergency field retreat / rapid transit |

---

## 🔄 End-to-End System Integration & Data Flow

```
 PHYSICAL WORLD                  RASPBERRY PI 4B (MAGI OS)                   ESP32
 ══════════════                  ═════════════════════════                   ═════
 
 Crop Canopy ──────► USB Camera
                       │
                       ▼
                 camera_capture.py (Core 0)
                       │
                 POSIX Shared Memory (Zero-Copy 640×480 BGR)
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
       melchior.py         balthasar.py
        (Core 1)            (Core 2)
             │                   │
     Spectral Masking    Scene Context &
     CLAHE + ExG Filter  Entropy Anomaly
             │                   │
             ▼                   ▼
       /detections             /scene
             │                   │
             └─────────┬─────────┘
                       │
                       ▼
                   caspar.py (Core 3)
                   Fusion & Priority Arbiter
                   + ToF Dist + IMU Telemetry
                       │
                   /decision
                       │
                       ▼
                 UART Command ("GAIT trot\n", "SPEED 60\n")
                       │
                       └────────────────────────────────────────► uart_protocol.cpp
                                                                        │
                                                                 gait_engine.cpp
                                                                        │
                                                                 kinematics.cpp
                                                                 (3-DOF IK @ 50Hz)
                                                                        │
                                                                 PCA9685 (I2C)
                                                                        │
                                                                 12× Servos Walk
```

---

## 🏛️ Project Classification Matrix

The repository follows a systematic three-lifecycle organization:

| Lifecycle | Directory | Purpose & Key Artifacts |
|---|---|---|
| 🏛️ **PAST** | [`archive/`](archive/) | Historical 3D printed brackets, early URDF tree iterations, monolithic prototype scripts, and open-source baseline references (Regis, SpdrBot, CubeSat). |
| ⚡ **PRESENT** | [`hardware/`](hardware/)<br/>[`firmware/`](firmware/)<br/>[`OS/`](OS/)<br/>[`simulation/`](simulation/)<br/>[`perception/`](perception/)<br/>[`media/`](media/) | Active production codebase: 12-DOF mechanical CAD & ROS 2 URDF, ESP32 FreeRTOS firmware, custom 4-core ZeroMQ Pi OS, Three.js digital twin, and MLOps plant pathology pipeline. |
| 🚀 **FUTURE** | [`ROADMAP.md`](ROADMAP.md)<br/>[`TODO.md`](TODO.md)<br/>[`paper/`](paper/)<br/>[`docs/research/`](docs/research/) | Active engineering backlog, Phase 1–8 milestone deliverables, IEEE conference paper, and agricultural swarm consensus specifications. |

---

## 🚀 Quick Start & Deployment Guide

### 1. Launch 3D Simulation Twin (Zero-Install)
```bash
cd simulation
python3 -m http.server 8765
# Open http://localhost:8765 in any modern browser
```

### 2. Test MAGI OS in Docker (No Hardware Required)
```bash
cd OS/docker
docker compose build
docker compose up -d
docker compose logs -f magi3    # Watch Caspar/Lugia fusion decision logs
```

### 3. Flash ESP32 Firmware
```bash
cd firmware/magi_esp32
pip install platformio
pio run --target upload --upload-port /dev/ttyUSB0
pio device monitor --baud 115200
```

### 4. Deploy to Raspberry Pi 4B
```bash
# Flash Raspberry Pi OS Lite (64-bit Bookworm)
scp -r OS pi@192.168.1.100:~/magi-os
ssh pi@192.168.1.100

sudo bash ~/magi-os/setup/01_strip_os.sh && sudo reboot
sudo bash ~/magi-os/setup/02_install_deps.sh
sudo bash ~/magi-os/setup/03_configure_boot.sh && sudo reboot
sudo bash ~/magi-os/setup/04_install_services.sh

# Start the MAGI Watchdog Supervisor
sudo systemctl start magi-watchdog
```

---

## 📜 Research Citation

If you use MAGI in academic work or robotics research, please cite our conference paper:

```bibtex
@inproceedings{dharmadhikari2026magi,
  title     = {Edge-Optimized Spectral Masking with Lifecycle-Gated Inference for Real-Time Agricultural Diagnostics on a Resource-Constrained Quadruped},
  author    = {Dharmadhikari, Paras and Lute, Swayam and Nagpure, AjayKumar and Chaudhari, Monali},
  booktitle = {Department of Electronics \& Telecommunication Engineering, VESIT},
  year      = {2026},
  url       = {https://github.com/paraspective/MAGI-Development}
}
```

---

## 📄 License

This project is licensed under the MIT License — see the [`LICENSE`](LICENSE) file for details.  
*MAGI — Multispectral Autonomous Ground Intelligence © 2026.*
