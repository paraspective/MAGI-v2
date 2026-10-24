# 🏛️ MAGI Archive — Historical Evolution & Research Iterations

This directory preserves the historical engineering journey, early prototypes, deprecated mechanical iterations, and comparative reference baselines that led to the production MAGI architecture.

---

## 🗂️ Classification of Past Work

```
archive/
├── cad_prototypes/              Early mechanical brackets and 3D print iterations
│   ├── HQpod_Coxal_Servo_Plate... Earlier servo mount designs (tested for flex & clearance)
│   ├── MG996R_servo.f3d / .step   CAD reference models for servo integration
│   └── README.md                 Detailed post-mortem on early mechanical iterations
│
├── urdf_iterations/             Kinematic description evolution
│   ├── URDF_initial/             First SolidWorks/Fusion URDF export (URDF_old)
│   ├── URDF_v1/                  Interim joint & link description (URDF)
│   └── README.md                 Evolution towards production MAGI_Assembly_URDF
│
├── legacy_scripts/              Monolithic prototype scripts
│   ├── MAGI_gait_learning.py     Initial standalone PyBullet training script
│   ├── ik.py / fk.py             Initial kinematics solvers before modularization
│   ├── camera_server.py          Early OpenCV streaming script
│   └── README.md                 Migration notes to modern modular architecture
│
└── references/                  Comparative open-source benchmarks & studies
    ├── Regis/                    Kenneth Mikolaichik's 14-servo quadruped
    ├── SpdrBot/                  Isaac Sim quadruped direct project
    ├── Walking 3U CubeSat/       Biomimetic walking satellite mechanism
    ├── Quadruped Hexapod MG996R/ 3D printed servo linkage baseline
    ├── hexapod_spiderbot/        Hexapod leg geometry reference
    └── REFERENCES.md             Formal attribution, citations, and comparative analysis
```

---

## 🔬 Key Engineering Insights from Past Iterations

1. **Servo Plate Flexing (CAD Iterations)**:
   Early iterations used a single 3.8mm pivot pole on the coxal servo plate. Under the dynamic torque of TowerPro MG996R servos (~11 kg·cm), the plate exhibited angular deflection, causing leg splay. The production chassis moved to reinforced dual-shear brackets integrated into the master `MAGI.3mf` assembly.

2. **URDF Standardization (URDF Iterations)**:
   Early exports suffered from misaligned joint rotation frames (Z-axis rotation mismatches between Fusion 360 and ROS coordinate conventions). `URDF_v1` resolved frame origins, and the production `hardware/urdf/MAGI_Assembly_URDF_description` delivers a fully validated ROS 2 Ament package with matching visual/collision meshes.

3. **Monolithic to Modular (Legacy Scripts)**:
   Initial Python scripts executed inference, locomotion, and kinematics in a single blocking thread. This resulted in jitter during AI inference bursts. The project subsequently evolved into **MAGI OS**, which leverages 4 isolated CPU cores via ZeroMQ and POSIX shared memory.
