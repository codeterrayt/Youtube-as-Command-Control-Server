import pytchat
from pynput.keyboard import Key, Controller

keyboard = Controller()

# Dictionary mapping comments to specific keys
key_map = {
    "enter": Key.enter,
    "space": Key.space,
    "shift": Key.shift,
    "ctrl": Key.ctrl,
    "alt": Key.alt,
    "tab": Key.tab,
    "backspace": Key.backspace,
    "delete": Key.delete,
    "esc": Key.esc,
    "capslock": Key.caps_lock,
    "win": Key.cmd,  # Windows key (cmd in pynput)
    "home": Key.home,
    "end": Key.end,
    "pageup": Key.page_up,
    "pagedown": Key.page_down,
    "insert": Key.insert,
    "pause": Key.pause,
    "printscreen": Key.print_screen,
    "scrolllock": Key.scroll_lock,
    "numlock": Key.num_lock,
    "f1": Key.f1,
    "f2": Key.f2,
    "f3": Key.f3,
    "f4": Key.f4,
    "f5": Key.f5,
    "f6": Key.f6,
    "f7": Key.f7,
    "f8": Key.f8,
    "f9": Key.f9,
    "f10": Key.f10,
    "f11": Key.f11,
    "f12": Key.f12,
    "up": Key.up,
    "down": Key.down,
    "left": Key.left,
    "right": Key.right,
    "shiftleft": Key.shift_l,
    "shiftright": Key.shift_r,
    "ctrlleft": Key.ctrl_l,
    "ctrlright": Key.ctrl_r,
    "altleft": Key.alt_l,
    "altright": Key.alt_r,
    "menu": Key.menu,
    "media_play_pause": Key.media_play_pause,
    "media_volume_mute": Key.media_volume_mute,
    "media_volume_down": Key.media_volume_down,
    "media_volume_up": Key.media_volume_up,
    "media_next": Key.media_next,
    "media_previous": Key.media_previous,
}

def handle_comment(comment):
    """Process a comment and perform corresponding key actions."""
    commands = comment.lower().split()  # Split comment into commands
    pressed_keys = []

    for command in commands:
        if command in key_map:
            pressed_keys.append(key_map[command])
        else:
            # If it's not a key command, type it as it is
            keyboard.type(command + ' ')  # Adding space to separate words

    # Handle combined key presses
    if pressed_keys:
        for key in pressed_keys:
            keyboard.press(key)
        for key in reversed(pressed_keys):  # Release keys in reverse order
            keyboard.release(key)

def readComments(link):
    chat = pytchat.create(video_id=link)
    while chat.is_alive():
        for c in chat.get().sync_items():
            handle_comment(c.message)

def startCloud(link):
    readComments(link)
