from pynput import keyboard
import os

# Full words to trigger shutdown
banned_words = {
    "porn", "sex", "tits", "boobs", "ass", "ntr", "milf", "hentai",
    "fap haven", "aunt hina", "princess peach", "force", "comic", "damp lips", "spankbang", "plainprxy", "plainproxy", "Jill valentine", "3D porn", "Porn Comic", "Brutality", "chuhai", "Hung", "Yamato", "Valentine", "Jill", "Zombie porn", "Cartoonporn", "Pln prxy" , "proxy", "prxy", "big boobs", "huge ass", "skylar vox", "alexa croft", "porn comics", "xxx", "9xbddy" , "9xbuddy", "nsfw"
}

typed_buffer = ""

def check_banned(buffer):
    buffer = buffer.lower()
    words = buffer.replace("\n", " ").split()
    for word in words:
        if word in banned_words:
            return word
    return None

def shutdown(trigger):
    print(f"[⚠️] Banned word detected: {trigger}")
    os.system("shutdown /s /f /t 5")  # Shutdown in 5 seconds

def on_press(key):
    global typed_buffer
    try:
        if hasattr(key, 'char') and key.char is not None:
            typed_buffer += key.char
            typed_buffer = typed_buffer[-100:]  # Limit size

            match = check_banned(typed_buffer)
            if match:
                shutdown(match)
    except:
        pass

    if key == keyboard.Key.space:
        typed_buffer += ' '
    elif key == keyboard.Key.enter:
        typed_buffer += '\n'
    elif key == keyboard.Key.backspace:
        typed_buffer = typed_buffer[:-1]

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
