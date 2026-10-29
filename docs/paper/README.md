# 📄 MAGI Research Paper (IEEE Format)

Source LaTeX files and bibliography for the academic publication documenting the MAGI architecture and empirical edge AI benchmarks.

---

## 📑 Paper Details

* **Title**: *MAGI: A Resource-Constrained 12-DOF Quadruped Architecture with Multi-Core Edge AI and Asynchronous ZeroMQ Middleware for In-Canopy Agricultural Pathology*
* **Authors**: Paras Dharmadhikari, Aki Alphon
* **Target Venues**:
  - IEEE Robotics and Automation Letters (RA-L)
  - IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
  - Computers and Electronics in Agriculture (Elsevier)

---

## 🛠️ How to Compile

### Using `pdflatex` / `latexmk`:
```bash
cd paper/
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

### Using Overleaf:
Upload `main.tex` and `references.bib` directly to [Overleaf](https://www.overleaf.com/) under the IEEE Conference / Transactions template.
