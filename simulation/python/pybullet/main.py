import os
import sys
import time

# Support standalone execution as well as package imports
current_dir = os.path.dirname(os.path.abspath(__file__))
python_root = os.path.abspath(os.path.join(current_dir, ".."))
kinematics_dir = os.path.join(python_root, "kinematics")
locomotion_dir = os.path.join(python_root, "locomotion")

for p in [current_dir, python_root, kinematics_dir, locomotion_dir]:
    if p not in sys.path:
        sys.path.insert(0, p)

try:
    from kinematics.ik import LegIK3DOF
    from locomotion.gait import Gait
except ImportError:
    from ik import LegIK3DOF
    from gait import Gait

# --- Robot dimensions ---
L_coxa = 6.3
L_femur = 10.15
L_tibia = 19.45

ik = LegIK3DOF(L_coxa, L_femur, L_tibia)
gait = Gait(step_length=10, step_height=5, cycle_time=2.0)

# --- Phase offsets (crawl gait) ---
phases = {
    "LF": 0.0,
    "RB": 0.5,
    "RF": 1.0,
    "LB": 1.5
}

def run_loop(max_steps=None):
    start_time = time.time()
    step = 0
    while max_steps is None or step < max_steps:
        t = time.time() - start_time

        print("\nTime:", round(t, 2))

        for leg, phase in phases.items():
            x, y, z = gait.foot_trajectory(t, phase)

            # shift leg position (important)
            # assume body offset for each leg
            if leg in ["LF", "LB"]:
                y_offset = 5
            else:
                y_offset = -5

            x += 10  # forward offset
            y += y_offset
            z -= 10  # keep leg below body

            t0, t1, t2 = ik.solve(x, y, z)

            print(f"{leg}:",
                  f"{round(t0,2)}",
                  f"{round(t1,2)}",
                  f"{round(t2,2)}")

        step += 1
        time.sleep(0.05)

if __name__ == "__main__":
    run_loop()
