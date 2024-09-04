### YouTube-as-Command-Control-Server

Imagine being able to control your device with just a few simple commands, without having to lift a finger or type
out complex instructions. Sounds like science fiction, right? Well, what if we told you that this is now possible,
and it's all thanks to the power of YouTube?

This innovative project has harnessed the potential of YouTube live comments as a command control server, allowing
users to assign specific actions to certain keywords or phrases in real-time. That's right - using nothing more
than your average YouTube video comment section, you can now control your device with unprecedented ease and
precision.

## Summary
This project allows you to control your computer or device using YouTube live comments. With this project, you can assign specific commands to certain keywords or phrases in YouTube live chat and perform corresponding actions on your device.

### Installing Guide

To get started with this project, follow these steps:

#### Step 2: Clone the Repository

1. Run the following command to clone the project from GitHub: `git clone
https://github.com/codeterrayt/Youtube-as-Command-Control-Server.git`.

#### Step 2: Create a Virtual Environment (venv)

1. Open your terminal or command prompt.
2. Run the following command to create a new virtual environment: `python -m venv myenv` (replace "myenv" with the
name you want).
3. Activate the virtual environment by running: `source myenv/bin/activate` (on Linux or macOS) or
`myenv\Scripts\activate` (on Windows).


#### Step 3: Install Required Packages

1. Run the following command to install the necessary packages using pip: `pip install -r requirements.txt`.

### Running the Program

To run the program, follow these steps:

1. Activate the virtual environment (if you haven't already).
2. Run the following command: `python GUI.py`
3. Enter the Live Youtube Stream Link
4. Done!
5. Now Just Navigate to The Live Stream and Start Commenting

### Demo Video



https://github.com/user-attachments/assets/a1898a85-04ce-4360-8114-63855c6bfe2d


This video demonstrates the functionality of the program and shows how it can be used to control your device using
YouTube live comments.

### How it Works

The program uses the `pytchat` library to connect to YouTube live and read comments. It then processes each
comment, checking if it contains any assigned commands. If it does, the program performs the corresponding action
using the `pynput` library.

Commands can be anything from pressing Enter or Caps Lock to typing specific text. The program will only respond
to commands that are specifically assigned in the `key_map` dictionary.


**Commands Documentation**
==========================

The `key_map` dictionary defines a set of pre-configured key mappings that can be used to control your device
using YouTube live comments. Each key mapping is associated with a specific action or command.

### Available Commands

Here is a list of available commands and their corresponding actions:

* **Navigation**:
  - up: Press Arrow Up Button
  - down: Press Arrow Down Button
  - left: Press Arrow Left Button
  - right: Press Arrow Right Button
    
* **Editing**:
  - enter: Press Enter key
  - space: Press Space bar
  - backspace: Delete character to the left of the cursor
  - delete: Delete character at the cursor position
  - esc: Press Esc key ( Escape )
* **Modifiers**:
  - shift: Press Shift key
  - ctrl: Press Ctrl key
  - alt: Press Alt key
  - win: Press Windows key (Cmd on Mac)
* **Function Keys**:
  - f1-f12: Press corresponding function key
* **Media Controls**:
  - media_play_pause: Play/Pause media
  - media_volume_mute: Mute/Unmute volume
  - media_volume_down: Decrease volume
  - media_volume_up: Increase volume
  - media_next: Skip to next track/song
  - media_previous: Go back to previous track/song
* **Miscellaneous**:
  - tab: Move cursor to the beginning of the next field
  - home: Move cursor to the beginning of the line
  - end: Move cursor to the end of the line
  - pageup: Scroll up
  - pagedown: Scroll down

And More!! 

```bash
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
```

### Customizing Key Mappings

The `key_map` dictionary is customizable, allowing you to define your own key mappings and actions. To customize
the key map, simply add or modify entries in the dictionary.

For example, if you want to assign a specific action to the "shift" key, you can modify the existing entry:

* `"shift": Key.shift,`

to something like this:

* `"shift": Key.media_volume_down,`

This would cause the "Shift" key to decrease the volume when pressed.

### Contributing

If you'd like to contribute to this project, please see the [contributing guide](CONTRIBUTING.md) for more
information on how to get involved.

### Licensing

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
