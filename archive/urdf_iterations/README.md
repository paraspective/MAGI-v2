# URDF Evolution & Kinematic Modeling History

Historical progression of the robot's URDF models across design iterations:

1. **`URDF_initial/`**: Initial CAD export with uncentered origins and default mass properties. Used to verify link conventions.
2. **`URDF_v1/`**: Corrected joint rotation frames and established the standardized link hierarchy (`base_link -> Coxa -> Femur -> Tibia -> Foot`).
3. **`MAGI_iteration3/`**: Intermediate iteration 3 assembly description and repaired STL components before final standardization.
4. **Current Production URDF**: Located at [`hardware/urdf/MAGI_Assembly_URDF_description/`](../../hardware/urdf/MAGI_Assembly_URDF_description/). Standard ROS 2 package with visual and collision meshes, RViz configurations, and launch files.
