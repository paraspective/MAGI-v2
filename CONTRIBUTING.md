# Contributing to MAGI

Contributions to the MAGI quadruped project are welcome. Please review the repository structure and workflow before submitting pull requests.

---

## Repository Structure

- **`firmware/`**: ESP32 C++ PlatformIO application (kinematics, Bézier gait engine, PCA9685, IMU).
- **`hardware/`**: Mechanical CAD assemblies, production 3D print STLs, BOM, and the official ROS 2 URDF package.
- **`OS/`**: Raspberry Pi 4B software stack — ZeroMQ middleware and multi-process AI inference nodes.
- **`perception/`**: Plant pathology computer vision, spectral analysis, and MLOps training pipelines.
- **`simulation/`**: Three.js WebGL browser simulator and PyBullet physics models.
- **`docs/`**: Academic paper draft, mathematical derivations, and technical whitepapers.
- **`archive/`**: Deprecated CAD prototypes, earlier URDF iterations, and reference designs.

---

## Development Workflow

1. **Clone the repository**:
   ```bash
   git clone https://github.com/paraspective/MAGI-v2.git
   cd MAGI-v2
   ```

2. **Branch naming**:
   - `feature/<subsystem>-<description>` (e.g., `feature/firmware-crc16`)
   - `fix/<subsystem>-<bug>` (e.g., `fix/os-shm-cleanup`)
   - `docs/<topic>` (e.g., `docs/kinematics-notes`)

3. **Commit messages**:
   Use standard conventional commits:
   - `feat(firmware): add crc16 validation to uart protocol`
   - `fix(os): handle zmq socket reconnection timeout`
   - `docs(hardware): update 3d printing parameters for petg`

4. **Code standards**:
   - Python code must conform to PEP 8 standards.
   - C++ firmware should compile with `pio run` without warnings.
   - Never commit large binaries (>50MB) or uncompressed datasets directly to Git.
