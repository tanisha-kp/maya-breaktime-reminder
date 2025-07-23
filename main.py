import maya.cmds as cmds
import threading
import time

# Globals
current_energy = 100
timer_active = False

def energy_drainer():
    global current_energy, timer_active

    while timer_active and current_energy > 10:
        time.sleep(5)  #5 seconds

        current_energy -= 30
        if current_energy < 0:
            current_energy = 0

        try:
            cmds.progressBar("energyBar", edit=True, progress=current_energy)
            cmds.text("energyText", edit=True, label=f"Energy: {current_energy}%")
        except:
            # UI closed — exit loop
            timer_active = False
            break

    if current_energy <= 10:
        cmds.confirmDialog(title="Break Time!", message="You deserve a break cutiee! Go get yourself a snack 🍵", button=["OK"])
        timer_active = False

def start_energy_timer(*args):
    global timer_active, current_energy

    if timer_active:
        cmds.warning("Timer is already running!")
        return

    timer_active = True
    current_energy = 100

    cmds.progressBar("energyBar", edit=True, progress=current_energy)
    cmds.text("energyText", edit=True, label=f"Energy: {current_energy}%")

    # Run the energy drain in a background thread
    thread = threading.Thread(target=energy_drainer)
    thread.start()

def show_energy_ui():
    if cmds.window("energyUI", exists=True):
        cmds.deleteUI("energyUI")

    cmds.window("energyUI", title="Maya Energy Bar", resizeToFitChildren=True)

    cmds.columnLayout(adjustableColumn=True, rowSpacing=5)
    cmds.text("energyText", label="Energy: 100%", align='center')
    cmds.progressBar("energyBar", maxValue=100, width=220, height=20, progress=100)
    cmds.button(label="Let's Go! 🚀", command=start_energy_timer)

    cmds.showWindow("energyUI")

# Run the UI
show_energy_ui()
