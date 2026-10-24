# 🌿 MAGI Perception & Multispectral Vision Subsystem

Edge AI perception, camera streaming, and end-to-end MLOps plant pathology detection pipeline for the MAGI Quadruped Robot.

---

## 📋 Overview

The perception subsystem provides the visual and spectral intelligence for MAGI, serving as the sensory input for the **Melchior (MAGI-1)** node. Unlike conventional spot-checking or leaf-level models, MAGI conducts **continuous canopy scanning** as it traverses agricultural rows, generating real-time GPS-referenced disease heatmaps.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        MAGI PERCEPTION PIPELINE                        │
│                                                                        │
│   PiCamera V2.1  ──► Camera Server (POSIX Shared Memory Zero-Copy)    │
│                                │                                       │
│                                ▼                                       │
│                  Pre-Filtering & Tiling Engine                         │
│             (4x3 grid decomposition + Excess Green Soil Mask)          │
│                                │                                       │
│                                ▼                                       │
│                6-Channel Spectral Feature Extraction                   │
│                    [R, G, B, ExG, GRVI, L* (LAB)]                      │
│                                │                                       │
│                                ▼                                       │
│                Melchior TFLite Classifier (XNNPACK)                    │
│            ~125ms per frame on Raspberry Pi 4B CPU                     │
│                                │                                       │
│                                ▼                                       │
│             Temporal EMA Smoothing + Spatial Field Grid                │
│                                │                                       │
│                                ▼                                       │
│               Caspar Decision Engine (TRACK / ALERT)                   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🗂️ Directory Organization

```
perception/
├── camera/                           Hardware Capture & Streaming Layer
│   ├── camera_server.py              Low-latency PiCamera streaming via ZeroMQ / Shared Memory
│   └── __init__.py
├── mlops/                            End-to-End MLOps Pipeline (MAGI Vision)
│   ├── magi_vision/                  Core modular Python package
│   │   ├── components/               Pipeline stages (Data Ingestion, Validation, Transform,
│   │   │                             Model Trainer, Model Evaluation, Model Pusher)
│   │   ├── configuration/            Pipeline parameters & runtime settings
│   │   ├── constants/                Static configurations & thresholds
│   │   ├── entity/                   Data contracts (config & artifact entities)
│   │   ├── pipeline/                 Training & prediction pipeline orchestrators
│   │   └── utils/                    Main helper functions
│   ├── config/                       Model architecture and schema YAMLs
│   ├── templates/                    Web inspection templates
│   ├── FLOW/ & flowchart/            Architectural visual diagrams
│   ├── app.py                        FastAPI inference & training trigger server
│   ├── Dockerfile                    Containerized training environment
│   └── requirements.txt              MLOps dependencies
└── analysis/                         Research & Preprocessing Notebooks
    ├── Heatmap_algo.ipynb            Baseline spectral heatmap algorithm
    ├── MAGI_Colab_Training.ipynb     Colab accelerated training notebook
    └── visauls.py                    Streamlit CLAHE & evaluation dashboard
```

---

## 🚀 Quick Start

### 1. Run Camera Capture Server
```bash
python perception/camera/camera_server.py
```

### 2. Launch FastAPI Inference & Training Dashboard
```bash
cd perception/mlops
pip install -r requirements.txt
python app.py
# Open http://localhost:8080 to access the Canopy Health Web UI
```

### 3. Launch Streamlit Spectral Visualizer
```bash
streamlit run perception/analysis/visauls.py
```
