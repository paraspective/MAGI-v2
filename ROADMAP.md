# MAGI Development Roadmap

Engineering milestones for the MAGI quadruped robotics platform. Status reflects the current state of physical hardware and software integration.

---

## Milestone Overview

| Milestone | Phase Name | Focus Area | Status | Target Delivery |
|:---:|---|---|:---:|:---:|
| **M1** | Foundations & Kinematics | 3-DOF analytical IK, CAD baseline, servo testing | Completed | Q1 2026 |
| **M2** | Embedded Joint Controller | ESP32 PlatformIO firmware, Bézier trajectories, PCA9685 | Completed | Q2 2026 |
| **M3** | MAGI OS Middleware | Custom ZeroMQ XPUB/XSUB broker, POSIX shared memory, Pi 4 pinning | Completed | Q3 2026 |
| **M4** | WebGL Digital Twin | Three.js zero-install simulator, GA gait evolution | In Progress | Q4 2026 |
| **M5** | Multispectral Vision | 6-channel plant pathology MLOps pipeline, TFLite export | In Progress | Q4 2026 |
| **M6** | Physical Integration | Power distribution, servo calibration, Pi-to-ESP32 UART | In Progress | Q1 2027 |
| **M7** | Autonomous Crop Navigation | In-row traversal, obstacle avoidance, continuous canopy scanning | Planned | Q2 2027 |
| **M8** | Academic Publication | IEEE conference paper submission, open-source dataset | Planned | Q3 2027 |
| **M9** | Multi-Agent Swarm | Decentralized MAGI consensus across multi-robot field deployments | Future | 2028+ |

---

## Detailed Milestone Breakdown

### Phase 1: Foundations & Kinematics (M1 — Completed)
- [x] Closed-form 3-DOF Forward and Inverse Kinematics derivation for quadruped leg geometry.
- [x] CAD models of Coxal, Femoral, and Tibial links modeled and validated in SolidWorks / Fusion 360.
- [x] Prototype servo plate testing and clearance verification for TowerPro MG996R servos.
- [x] Kinematic simulation validation in Python and PyBullet.

### Phase 2: Embedded Joint Controller (M2 — Completed)
- [x] High-frequency dual-core ESP32 C++ firmware architecture using FreeRTOS.
- [x] Closed-form 3-DOF IK solver executing in <0.80 µs per leg at 240 MHz.
- [x] Continuous cubic Bézier swing-phase foot trajectory generator (Crawl, Trot, and Bound).
- [x] PCA9685 16-channel 12-bit I2C servo driver implementation running at 400 kHz.
- [x] MPU-6050 6-axis IMU complementary filtering for dynamic body stabilization.
- [x] High-speed UART serial command parsing (115,200 baud).
- [x] 7-stage progressive bringup test suite (`firmware/pca9685_test/`).

### Phase 3: MAGI OS & Multi-Core Middleware (M3 — Completed)
- [x] Minimal Linux distribution configuration for Raspberry Pi 4B (~180 MB boot footprint).
- [x] Custom ZeroMQ XPUB/XSUB message broker operating with ~22 MB RAM overhead.
- [x] Zero-copy POSIX shared memory frame pipeline for camera frames.
- [x] Process-level CPU core pinning across 4 ARM Cortex-A72 cores:
  - **Core 0:** Sensor Hub & I/O
  - **Core 1:** Melchior (MobileNetV2 foliar detection)
  - **Core 2:** Balthasar (Scene classification & anomaly detection)
  - **Core 3:** Caspar (Sensor fusion, decision state machine, UART output)
- [x] Diagnostics monitor, QoS delivery profiles, TF coordinate transforms, and SQLite telemetry recorder.

### Phase 4: WebGL Digital Twin & Gait Training (M4 — In Progress)
- [x] Three.js WebGL 3D robot visualizer running at 60 FPS in browser.
- [x] Client-side Genetic Algorithm for 12-parameter gait optimization.
- [x] PyBullet physics backend for rigid-body contact verification.
- [ ] Export optimized genome parameters directly into ESP32 `config.h`.
- [ ] Add domain randomization for simulated terrain slope and ground friction.

### Phase 5: Multispectral Vision & Canopy Pathology (M5 — In Progress)
- [x] 6-channel spectral input formulation: RGB + Excess Green (ExG) + GRVI + CIE L*.
- [x] End-to-end MLOps pipeline: Data Ingestion, Validation, Transformation, Model Trainer, Evaluation.
- [x] Soil pre-filtering reducing inference load by ~40% on non-canopy background tiles.
- [x] Quantized float16 TFLite model generation benchmarked for Pi 4B XNNPACK runtime.
- [ ] Pipe shared memory video directly into active perception service.
- [ ] Integrate thermal / near-infrared sensor input alongside RGB camera.

### Phase 6: Physical System Integration & Bench Testing (M6 — Next)
- [ ] Wire the 5V / 6V dual buck converter system with 3S LiPo battery for physical robot.
- [ ] Physical servo zero-point calibration routine via ESP32 EEPROM storage.
- [ ] Bench test continuous walking gait on flat indoor surfaces.
- [ ] Validate Caspar autonomous decision engine: real-time `TRACK`, `ALERT`, and `EMERGENCY STOP` triggers.

### Phase 7: Autonomous Field Navigation (M7 — Planned)
- [ ] In-row traversal through agricultural furrows.
- [ ] Obstacle detection and avoidance using ToF sensors and IMU.
- [ ] Continuous canopy disease scanning during live field trials.

### Phase 8: Scientific Publication (M8 — Planned)
- [ ] Complete full IEEE-formatted publication draft located at [`docs/paper/main.tex`](docs/paper/main.tex).
- [ ] Compile experimental benchmarks: ZeroMQ vs ROS 2 DDS latency and CPU utilization profiles.
- [ ] Open-source release of the MAGI Precision Canopy Dataset.
