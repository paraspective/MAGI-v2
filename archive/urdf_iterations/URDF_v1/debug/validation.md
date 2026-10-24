# Validation Report: MAGI_Assemblyy

## Status: PASS

## Summary

| Metric | Value |
|--------|-------|
| Links | 27 |
| Joints | 26 |
| Assemblies | 1 |
| Root | `base_link` |
| Errors | 0 |
| Warnings | 0 |

## Kinematic Tree

```
base_link [primitive]
  └─ Rigid_1 [fixed]
    HexapodV3Mid [primitive]
      └─ Rigid_2 [fixed]
        HexapodV3Top [primitive]
          └─ Rigid_4 [fixed]
            MAGI_Assemblyy_MG996R_servo [primitive]
              └─ Revolute_5 [revolute]
                MAGI_Assemblyy_HQpod_Coxal_Left_v2 [BAKE] [primitive]
                  └─ Rigid_6 [fixed]
                    MAGI_Assemblyy_MG996R_servo_6 [primitive]
                      └─ Revolute_7 [revolute]
                        MAGI_Assemblyy_HQpod_Femur [BAKE] [primitive]
                          └─ Revolute_8 [revolute]
                            MAGI_Assemblyy_MG996R_servo_7 [BAKE] [primitive]
                              └─ Rigid_32 [fixed]
                                MAGI_Assemblyy_HQpod_Tibia_Left_New_2 [primitive]
          └─ Rigid_10 [fixed]
            MAGI_Assemblyy_MG996R_servo_8 [primitive]
              └─ Revolute_12 [revolute]
                MAGI_Assemblyy_HQpod_Coxal_Left_v2_2 [BAKE] [primitive]
                  └─ Rigid_13 [fixed]
                    MAGI_Assemblyy_MG996R_servo_9 [primitive]
                      └─ Revolute_14 [revolute]
                        MAGI_Assemblyy_HQpod_Femur_2 [BAKE] [primitive]
                          └─ Revolute_15 [revolute]
                            MAGI_Assemblyy_MG996R_servo_10 [BAKE] [primitive]
                              └─ Rigid_31 [fixed]
                                MAGI_Assemblyy_HQpod_Tibia_Left_New [primitive]
          └─ Rigid_17 [fixed]
            MAGI_Assemblyy_MG996R_servo_11 [primitive]
              └─ Revolute_18 [revolute]
                MAGI_Assemblyy_HQpod_Coxal_Right_v2 [BAKE] [primitive]
                  └─ Rigid_19 [fixed]
                    MAGI_Assemblyy_MG996R_servo_12 [primitive]
                      └─ Revolute_20 [revolute]
                        MAGI_Assemblyy_HQpod_Femur_3 [BAKE] [primitive]
                          └─ Revolute_21 [revolute]
                            MAGI_Assemblyy_MG996R_servo_2 [BAKE] [primitive]
                              └─ Rigid_34 [fixed]
                                MAGI_Assemblyy_HQpod_Tibia_Right_New_2 [primitive]
          └─ Rigid_29 [fixed]
            MAGI_Assemblyy_MG996R_servo_5 [primitive]
              └─ Revolute_24 [revolute]
                MAGI_Assemblyy_HQpod_Coxal_Right_v2_2 [BAKE] [primitive]
                  └─ Rigid_25 [fixed]
                    MAGI_Assemblyy_MG996R_servo_4 [primitive]
                      └─ Revolute_26 [revolute]
                        MAGI_Assemblyy_HQpod_Femur_4 [BAKE] [primitive]
                          └─ Revolute_27 [revolute]
                            MAGI_Assemblyy_MG996R_servo_3 [BAKE] [primitive]
                              └─ Rigid_33 [fixed]
                                MAGI_Assemblyy_HQpod_Tibia_Right_New [primitive]
```

## Collision Geometry

| Link | Source | Shape/File |
|------|--------|------------|
| `HexapodV3Mid` | primitive STL | box |
| `HexapodV3Top` | primitive STL | box |
| `MAGI_Assemblyy_HQpod_Coxal_Left_v2` | primitive STL | box |
| `MAGI_Assemblyy_HQpod_Coxal_Left_v2_2` | primitive STL | box |
| `MAGI_Assemblyy_HQpod_Coxal_Right_v2` | primitive STL | box |
| `MAGI_Assemblyy_HQpod_Coxal_Right_v2_2` | primitive STL | box |
| `MAGI_Assemblyy_HQpod_Femur` | primitive STL | box |
| `MAGI_Assemblyy_HQpod_Femur_2` | primitive STL | box |
| `MAGI_Assemblyy_HQpod_Femur_3` | primitive STL | box |
| `MAGI_Assemblyy_HQpod_Femur_4` | primitive STL | box |
| `MAGI_Assemblyy_HQpod_Tibia_Left_New` | primitive STL | cylinder |
| `MAGI_Assemblyy_HQpod_Tibia_Left_New_2` | primitive STL | cylinder |
| `MAGI_Assemblyy_HQpod_Tibia_Right_New` | primitive STL | cylinder |
| `MAGI_Assemblyy_HQpod_Tibia_Right_New_2` | primitive STL | cylinder |
| `MAGI_Assemblyy_MG996R_servo` | primitive STL | box |
| `MAGI_Assemblyy_MG996R_servo_10` | primitive STL | box |
| `MAGI_Assemblyy_MG996R_servo_11` | primitive STL | box |
| `MAGI_Assemblyy_MG996R_servo_12` | primitive STL | box |
| `MAGI_Assemblyy_MG996R_servo_2` | primitive STL | box |
| `MAGI_Assemblyy_MG996R_servo_3` | primitive STL | box |
| `MAGI_Assemblyy_MG996R_servo_4` | primitive STL | box |
| `MAGI_Assemblyy_MG996R_servo_5` | primitive STL | box |
| `MAGI_Assemblyy_MG996R_servo_6` | primitive STL | box |
| `MAGI_Assemblyy_MG996R_servo_7` | primitive STL | box |
| `MAGI_Assemblyy_MG996R_servo_8` | primitive STL | box |
| `MAGI_Assemblyy_MG996R_servo_9` | primitive STL | box |
| `base_link` | primitive STL | box |

## Mesh Bake Offsets

Links where joint frame ≠ component origin. Visual/inertial/collision origins shifted.

| Link | Offset (mm) |
|------|-------------|
| `MAGI_Assemblyy_HQpod_Coxal_Left_v2` | (-790.2, -541.6, 101.0) |
| `MAGI_Assemblyy_HQpod_Femur` | (-512.4, -773.1, -127.7) |
| `MAGI_Assemblyy_MG996R_servo_7` | (-31.1, -95.6, -890.5) |
| `MAGI_Assemblyy_HQpod_Coxal_Left_v2_2` | (888.3, 636.8, 275.4) |
| `MAGI_Assemblyy_HQpod_Femur_2` | (-826.2, -793.2, -127.6) |
| `MAGI_Assemblyy_MG996R_servo_10` | (-258.5, 262.7, -1135.3) |
| `MAGI_Assemblyy_HQpod_Coxal_Right_v2` | (-569.6, 770.0, 275.5) |
| `MAGI_Assemblyy_HQpod_Femur_3` | (186.2, -961.4, -127.0) |
| `MAGI_Assemblyy_MG996R_servo_2` | (-357.3, -93.2, -890.6) |
| `MAGI_Assemblyy_MG996R_servo_3` | (66.5, -74.6, -1134.3) |
| `MAGI_Assemblyy_HQpod_Femur_4` | (-500.3, 980.3, -127.0) |
| `MAGI_Assemblyy_HQpod_Coxal_Right_v2_2` | (668.2, -864.6, 100.8) |
