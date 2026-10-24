# 🛠️ MAGI Developer Tools & Diagnostic Dashboards

Diagnostic tools, telemetry monitors, and debugging utilities for the MAGI robot.

---

## 🖥️ Available Tools

### 1. Unified Telemetry Dashboard
* **Location**: [`tools/dashboards/Dashboard.py`](dashboards/Dashboard.py)
* **Functionality**:
  - Subscribes to the ZeroMQ message bus (`ipc:///tmp/magi/pub.ipc` or TCP).
  - Displays real-time joint angles, IMU orientation (roll/pitch/yaw), node heartbeat latencies, and Caspar decision states.

### Running the Dashboard:
```bash
python tools/dashboards/Dashboard.py
```
