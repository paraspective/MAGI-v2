import os
import time
import pybullet as p
import pybullet_data

# Resolve model path dynamically
current_dir = os.path.dirname(os.path.abspath(__file__))
urdf_path = os.path.join(current_dir, "..", "..", "models", "urdf", "SpiderQ.urdf")
if not os.path.exists(urdf_path):
    urdf_path = "SpiderQ.urdf"

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.loadURDF("plane.urdf")
robot = p.loadURDF(urdf_path, [0, 0, 1])

p.setGravity(0, 0, -9.8)

while True:
    p.stepSimulation()
    time.sleep(1 / 240)
