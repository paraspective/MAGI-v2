# 📐 URDF Evolution & Kinematic Modeling History

This directory documents the progression of the robot's Unified Robot Description Format (URDF) models from initial Fusion 360 / SolidWorks exports to the modern ROS 2 Ament package.

---

## 🗂️ Version Progression

1. **`URDF_initial/` (`URDF_old`)**:
   - The very first automatic URDF export from CAD.
   - Contained raw meshes with uncentered origins and default mass properties.
   - Identified joint axis polarity discrepancies where revolute axes inverted between left and right leg pairs.

2. **`URDF_v1/` (`URDF`)**:
   - Corrected joint rotation frames and established the standardized link hierarchy:
     `base_link -> Coxa -> Femur -> Tibia -> Foot`.
   - Tuned link inertial matrices based on PETG material density estimates.

3. **Current Production URDF**:
   - The current production package is located at [`hardware/urdf/MAGI_Assembly_URDF_description/`](../../hardware/urdf/MAGI_Assembly_URDF_description/).
   - Fully compatible with ROS 2 Humble/Iron/Jazzy, Gazebo Harmonic, and PyBullet.
