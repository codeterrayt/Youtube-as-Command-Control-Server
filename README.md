### YouTube-as-Command-Control-Server

This project allows you to control your computer or
device using YouTube live comments. With this project, you can assign specific commands to certain keywords or
phrases in YouTube live chat and perform corresponding actions on your device.

### Installing Guide

To get started with this project, follow these steps:

#### Step 1: Create a Virtual Environment (venv)

1. Open your terminal or command prompt.
2. Run the following command to create a new virtual environment: `python -m venv myenv` (replace "myenv" with the
name you want).
3. Activate the virtual environment by running: `source myenv/bin/activate` (on Linux or macOS) or
`myenv\Scripts\activate` (on Windows).


#### Step 2: Clone the Repository

1. Run the following command to clone the project from GitHub: `git clone
https://github.com/codeterrayt/Youtube-as-Command-Control-Server.git`.

#### Step 3: Install Required Packages

1. Run the following command to install the necessary packages using pip: `pip install -r requirements.txt`.

### Running the Program

To run the program, follow these steps:

1. Activate the virtual environment (if you haven't already).
2. Navigate to the project directory.
3. Run the following command: `python GUI.py`
4. Enter the Live Youtube Stream Link

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

### Contributing

If you'd like to contribute to this project, please see the [contributing guide](CONTRIBUTING.md) for more
information on how to get involved.

### Licensing

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
