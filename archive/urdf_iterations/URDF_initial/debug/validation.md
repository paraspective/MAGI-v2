# Validation Report: MAGI_Assembly_URDF

## Status: PASS (with warnings)

## Summary

| Metric | Value |
|--------|-------|
| Links | 23 |
| Joints | 22 |
| Assemblies | 1 |
| Root | `base_link` |
| Errors | 0 |
| Warnings | 4 |

## Warnings

- Joint 'Revolute_18' is internal to a rigid group (both endpoints → MAGI_Assembly_URDF/HQpod_Coxal_Right_v2).  Dropped — rigid groups represent one rigid body, joints between members are ignored.  Move this joint to assemble between rigid groups instead.
- Joint 'Revolute_20' is internal to a rigid group (both endpoints → MAGI_Assembly_URDF/HQpod_Coxal_Right_v2).  Dropped — rigid groups represent one rigid body, joints between members are ignored.  Move this joint to assemble between rigid groups instead.
- Joint 'Revolute_21' is internal to a rigid group (both endpoints → MAGI_Assembly_URDF/HQpod_Coxal_Right_v2).  Dropped — rigid groups represent one rigid body, joints between members are ignored.  Move this joint to assemble between rigid groups instead.
- Zero-mass links: ['MAGI_Assembly_URDF_HQpod_Tibia_Left', 'MAGI_Assembly_URDF_HQpod_Tibia_Left_2', 'HQpod_Tibia_Right']

## Kinematic Tree

```
base_link [primitive]
  └─ Rigid_1 [fixed]
    HexapodV3Mid [primitive]
      └─ Rigid_2 [fixed]
        HexapodV3Top [primitive]
          └─ Rigid_4 [fixed]
            MAGI_Assembly_URDF_MG996R_servo [primitive]
              └─ Revolute_5 [revolute]
                MAGI_Assembly_URDF_HQpod_Coxal_Left_v2 [BAKE] [primitive]
                  └─ Rigid_6 [fixed]
                    MAGI_Assembly_URDF_MG996R_servo_5 [primitive]
                      └─ Revolute_7 [revolute]
                        MAGI_Assembly_URDF_HQpod_Femur [BAKE] [primitive]
                          └─ Revolute_8 [revolute]
                            MAGI_Assembly_URDF_MG996R_servo_6 [BAKE] [primitive]
                              └─ Rigid_9 [fixed]
                                MAGI_Assembly_URDF_HQpod_Tibia_Left [primitive]
          └─ Rigid_10 [fixed]
            MAGI_Assembly_URDF_MG996R_servo_7 [primitive]
              └─ Rigid_11 [fixed]
                MAGI_Assembly_URDF_HQpod_Coxal_Right_v2 [primitive]
              └─ Revolute_12 [revolute]
                MAGI_Assembly_URDF_HQpod_Coxal_Left_v2_2 [BAKE] [primitive]
                  └─ Rigid_13 [fixed]
                    MAGI_Assembly_URDF_MG996R_servo_8 [primitive]
                      └─ Revolute_14 [revolute]
                        MAGI_Assembly_URDF_HQpod_Femur_2 [BAKE] [primitive]
                          └─ Revolute_15 [revolute]
                            MAGI_Assembly_URDF_MG996R_servo_9 [BAKE] [primitive]
                              └─ Rigid_16 [fixed]
                                MAGI_Assembly_URDF_HQpod_Tibia_Left_2 [primitive]
          └─ Rigid_17 [fixed]
            MAGI_Assembly_URDF_HQpod_Coxal_Right_v2_2 [primitive]
          └─ Rigid_29 [fixed]
            MAGI_Assembly_URDF_MG996R_servo_4 [primitive]
              └─ Revolute_24 [revolute]
                MAGI_Assembly_URDF_HQpod_Coxal_Right_v2_3 [BAKE] [primitive]
                  └─ Rigid_25 [fixed]
                    MAGI_Assembly_URDF_MG996R_servo_3 [primitive]
                      └─ Revolute_26 [revolute]
                        MAGI_Assembly_URDF_HQpod_Femur_3 [BAKE] [primitive]
                          └─ Revolute_27 [revolute]
                            MAGI_Assembly_URDF_MG996R_servo_2 [BAKE] [primitive]
                              └─ Rigid_30 [fixed]
                                HQpod_Tibia_Right [primitive]
```

## Collision Geometry

| Link | Source | Shape/File |
|------|--------|------------|
| `HQpod_Tibia_Right` | primitive STL | box |
| `HexapodV3Mid` | primitive STL | box |
| `HexapodV3Top` | primitive STL | box |
| `MAGI_Assembly_URDF_HQpod_Coxal_Left_v2` | primitive STL | box |
| `MAGI_Assembly_URDF_HQpod_Coxal_Left_v2_2` | primitive STL | box |
| `MAGI_Assembly_URDF_HQpod_Coxal_Right_v2` | primitive STL | box |
| `MAGI_Assembly_URDF_HQpod_Coxal_Right_v2_2` | primitive STL | box |
| `MAGI_Assembly_URDF_HQpod_Coxal_Right_v2_3` | primitive STL | box |
| `MAGI_Assembly_URDF_HQpod_Femur` | primitive STL | box |
| `MAGI_Assembly_URDF_HQpod_Femur_2` | primitive STL | box |
| `MAGI_Assembly_URDF_HQpod_Femur_3` | primitive STL | box |
| `MAGI_Assembly_URDF_HQpod_Tibia_Left` | primitive STL | box |
| `MAGI_Assembly_URDF_HQpod_Tibia_Left_2` | primitive STL | box |
| `MAGI_Assembly_URDF_MG996R_servo` | primitive STL | box |
| `MAGI_Assembly_URDF_MG996R_servo_2` | primitive STL | box |
| `MAGI_Assembly_URDF_MG996R_servo_3` | primitive STL | box |
| `MAGI_Assembly_URDF_MG996R_servo_4` | primitive STL | box |
| `MAGI_Assembly_URDF_MG996R_servo_5` | primitive STL | box |
| `MAGI_Assembly_URDF_MG996R_servo_6` | primitive STL | box |
| `MAGI_Assembly_URDF_MG996R_servo_7` | primitive STL | box |
| `MAGI_Assembly_URDF_MG996R_servo_8` | primitive STL | box |
| `MAGI_Assembly_URDF_MG996R_servo_9` | primitive STL | box |
| `base_link` | primitive STL | box |

## Mesh Bake Offsets

Links where joint frame ≠ component origin. Visual/inertial/collision origins shifted.

| Link | Offset (mm) |
|------|-------------|
| `MAGI_Assembly_URDF_HQpod_Coxal_Left_v2` | (-790.2, -541.6, 101.0) |
| `MAGI_Assembly_URDF_HQpod_Femur` | (-512.4, -773.1, -127.7) |
| `MAGI_Assembly_URDF_MG996R_servo_6` | (-31.1, -95.6, -890.5) |
| `MAGI_Assembly_URDF_HQpod_Coxal_Left_v2_2` | (888.3, 636.8, 275.4) |
| `MAGI_Assembly_URDF_HQpod_Femur_2` | (-826.2, -793.2, -127.6) |
| `MAGI_Assembly_URDF_MG996R_servo_9` | (-258.5, 262.7, -1135.3) |
| `MAGI_Assembly_URDF_MG996R_servo_2` | (66.5, -74.6, -1134.3) |
| `MAGI_Assembly_URDF_HQpod_Femur_3` | (-500.3, 980.3, -127.0) |
| `MAGI_Assembly_URDF_HQpod_Coxal_Right_v2_3` | (668.2, -864.6, 100.8) |
