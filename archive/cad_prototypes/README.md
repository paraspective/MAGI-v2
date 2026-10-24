# 🛠️ Legacy CAD Prototypes & Bracket Iterations

This directory preserves early mechanical design iterations for the 12-DOF quadruped's joint brackets and servo plates.

---

## 📋 Iteration History

| File | Description | Status & Evaluation |
|---|---|---|
| `HQpod_Coxal_Servo_Plate_with_3.8mm_pole.stl` | First revision of the Coxal servo plate with an integrated 3.8mm pivot pin. | **Superseded**: Inadequate shear strength under dynamic leg impacts. |
| `HQpod_Coxal_Servo_Plate_40.7x20mm_with_3.8mm_pole.stl` | Adjusted rectangular servo cutout dimensions (40.7 × 20 mm). | **Superseded**: Improved servo fitment, but single pivot suffered angular flex. |
| `HQpod_Coxal_Servo_Plate_MG996R_fit.stl` | Specialized clearance tolerances specifically measured for TowerPro MG996R cases. | **Integrated**: Tolerance values incorporated into final `MAGI.3mf`. |
| `HQpod_Coxal_Servo_Plate_MG996R_pole_repositioned.stl` | Shifted pivot pole axis to align with the servo output shaft centerline. | **Integrated**: Centerline alignment carried forward into current production legs. |
| `MG996R_servo.f3d` / `.step` | Reference CAD solid bodies of the TowerPro MG996R standard servo motor. | **Reference**: Used for clearance validation in CAD software. |
| `mg996_arm_round.step` | Circular servo horn CAD model for 25T spline interface. | **Reference**: Used to design interlocking horn sockets. |

---

## 💡 Production Progression

All successful lessons from these prototype iterations were integrated into the unified production master model at [`hardware/cad/MAGI.3mf`](../../hardware/cad/MAGI.3mf) and production STLs at [`hardware/stl/`](../../hardware/stl/).
