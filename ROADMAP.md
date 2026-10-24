# 🗺️ MAGI Development Roadmap & Milestones

This document outlines the strategic engineering roadmap for the MAGI Quadruped Robot, systematically classifying past achievements, active engineering milestones, and upcoming work.

---

## 🧭 Milestone Overview Matrix

| Milestone | Phase Name | Focus Area | Status | Target Delivery |
|:---:|---|---|:---:|:---:|
| **M1** | Foundations & Kinematics | 3-DOF analytical IK, CAD baseline, servo testing | ✅ Completed | Q1 2026 |
| **M2** | Embedded Joint Controller | ESP32 PlatformIO firmware, Bézier trajectories, PCA9685 | ✅ Completed | Q2 2026 |
| **M3** | MAGI OS & Middleware | Custom ZeroMQ XPUB/XSUB broker, POSIX shared memory, Pi4 pinning | ✅ Completed | Q3 2026 |
| **M4** | WebGL Digital Twin | Three.js zero-install simulator, GA gait evolution, Caspar UI | 🔄 Active | Q4 2026 |
| **M5** | Multispectral Vision | 6-channel plant pathology MLOps pipeline, TFLite export | 🔄 Active | Q4 2026 |
| **M6** | Physical System Integration | 3S LiPo power distribution, servo horn calibration, Pi-to-ESP32 UART | ⏳ Next | Q1 2027 |
| **M7** | Autonomous Crop Navigation | In-row traversal, obstacle avoidance, continuous canopy scanning | 📋 Planned | Q2 2027 |
| **M8** | Academic Publication | IEEE journal/conference paper submission, open-source dataset | 📋 Planned | Q3 2027 |
| **M9** | Multi-Agent Swarm Intelligence | Decentralized MAGI consensus across multi-robot field deployments | 🔮 Future | 2028+ |

---

## 📌 Phase-by-Phase Technical Breakdown

### Phase 1: Foundations & Kinematics (M1 — Completed)
- [x] Analytical derivation of 3-DOF Forward and Inverse Kinematics for quadruped leg geometry.
- [x] Initial CAD models of Coxal, Femoral, and Tibial links in Fusion 360 / SolidWorks.
- [x] Prototype servo plate testing and tolerance optimization for TowerPro MG996R servos.
- [x] Kinematic simulation validation in Python and PyBullet.

### Phase 2: Embedded Joint Controller (M2 — Completed)
- [x] High-frequency dual-core ESP32 C++ firmware architecture using FreeRTOS.
- [x] Closed-form 3-DOF IK solver executing in under 0.8 ms per 4-leg cycle.
- [x] Continuous Bézier swing-phase foot trajectory generation (Crawl, Trot, and Bound patterns).
- [x] PCA9685 16-channel 12-bit I²C servo driver implementation.
- [x] MPU-6050 6-DOF IMU complementary filtering for dynamic body pitch/roll stabilization.
- [x] High-speed UART serial command parsing (115,200 baud) with packet checksums.

### Phase 3: MAGI OS & Multi-Core Middleware (M3 — Completed)
- [x] Custom Linux OS distribution configuration for Raspberry Pi 4B (under 180 MB boot footprint).
- [x] ROS2-grade ZeroMQ XPUB/XSUB broker operating with only 22 MB RAM overhead.
- [x] Zero-copy POSIX shared memory frame pipeline for 1080p camera frames.
- [x] Process-level CPU core affinity:
  - **Core 0**: Sensor Hub & I/O
  - **Core 1**: Melchior (YOLOv8-nano / MobileNetV2 detection)
  - **Core 2**: Balthasar (Scene classification & anomaly detection)
  - **Core 3**: Caspar (Sensor fusion, decision state machine, UART output)
- [x] Diagnostics node, QoS profiles, TF2 coordinate transform registry, and SQLite recorder.

### Phase 4: WebGL Digital Twin & Genetic Training (M4 — Active)
- [x] Client-side Three.js WebGL 3D robot visualizer running at 60 FPS in standard web browsers.
- [x] Client-side Genetic Algorithm for 12-parameter gait optimization.
- [x] PyBullet physics backend for rigid-body contact verification.
- [ ] Export optimized genome directly into ESP32 `config.h` via web interface.
- [ ] Implement domain randomization for simulated terrain slope and ground friction variations.

### Phase 5: Multispectral Vision & Canopy Pathology (M5 — Active)
- [x] 6-channel spectral input formulation: RGB + Excess Green (ExG) + GRVI + CIE L*.
- [x] End-to-end MLOps pipeline: Data Ingestion, Validation, Transformation, Model Trainer, Evaluation, Pusher.
- [x] Automated soil pre-filtering reducing inference load by ~40%.
- [x] Quantized float16 TFLite model generation benchmarked for Pi 4B XNNPACK runtime.
- [ ] Integrate thermal / near-infrared sensor input alongside RGB camera.
- [ ] Deploy spatial GPS heatmap visualization onto field mapping interface.

### Phase 6: Physical System Integration & Field Trials (M6 & M7 — What Is To Be Done)
- [ ] Wire the 5V / 8A dual buck converter system with 3S LiPo battery for physical robot.
- [ ] Physical servo zero-point calibration routine via ESP32 EEPROM storage.
- [ ] Bench test continuous walking gait on flat indoor surfaces.
- [ ] Conduct field trials traversing agricultural soil and crop rows.
- [ ] Validate Caspar autonomous decision engine: real-time `TRACK`, `ALERT`, and `EMERGENCY STOP` triggers.

### Phase 7: Scientific Dissemination (M8 — What Is To Be Done)
- [ ] Complete full IEEE-formatted publication draft located at [`paper/main.tex`](paper/main.tex).
- [ ] Compile experimental latency benchmarks: ZeroMQ vs ROS2 DDS, and CPU core utilization profiles.
- [ ] Open-source release of the MAGI Precision Canopy Dataset.
- [ ] Submit manuscript to IEEE Robotics and Automation Letters (RA-L) / IROS.
