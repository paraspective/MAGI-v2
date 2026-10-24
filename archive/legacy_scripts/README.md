# 📜 Early Prototype Scripts (Legacy Baseline)

These standalone scripts represent the earliest prototype code written during the proof-of-concept phase of the MAGI project before the modular multi-core operating system and web simulator were engineered.

---

## 🗂️ Script Inventory & Modern Replacements

| Legacy Script | Description | Modern Modular Replacement |
|---|---|---|
| `MAGI_gait_learning.py` | Monolithic PyBullet reinforcement learning & gait trainer | [`simulation/python/locomotion/MAGI_gait_learning.py`](../../simulation/python/locomotion/MAGI_gait_learning.py) |
| `demo_pybullet.py` | Basic PyBullet physics environment loader | [`simulation/python/pybullet/demo_pybullet.py`](../../simulation/python/pybullet/demo_pybullet.py) |
| `ik.py` / `fk.py` | Initial geometric 3-DOF inverse and forward kinematics | [`simulation/python/kinematics/ik.py`](../../simulation/python/kinematics/ik.py) & [`firmware/magi_esp32/src/kinematics.cpp`](../../firmware/magi_esp32/src/kinematics.cpp) |
| `gait.py` | Analytical foot trajectory generator | [`simulation/python/locomotion/gait.py`](../../simulation/python/locomotion/gait.py) |
| `camera_server.py` | Simple OpenCV MJPEG streaming server | [`perception/camera/camera_server.py`](../../perception/camera/camera_server.py) |
| `Dashboard.py` | Early desktop Tkinter/Matplotlib monitor | [`tools/dashboards/Dashboard.py`](../../tools/dashboards/Dashboard.py) |
| `visualize_2D.py` / `Visualize_3D.py` | Matplotlib 2D/3D leg kinematic visualizers | [`simulation/python/visualization/`](../../simulation/python/visualization/) |

---

## 💡 Modern Architecture

All active development now runs within the **MAGI OS** multi-core architecture (`OS/`), the **PlatformIO ESP32 Firmware** (`firmware/`), and the **Three.js WebGL Digital Twin** (`simulation/web/`).
