from psychopy.hardware import keyboard

from threedipa.renderer.haploscopeRender import HaplscopeRender2D
from threedipa.renderer.haploscopeConfig import monitor_settings, physical_calibration

def main():
    

    renderer = HaplscopeRender2D(physical_calibration, monitor_settings, 0)
    kb = keyboard.Keyboard()

    while True:
        renderer.draw_fixation_cross()
        renderer.render_screen()

        response_key = kb.waitKeys(keyList=['3', '6', 'escape'], waitRelease=False)

        if response_key[0].name == 'escape':
            break
        
    renderer.close_windows()


if __name__ == "__main__":
    main()