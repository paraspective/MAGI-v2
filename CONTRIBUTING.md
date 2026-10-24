# Contributing to MAGI

Thank you for your interest in contributing to the **MAGI (Multispectral Autonomous Ground Intelligence)** project!

MAGI is a modular, multi-core quadruped robotics platform combining custom embedded Linux middleware (MAGI OS), ESP32 C++ firmware, Three.js WebGL simulation, and edge computer vision.

---

## 🏛️ Repository Architecture & Guidelines

Before submitting contributions, review our organizational architecture:

1. **`hardware/` (Present)**: Production CAD, verified STLs, BOM, and the active ROS 2 URDF description package.
2. **`firmware/` (Present)**: ESP32 PlatformIO C++ firmware (kinematics, gait engine, IMU, PCA9685).
3. **`OS/` (Present)**: Core ZeroMQ middleware and multi-process AI inference nodes for Raspberry Pi 4B.
4. **`simulation/` (Present)**: Three.js WebGL browser simulator and PyBullet kinematics/RL trainers.
5. **`perception/` (Present)**: PiCamera streaming and MLOps plant pathology training/inference pipeline.
6. **`archive/` (Past)**: Historical CAD prototypes, deprecated URDF iterations, legacy scripts, and attributed open-source references.
7. **`ROADMAP.md` & `TODO.md` (Future)**: Active engineering backlog and project milestones.

---

## 🌿 Git & Branching Workflow

1. **Fork and Clone**:
   ```bash
   git clone https://github.com/paraspective/MAGI-Development.git
   cd MAGI-Development
   ```

2. **Branch Naming**:
   - `feature/<subsystem>-<short-description>` (e.g. `feature/firmware-checksum`, `feature/simulation-terrain`)
   - `fix/<subsystem>-<bug>` (e.g. `fix/os-zmq-reconnect`)
   - `docs/<topic>` (e.g. `docs/kinematics-equations`)

3. **Commit Messages**:
   Follow [Conventional Commits](https://www.conventionalcommits.org/):
   - `feat(firmware): add crc16 validation to uart protocol`
   - `fix(os): resolve posix shared memory unmap leak`
   - `docs(hardware): update 3d printing slicer profile parameters`

4. **Code Quality**:
   - Python code must conform to PEP 8 standards.
   - C++ firmware must compile cleanly via `pio run` without compiler warnings.
   - Files over 50 MB should not be checked into Git without maintainer approval.
