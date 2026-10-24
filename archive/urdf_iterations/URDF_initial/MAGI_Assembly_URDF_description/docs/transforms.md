# Transformation Matrices - MAGI_Assembly_URDF

Homogeneous transformation matrices between consecutive frames.
Convention: URDF RPY (XYZ extrinsic / ZYX intrinsic).

## Notation

### Frames

| Index | Link |
|-------|------|
| $L_{0}$ | base_link |
| $L_{1}$ | HexapodV3Mid |
| $L_{2}$ | HexapodV3Top |
| $L_{3}$ | MAGI_Assembly_URDF_MG996R_servo |
| $L_{4}$ | MAGI_Assembly_URDF_MG996R_servo_7 |
| $L_{5}$ | MAGI_Assembly_URDF_HQpod_Coxal_Right_v2_2 |
| $L_{6}$ | MAGI_Assembly_URDF_MG996R_servo_4 |
| $L_{7}$ | MAGI_Assembly_URDF_HQpod_Coxal_Left_v2 |
| $L_{8}$ | MAGI_Assembly_URDF_HQpod_Coxal_Right_v2 |
| $L_{9}$ | MAGI_Assembly_URDF_HQpod_Coxal_Left_v2_2 |
| $L_{10}$ | MAGI_Assembly_URDF_HQpod_Coxal_Right_v2_3 |
| $L_{11}$ | MAGI_Assembly_URDF_MG996R_servo_5 |
| $L_{12}$ | MAGI_Assembly_URDF_MG996R_servo_8 |
| $L_{13}$ | MAGI_Assembly_URDF_MG996R_servo_3 |
| $L_{14}$ | MAGI_Assembly_URDF_HQpod_Femur |
| $L_{15}$ | MAGI_Assembly_URDF_HQpod_Femur_2 |
| $L_{16}$ | MAGI_Assembly_URDF_HQpod_Femur_3 |
| $L_{17}$ | MAGI_Assembly_URDF_MG996R_servo_6 |
| $L_{18}$ | MAGI_Assembly_URDF_MG996R_servo_9 |
| $L_{19}$ | MAGI_Assembly_URDF_MG996R_servo_2 |
| $L_{20}$ | MAGI_Assembly_URDF_HQpod_Tibia_Left |
| $L_{21}$ | MAGI_Assembly_URDF_HQpod_Tibia_Left_2 |
| $L_{22}$ | HQpod_Tibia_Right |

### Joint Variables

| Variable | Joint | Type | From | To |
|----------|-------|------|------|----|
| $q_{1}$ | Revolute_5 | revolute (rad) | $L_{3}$ | $L_{7}$ |
| $q_{2}$ | Revolute_12 | revolute (rad) | $L_{4}$ | $L_{9}$ |
| $q_{3}$ | Revolute_24 | revolute (rad) | $L_{6}$ | $L_{10}$ |
| $q_{4}$ | Revolute_7 | revolute (rad) | $L_{11}$ | $L_{14}$ |
| $q_{5}$ | Revolute_14 | revolute (rad) | $L_{12}$ | $L_{15}$ |
| $q_{6}$ | Revolute_26 | revolute (rad) | $L_{13}$ | $L_{16}$ |
| $q_{7}$ | Revolute_8 | revolute (rad) | $L_{14}$ | $L_{17}$ |
| $q_{8}$ | Revolute_15 | revolute (rad) | $L_{15}$ | $L_{18}$ |
| $q_{9}$ | Revolute_27 | revolute (rad) | $L_{16}$ | $L_{19}$ |

Shorthand: $c_i = \cos(q_i)$, $s_i = \sin(q_i)$

### Kinematic Tree

```
L0: base_link
  +-- [fixed] Rigid_1
      L1: HexapodV3Mid
        +-- [fixed] Rigid_2
            L2: HexapodV3Top
              |-- [fixed] Rigid_4
              |   L3: MAGI_Assembly_URDF_MG996R_servo
              |     +-- [revolute] Revolute_5 (q1)
              |         L7: MAGI_Assembly_URDF_HQpod_Coxal_Left_v2
              |           +-- [fixed] Rigid_6
              |               L11: MAGI_Assembly_URDF_MG996R_servo_5
              |                 +-- [revolute] Revolute_7 (q4)
              |                     L14: MAGI_Assembly_URDF_HQpod_Femur
              |                       +-- [revolute] Revolute_8 (q7)
              |                           L17: MAGI_Assembly_URDF_MG996R_servo_6
              |                             +-- [fixed] Rigid_9
              |                                 L20: MAGI_Assembly_URDF_HQpod_Tibia_Left
              |-- [fixed] Rigid_10
              |   L4: MAGI_Assembly_URDF_MG996R_servo_7
              |     |-- [fixed] Rigid_11
              |     |   L8: MAGI_Assembly_URDF_HQpod_Coxal_Right_v2
              |     +-- [revolute] Revolute_12 (q2)
              |         L9: MAGI_Assembly_URDF_HQpod_Coxal_Left_v2_2
              |           +-- [fixed] Rigid_13
              |               L12: MAGI_Assembly_URDF_MG996R_servo_8
              |                 +-- [revolute] Revolute_14 (q5)
              |                     L15: MAGI_Assembly_URDF_HQpod_Femur_2
              |                       +-- [revolute] Revolute_15 (q8)
              |                           L18: MAGI_Assembly_URDF_MG996R_servo_9
              |                             +-- [fixed] Rigid_16
              |                                 L21: MAGI_Assembly_URDF_HQpod_Tibia_Left_2
              |-- [fixed] Rigid_17
              |   L5: MAGI_Assembly_URDF_HQpod_Coxal_Right_v2_2
              +-- [fixed] Rigid_29
                  L6: MAGI_Assembly_URDF_MG996R_servo_4
                    +-- [revolute] Revolute_24 (q3)
                        L10: MAGI_Assembly_URDF_HQpod_Coxal_Right_v2_3
                          +-- [fixed] Rigid_25
                              L13: MAGI_Assembly_URDF_MG996R_servo_3
                                +-- [revolute] Revolute_26 (q6)
                                    L16: MAGI_Assembly_URDF_HQpod_Femur_3
                                      +-- [revolute] Revolute_27 (q9)
                                          L19: MAGI_Assembly_URDF_MG996R_servo_2
                                            +-- [fixed] Rigid_30
                                                L22: HQpod_Tibia_Right
```

## Transforms

## Rigid_1

$L_{0}$ **base_link** -> $L_{1}$ **HexapodV3Mid** (fixed)

- **origin xyz**: (0.113207, 1.351156, -0.242) m
- **origin rpy**: (0, 0, 0) rad

### Local Transform

$$
T^{0}_{1} = \begin{bmatrix}
1 & 0 & 0 & 0.113207 \\
0 & 1 & 0 & 1.351156 \\
0 & 0 & 1 & -0.242 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Rigid_2

$L_{1}$ **HexapodV3Mid** -> $L_{2}$ **HexapodV3Top** (fixed)

- **origin xyz**: (-0.074434, -2.851566, 0.152148) m
- **origin rpy**: (0, 0, 0) rad

### Local Transform

$$
T^{1}_{2} = \begin{bmatrix}
1 & 0 & 0 & -0.074434 \\
0 & 1 & 0 & -2.851566 \\
0 & 0 & 1 & 0.152148 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Rigid_4

$L_{2}$ **HexapodV3Top** -> $L_{3}$ **MAGI_Assembly_URDF_MG996R_servo** (fixed)

- **origin xyz**: (0.054925, 2.437386, 0.211602) m
- **origin rpy**: (1.570796, 0, 0.785398) rad

### Local Transform

$$
T^{2}_{3} = \begin{bmatrix}
0.707107 & 0 & 0.707107 & 0.054925 \\
0.707107 & 0 & -0.707107 & 2.437386 \\
0 & 1 & 0 & 0.211602 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Rigid_10

$L_{2}$ **HexapodV3Top** -> $L_{4}$ **MAGI_Assembly_URDF_MG996R_servo_7** (fixed)

- **origin xyz**: (0.243915, 2.588642, 0.211602) m
- **origin rpy**: (1.570796, 0, -2.356194) rad

### Local Transform

$$
T^{2}_{4} = \begin{bmatrix}
-0.707107 & 0 & -0.707107 & 0.243915 \\
-0.707107 & 0 & 0.707107 & 2.588642 \\
0 & 1 & 0 & 0.211602 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Rigid_17

$L_{2}$ **HexapodV3Top** -> $L_{5}$ **MAGI_Assembly_URDF_HQpod_Coxal_Right_v2_2** (fixed)

- **origin xyz**: (0.512995, 2.378974, 0.882978) m
- **origin rpy**: (-1.154975, 1.570793, 2.792527) rad

### Local Transform

$$
T^{2}_{5} = \begin{bmatrix}
-0.000003 & 0.72146 & -0.692456 & 0.512995 \\
0.000001 & -0.692456 & -0.72146 & 2.378974 \\
-1 & -0.000003 & 0.000001 & 0.882978 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Rigid_29

$L_{2}$ **HexapodV3Top** -> $L_{6}$ **MAGI_Assembly_URDF_MG996R_servo_4** (fixed)

- **origin xyz**: (0.054739, 2.588547, 0.210956) m
- **origin rpy**: (1.570796, 0, -0.785398) rad

### Local Transform

$$
T^{2}_{6} = \begin{bmatrix}
0.707107 & 0 & -0.707107 & 0.054739 \\
-0.707107 & 0 & -0.707107 & 2.588547 \\
0 & 1 & 0 & 0.210956 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Revolute_5

$L_{3}$ **MAGI_Assembly_URDF_MG996R_servo** -> $L_{7}$ **MAGI_Assembly_URDF_HQpod_Coxal_Left_v2** (revolute)
  Variable: $q_{1}$

- **origin xyz**: (0.389152, 0.569011, 0.023325) m
- **origin rpy**: (-1.570796, -0.785398, 0) rad
- **axis**: (0, 0, 1)
- **limits**: [-0.593412, 1.570796] rad ([-34deg, 90deg])

### Local Transform

$T^{3}_{7}(q_{1}) = T_{fixed} \cdot R_{axis}(q_{1})$ where:

$$
T_{fixed} = \begin{bmatrix}
0.707107 & 0.707107 & 0 & 0.389152 \\
0 & 0 & 1 & 0.569011 \\
0.707107 & -0.707107 & 0 & 0.023325 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

$$
R_{axis}(q_{1}) = \begin{bmatrix}
c_{1} & -s_{1} & 0 & 0 \\
s_{1} & c_{1} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Rigid_11

$L_{4}$ **MAGI_Assembly_URDF_MG996R_servo_7** -> $L_{8}$ **MAGI_Assembly_URDF_HQpod_Coxal_Right_v2** (fixed)

- **origin xyz**: (-0.271684, 0.672022, 0.032938) m
- **origin rpy**: (-2.725771, 0, -1.570793) rad

### Local Transform

$$
T^{4}_{8} = \begin{bmatrix}
0.000004 & -0.914785 & 0.403941 & -0.271684 \\
-1 & -0.000003 & 0.000001 & 0.672022 \\
0 & -0.403941 & -0.914785 & 0.032938 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Revolute_12

$L_{4}$ **MAGI_Assembly_URDF_MG996R_servo_7** -> $L_{9}$ **MAGI_Assembly_URDF_HQpod_Coxal_Left_v2_2** (revolute)
  Variable: $q_{2}$

- **origin xyz**: (0.525758, 0.394657, 0.025361) m
- **origin rpy**: (1.570796, 0.785398, -3.141593) rad
- **axis**: (0, 0, 1)
- **limits**: [-0.383972, 1.570796] rad ([-22deg, 90deg])

### Local Transform

$T^{4}_{9}(q_{2}) = T_{fixed} \cdot R_{axis}(q_{2})$ where:

$$
T_{fixed} = \begin{bmatrix}
-0.707107 & -0.707107 & 0 & 0.525758 \\
0 & 0 & 1 & 0.394657 \\
-0.707107 & 0.707107 & 0 & 0.025361 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

$$
R_{axis}(q_{2}) = \begin{bmatrix}
c_{2} & -s_{2} & 0 & 0 \\
s_{2} & c_{2} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Revolute_24

$L_{6}$ **MAGI_Assembly_URDF_MG996R_servo_4** -> $L_{10}$ **MAGI_Assembly_URDF_HQpod_Coxal_Right_v2_3** (revolute)
  Variable: $q_{3}$

- **origin xyz**: (-1.315235, 0.571189, 0.010147) m
- **origin rpy**: (-1.570796, 0.785398, 0) rad
- **axis**: (0, 0, 1)
- **limits**: [-1.570796, 0.593412] rad ([-90deg, 34deg])

### Local Transform

$T^{6}_{10}(q_{3}) = T_{fixed} \cdot R_{axis}(q_{3})$ where:

$$
T_{fixed} = \begin{bmatrix}
0.707107 & -0.707107 & 0 & -1.315235 \\
0 & 0 & 1 & 0.571189 \\
-0.707107 & -0.707107 & 0 & 0.010147 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

$$
R_{axis}(q_{3}) = \begin{bmatrix}
c_{3} & -s_{3} & 0 & 0 \\
s_{3} & c_{3} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Rigid_6

$L_{7}$ **MAGI_Assembly_URDF_HQpod_Coxal_Left_v2** -> $L_{11}$ **MAGI_Assembly_URDF_MG996R_servo_5** (fixed)

- **origin xyz**: (-0.300345, -0.298625, -0.573417) m
- **origin rpy**: (-2.077761, -1.570782, 2.848271) rad

### Local Transform

$$
T^{7}_{11} = \begin{bmatrix}
-0.000014 & -0.696501 & -0.717556 & -0.300345 \\
0.000004 & 0.717556 & -0.696501 & -0.298625 \\
1 & -0.000012 & -0.000007 & -0.573417 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Rigid_13

$L_{9}$ **MAGI_Assembly_URDF_HQpod_Coxal_Left_v2_2** -> $L_{12}$ **MAGI_Assembly_URDF_MG996R_servo_8** (fixed)

- **origin xyz**: (0.398051, 0.394361, -0.399161) m
- **origin rpy**: (-2.077761, -1.570782, -0.293322) rad

### Local Transform

$$
T^{9}_{12} = \begin{bmatrix}
0.000014 & 0.696501 & 0.717556 & 0.398051 \\
-0.000004 & -0.717556 & 0.696501 & 0.394361 \\
1 & -0.000012 & -0.000007 & -0.399161 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Rigid_25

$L_{10}$ **MAGI_Assembly_URDF_HQpod_Coxal_Right_v2_3** -> $L_{13}$ **MAGI_Assembly_URDF_MG996R_servo_3** (fixed)

- **origin xyz**: (0.92823, -0.88297, -0.575629) m
- **origin rpy**: (-0.545389, -1.570792, 2.922096) rad

### Local Transform

$$
T^{10}_{13} = \begin{bmatrix}
-0.000004 & -0.692455 & 0.721461 & 0.92823 \\
0.000001 & -0.721461 & -0.692455 & -0.88297 \\
1 & -0.000002 & 0.000003 & -0.575629 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Revolute_7

$L_{11}$ **MAGI_Assembly_URDF_MG996R_servo_5** -> $L_{14}$ **MAGI_Assembly_URDF_HQpod_Femur** (revolute)
  Variable: $q_{4}$

- **origin xyz**: (-0.061224, -0.389313, -0.445687) m
- **origin rpy**: (1.570796, 1.570777, -3.141593) rad
- **axis**: (0, 0, 1)
- **limits**: [-1.396263, 0.959931] rad ([-80deg, 55deg])

### Local Transform

$T^{11}_{14}(q_{4}) = T_{fixed} \cdot R_{axis}(q_{4})$ where:

$$
T_{fixed} = \begin{bmatrix}
-0.000019 & -1 & 0 & -0.061224 \\
0 & 0 & 1 & -0.389313 \\
-1 & 0.000019 & 0 & -0.445687 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

$$
R_{axis}(q_{4}) = \begin{bmatrix}
c_{4} & -s_{4} & 0 & 0 \\
s_{4} & c_{4} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Revolute_14

$L_{12}$ **MAGI_Assembly_URDF_MG996R_servo_8** -> $L_{15}$ **MAGI_Assembly_URDF_HQpod_Femur_2** (revolute)
  Variable: $q_{5}$

- **origin xyz**: (0.072694, -0.389411, 0.810137) m
- **origin rpy**: (-1.570796, -1.570777, 0) rad
- **axis**: (0, 0, 1)
- **limits**: [-1.396263, 0.959931] rad ([-80deg, 55deg])

### Local Transform

$T^{12}_{15}(q_{5}) = T_{fixed} \cdot R_{axis}(q_{5})$ where:

$$
T_{fixed} = \begin{bmatrix}
0.000019 & 1 & 0 & 0.072694 \\
0 & 0 & 1 & -0.389411 \\
1 & -0.000019 & 0 & 0.810137 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

$$
R_{axis}(q_{5}) = \begin{bmatrix}
c_{5} & -s_{5} & 0 & 0 \\
s_{5} & c_{5} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Revolute_26

$L_{13}$ **MAGI_Assembly_URDF_MG996R_servo_3** -> $L_{16}$ **MAGI_Assembly_URDF_HQpod_Femur_3** (revolute)
  Variable: $q_{6}$

- **origin xyz**: (-0.590615, -0.389993, -0.124604) m
- **origin rpy**: (1.570796, -1.570791, 3.141593) rad
- **axis**: (0, 0, 1)
- **limits**: [-0.959931, 1.396263] rad ([-55deg, 80deg])

### Local Transform

$T^{13}_{16}(q_{6}) = T_{fixed} \cdot R_{axis}(q_{6})$ where:

$$
T_{fixed} = \begin{bmatrix}
-0.000005 & 1 & 0 & -0.590615 \\
0 & 0 & 1 & -0.389993 \\
1 & 0.000005 & 0 & -0.124604 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

$$
R_{axis}(q_{6}) = \begin{bmatrix}
c_{6} & -s_{6} & 0 & 0 \\
s_{6} & c_{6} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Revolute_8

$L_{14}$ **MAGI_Assembly_URDF_HQpod_Femur** -> $L_{17}$ **MAGI_Assembly_URDF_MG996R_servo_6** (revolute)
  Variable: $q_{7}$

- **origin xyz**: (-0.456212, 0.048197, 1.279788) m
- **origin rpy**: (0, 0, 0) rad
- **axis**: (0, 0, 1)
- **limits**: [-1.570796, 1.570796] rad ([-90deg, 90deg])

### Local Transform

$$
T^{14}_{17}(q_{7}) = \begin{bmatrix}
c_{7} & -s_{7} & 0 & -0.456212 \\
s_{7} & c_{7} & 0 & 0.048197 \\
0 & 0 & 1 & 1.279788 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Revolute_15

$L_{15}$ **MAGI_Assembly_URDF_HQpod_Femur_2** -> $L_{18}$ **MAGI_Assembly_URDF_MG996R_servo_9** (revolute)
  Variable: $q_{8}$

- **origin xyz**: (-0.509995, -0.349198, 1.524726) m
- **origin rpy**: (0, 0, 0) rad
- **axis**: (0, 0, 1)
- **limits**: [-1.570796, 1.570796] rad ([-90deg, 90deg])

### Local Transform

$$
T^{15}_{18}(q_{8}) = \begin{bmatrix}
c_{8} & -s_{8} & 0 & -0.509995 \\
s_{8} & c_{8} & 0 & -0.349198 \\
0 & 0 & 1 & 1.524726 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Revolute_27

$L_{16}$ **MAGI_Assembly_URDF_HQpod_Femur_3** -> $L_{19}$ **MAGI_Assembly_URDF_MG996R_servo_2** (revolute)
  Variable: $q_{9}$

- **origin xyz**: (0.016368, 0.651577, 1.524259) m
- **origin rpy**: (0, 0, 0) rad
- **axis**: (0, 0, 1)
- **limits**: [-1.570796, 1.570796] rad ([-90deg, 90deg])

### Local Transform

$$
T^{16}_{19}(q_{9}) = \begin{bmatrix}
c_{9} & -s_{9} & 0 & 0.016368 \\
s_{9} & c_{9} & 0 & 0.651577 \\
0 & 0 & 1 & 1.524259 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Rigid_9

$L_{17}$ **MAGI_Assembly_URDF_MG996R_servo_6** -> $L_{20}$ **MAGI_Assembly_URDF_HQpod_Tibia_Left** (fixed)

- **origin xyz**: (0.053166, -0.665761, -0.837464) m
- **origin rpy**: (3.141593, 0, 1.047179) rad

### Local Transform

$$
T^{17}_{20} = \begin{bmatrix}
0.500016 & 0.866016 & 0 & 0.053166 \\
0.866016 & -0.500016 & 0 & -0.665761 \\
0 & 0 & -1 & -0.837464 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Rigid_16

$L_{18}$ **MAGI_Assembly_URDF_MG996R_servo_9** -> $L_{21}$ **MAGI_Assembly_URDF_HQpod_Tibia_Left_2** (fixed)

- **origin xyz**: (-0.342786, 0.832867, -1.082304) m
- **origin rpy**: (-3.141593, 0, -2.094414) rad

### Local Transform

$$
T^{18}_{21} = \begin{bmatrix}
-0.500016 & -0.866016 & 0 & -0.342786 \\
-0.866016 & 0.500016 & 0 & 0.832867 \\
0 & 0 & -1 & -1.082304 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Rigid_30

$L_{19}$ **MAGI_Assembly_URDF_MG996R_servo_2** -> $L_{22}$ **HQpod_Tibia_Right** (fixed)

- **origin xyz**: (-0.273455, 0.731255, -0.968443) m
- **origin rpy**: (-3.141589, -0.000003, 2.0944) rad

### Local Transform

$$
T^{19}_{22} = \begin{bmatrix}
-0.500005 & 0.866023 & -0.000004 & -0.273455 \\
0.866023 & 0.500005 & 0.000001 & 0.731255 \\
0.000003 & -0.000003 & -1 & -0.968443 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Global Transform Chains

Transform from root $L_0$ to any link, as product of local transforms along the kinematic chain.

$$T^{0}_{2} = T^{0}_{1} \cdot T^{1}_{2}\quad (L_0 \to L_{2}: \text{HexapodV3Top})$$

$$T^{0}_{3} = T^{0}_{1} \cdot T^{1}_{2} \cdot T^{2}_{3}\quad (L_0 \to L_{3}: \text{MAGI_Assembly_URDF_MG996R_servo})$$

$$T^{0}_{4} = T^{0}_{1} \cdot T^{1}_{2} \cdot T^{2}_{4}\quad (L_0 \to L_{4}: \text{MAGI_Assembly_URDF_MG996R_servo_7})$$

$$T^{0}_{5} = T^{0}_{1} \cdot T^{1}_{2} \cdot T^{2}_{5}\quad (L_0 \to L_{5}: \text{MAGI_Assembly_URDF_HQpod_Coxal_Right_v2_2})$$

$$T^{0}_{6} = T^{0}_{1} \cdot T^{1}_{2} \cdot T^{2}_{6}\quad (L_0 \to L_{6}: \text{MAGI_Assembly_URDF_MG996R_servo_4})$$

$$T^{0}_{7} = T^{0}_{1} \cdot T^{1}_{2} \cdot T^{2}_{3} \cdot T^{3}_{7}(q_{1})\quad (L_0 \to L_{7}: \text{MAGI_Assembly_URDF_HQpod_Coxal_Left_v2})$$

$$T^{0}_{8} = T^{0}_{1} \cdot T^{1}_{2} \cdot T^{2}_{4} \cdot T^{4}_{8}\quad (L_0 \to L_{8}: \text{MAGI_Assembly_URDF_HQpod_Coxal_Right_v2})$$

$$T^{0}_{9} = T^{0}_{1} \cdot T^{1}_{2} \cdot T^{2}_{4} \cdot T^{4}_{9}(q_{2})\quad (L_0 \to L_{9}: \text{MAGI_Assembly_URDF_HQpod_Coxal_Left_v2_2})$$

$$T^{0}_{10} = T^{0}_{1} \cdot T^{1}_{2} \cdot T^{2}_{6} \cdot T^{6}_{10}(q_{3})\quad (L_0 \to L_{10}: \text{MAGI_Assembly_URDF_HQpod_Coxal_Right_v2_3})$$

$$T^{0}_{11} = T^{0}_{1} \cdot T^{1}_{2} \cdot T^{2}_{3} \cdot T^{3}_{7}(q_{1}) \cdot T^{7}_{11}\quad (L_0 \to L_{11}: \text{MAGI_Assembly_URDF_MG996R_servo_5})$$

$$T^{0}_{12} = T^{0}_{1} \cdot T^{1}_{2} \cdot T^{2}_{4} \cdot T^{4}_{9}(q_{2}) \cdot T^{9}_{12}\quad (L_0 \to L_{12}: \text{MAGI_Assembly_URDF_MG996R_servo_8})$$

$$T^{0}_{13} = T^{0}_{1} \cdot T^{1}_{2} \cdot T^{2}_{6} \cdot T^{6}_{10}(q_{3}) \cdot T^{10}_{13}\quad (L_0 \to L_{13}: \text{MAGI_Assembly_URDF_MG996R_servo_3})$$

$$T^{0}_{14} = T^{0}_{1} \cdot T^{1}_{2} \cdot T^{2}_{3} \cdot T^{3}_{7}(q_{1}) \cdot T^{7}_{11} \cdot T^{11}_{14}(q_{4})\quad (L_0 \to L_{14}: \text{MAGI_Assembly_URDF_HQpod_Femur})$$

$$T^{0}_{15} = T^{0}_{1} \cdot T^{1}_{2} \cdot T^{2}_{4} \cdot T^{4}_{9}(q_{2}) \cdot T^{9}_{12} \cdot T^{12}_{15}(q_{5})\quad (L_0 \to L_{15}: \text{MAGI_Assembly_URDF_HQpod_Femur_2})$$

$$T^{0}_{16} = T^{0}_{1} \cdot T^{1}_{2} \cdot T^{2}_{6} \cdot T^{6}_{10}(q_{3}) \cdot T^{10}_{13} \cdot T^{13}_{16}(q_{6})\quad (L_0 \to L_{16}: \text{MAGI_Assembly_URDF_HQpod_Femur_3})$$

$$T^{0}_{17} = T^{0}_{1} \cdot T^{1}_{2} \cdot T^{2}_{3} \cdot T^{3}_{7}(q_{1}) \cdot T^{7}_{11} \cdot T^{11}_{14}(q_{4}) \cdot T^{14}_{17}(q_{7})\quad (L_0 \to L_{17}: \text{MAGI_Assembly_URDF_MG996R_servo_6})$$

$$T^{0}_{18} = T^{0}_{1} \cdot T^{1}_{2} \cdot T^{2}_{4} \cdot T^{4}_{9}(q_{2}) \cdot T^{9}_{12} \cdot T^{12}_{15}(q_{5}) \cdot T^{15}_{18}(q_{8})\quad (L_0 \to L_{18}: \text{MAGI_Assembly_URDF_MG996R_servo_9})$$

$$T^{0}_{19} = T^{0}_{1} \cdot T^{1}_{2} \cdot T^{2}_{6} \cdot T^{6}_{10}(q_{3}) \cdot T^{10}_{13} \cdot T^{13}_{16}(q_{6}) \cdot T^{16}_{19}(q_{9})\quad (L_0 \to L_{19}: \text{MAGI_Assembly_URDF_MG996R_servo_2})$$

$$T^{0}_{20} = T^{0}_{1} \cdot T^{1}_{2} \cdot T^{2}_{3} \cdot T^{3}_{7}(q_{1}) \cdot T^{7}_{11} \cdot T^{11}_{14}(q_{4}) \cdot T^{14}_{17}(q_{7}) \cdot T^{17}_{20}\quad (L_0 \to L_{20}: \text{MAGI_Assembly_URDF_HQpod_Tibia_Left})$$

$$T^{0}_{21} = T^{0}_{1} \cdot T^{1}_{2} \cdot T^{2}_{4} \cdot T^{4}_{9}(q_{2}) \cdot T^{9}_{12} \cdot T^{12}_{15}(q_{5}) \cdot T^{15}_{18}(q_{8}) \cdot T^{18}_{21}\quad (L_0 \to L_{21}: \text{MAGI_Assembly_URDF_HQpod_Tibia_Left_2})$$

$$T^{0}_{22} = T^{0}_{1} \cdot T^{1}_{2} \cdot T^{2}_{6} \cdot T^{6}_{10}(q_{3}) \cdot T^{10}_{13} \cdot T^{13}_{16}(q_{6}) \cdot T^{16}_{19}(q_{9}) \cdot T^{19}_{22}\quad (L_0 \to L_{22}: \text{HQpod_Tibia_Right})$$

