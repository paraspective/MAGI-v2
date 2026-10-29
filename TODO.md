# Engineering Task Tracker (TODO)

Active engineering tasks organized by subsystem.

---

## High Priority (Active Sprint)

### Hardware & Mechanical Subsystem (`hardware/`)
- [ ] Assemble braided power harness with XT60 connector from 3S LiPo to dual buck converters.
- [ ] Servo centering: assemble aluminum horns with servos commanded to neutral 90° position.
- [ ] Complete printing of protective top canopy cover.

### Firmware & Joint Controller (`firmware/`)
- [ ] Add CRC16 packet checksums to UART communication protocol between Pi and ESP32.
- [ ] Implement smooth trajectory blending when switching between Trot and Crawl gaits.
- [ ] Feed IMU roll/pitch error into leg Z-offset for active body leveling on inclines.

### MAGI OS & Middleware (`OS/`)
- [ ] Run full bringup sequence on fresh Raspberry Pi OS Lite SD card via `OS/setup/` scripts.
- [ ] Validate `magi-watchdog.service` auto-restart under simulated node crashes.
- [ ] Benchmark ZeroMQ topic drop rate under 100 Hz IMU telemetry streaming.

### Perception & MLOps (`perception/`)
- [ ] Pipe zero-copy shared memory frames directly into `perception/mlops/app.py`.
- [ ] Profile ExG soil mask calculation on ARM Cortex-A72 to maintain <15 ms latency.
- [ ] Add NMEA GPS string parsing to tag image frame health scores with coordinates.

### Simulation (`simulation/`)
- [ ] Add export button in `simulation/web/rl_train.js` to serialize best genome to C++ `config.h`.
- [ ] Add visual contact indicators on foot spheres in Three.js when touching ground plane.

---

## Medium Priority

- [ ] Add ADS1115 I2C ADC monitoring for 3S LiPo battery state-of-charge reporting to Caspar.
- [ ] Populate hardware timing tables and benchmark figures in [`docs/paper/main.tex`](docs/paper/main.tex).
- [ ] Prepare Gazebo Harmonic simulation world with agricultural furrows.

---

## Long Term

- [ ] Evaluate SPI thermal camera module for crop canopy water-stress detection.
- [ ] Multi-robot wireless mesh protocol for cooperative field monitoring.
