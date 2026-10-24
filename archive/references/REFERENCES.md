# 📚 External References, Baselines & Attributions

During the research and prototyping phases of MAGI, several open-source quadruped and hexapod robotics projects were investigated to understand mechanical linkages, servo kinematics, and simulation dynamics. We gratefully acknowledge these community projects:

---

## 1. Regis Quadruped Robot
* **Author**: Kenneth Mikolaichik ([@kennethmikolaichik](https://github.com/kennethmikolaichik))
* **Repository**: [kennethmikolaichik/Regis](https://github.com/kennethmikolaichik/Regis)
* **License**: Open Source / Creative Commons
* **Role in MAGI Research**:
  - Provided early insights into 4-legged walking robot chassis layout using Raspberry Pi 4B and MG90S/MG996R servos.
  - *MAGI Evolution*: MAGI diverged significantly by developing a custom 3-DOF inverse kinematics solver on an ESP32 co-processor, a custom multi-core ZeroMQ OS, and multispectral plant disease computer vision.
  - *Note*: Large CAD mesh (>100MB) excluded for GitHub compliance; upstream repository contains the full original dataset.

---

## 2. SPDR Bot (Simulated Spider Robot for Isaac Sim)
* **Author**: indystry.cc ([@indystry-cc](https://github.com/indystry-cc))
* **Repository**: [indystry-cc/SPDR-Isaac-Lab](https://github.com/indystry-cc/SPDR-Isaac-Lab) / [indystry.cc](https://indystry.cc)
* **License**: Open for personal and educational use
* **Role in MAGI Research**:
  - Reference implementation for quadruped USD scenes and Isaac Lab reinforcement learning training pipelines.
  - *MAGI Evolution*: MAGI implemented a zero-install Three.js WebGL browser simulator for instant client-side testing without requiring high-end NVIDIA RTX hardware.

---

## 3. Walking 3U CubeSat
* **Platform**: Thingiverse Project #6395490
* **Author**: Open Source Maker Community
* **License**: Creative Commons - Attribution - Non-Commercial
* **Role in MAGI Research**:
  - Explored ultra-compact, modular walking mechanisms for space and resource-constrained robotics applications.

---

## 4. Quadruped Hexapod MG996R
* **Platform**: Thingiverse Project #2726435
* **Author**: Open Source 3D Printing Robotics Community
* **License**: Creative Commons
* **Role in MAGI Research**:
  - Baseline mechanical dimensions for TowerPro MG996R metal-gear servo mounts and horn spacing.

---

## 5. Hexapod Spiderbot Model
* **Repository**: hexapod_spiderbot_model
* **Role in MAGI Research**:
  - Comparative analysis between 6-legged tripod gaits and 4-legged quadruped trot/crawl stability polygons.
