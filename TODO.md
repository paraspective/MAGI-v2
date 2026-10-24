# 📝 MAGI Engineering Task Tracker (TODO)

This document tracks active development tasks, classified by subsystem and urgency, for contributors and core maintainers.

---

## ⚡ High-Priority Tasks (Current Sprint)

### Hardware & Mechanical Subsystem (`hardware/`)
- [ ] **Physical Print & Slicing**: Batch slice the remaining top cover and camera hood using PETG (40% gyroid infill).
- [ ] **Wiring Harness**: Assemble the braided power harness with XT60 connector from 3S LiPo to the step-down buck regulator.
- [ ] **Servo Centering**: Assemble aluminum servo horns with servos powered and commanded to neutral 90° position.

### Firmware & Joint Controller (`firmware/`)
- [ ] **Serial Checksum Validation**: Add CRC16 packet checksums to the UART protocol between Pi and ESP32.
- [ ] **Dynamic Gait Transition**: Implement smooth trajectory blending when switching between Trot (medium speed) and Crawl (rough terrain).
- [ ] **IMU Auto-Leveling**: Feed pitch/roll error back into the leg Z-height offset to maintain level chassis attitude on slopes.

### MAGI OS & Middleware (`OS/`)
- [ ] **Hardware Pi4 Validation**: Deploy the `OS/setup/` 4-stage scripts onto a physical Raspberry Pi 4B micro-SD card.
- [ ] **Systemd Verification**: Enable `magi-watchdog.service` and verify automatic node respawn on simulated process crash.
- [ ] **ZeroMQ QoS Tuning**: Benchmark message loss under high-frequency sensor publishing (100 Hz IMU data stream).

### Perception & MLOps (`perception/`)
- [ ] **Live Camera Feed Integration**: Pipe zero-copy shared memory frames directly into `perception/mlops/app.py`.
- [ ] **ExG Soil Filter Optimization**: Profile the NumPy ExG masking step on ARM Cortex-A72 to ensure < 15 ms latency.
- [ ] **GPS Metadata Tagging**: Add NMEA sentence parsing to tag each frame's spatial health score with field coordinates.

### Simulation & Web Visualizer (`simulation/`)
- [ ] **Preset Export**: Add a "Save to ESP32 Format" button in `simulation/web/rl_train.js` that outputs C++ header arrays.
- [ ] **Foot Contact Indicator**: Add visual color changes (green/red) to the Three.js foot spheres when in contact with ground plane.

---

## 📋 Medium-Term Tasks

- [ ] **Gazebo Model**: Port `hardware/urdf/MAGI_Assembly_URDF_description` to Gazebo Harmonic with ros2_control integration.
- [ ] **Battery State of Charge Monitor**: Add ADS1115 ADC read on the I²C bus to publish battery voltage to Caspar.
- [ ] **IEEE Paper Finalization**: Populate experimental figures and timing tables into [`paper/main.tex`](paper/main.tex).

---

## 🔮 Long-Term & Exploration

- [ ] **Thermal Imaging Sensor**: Evaluate FLIR Lepton 3.5 module over SPI for water stress detection in crops.
- [ ] **Multi-Robot Swarm Communication**: Implement decentralized ad-hoc WiFi mesh protocol for multi-MAGI fleet coordination.
