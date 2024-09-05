from pynput import keyboard

keys = []
def on_press(keys) :
    print(f"You pressed {keys}")

def on_release(keys) :
    print(" ")
    if keys == keyboard.Key.esc :
        # Stop listener
        return False

with keyboard.Listener(on_press=on_press,
                       on_release=on_release) as Listener :
                       Listener.join()