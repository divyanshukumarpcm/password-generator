# Password Generator
 Generates Strong ( Random | Logical ) Password.

### Supports Platform: Cross Platform

### Programming Language: Python 3 and above

### How to use:
 1. If you have *Python3* installed. You can use the `.py` file. Make sure to install `pyperclip` package - `python -m pip install pyperclip`.
  - For *Windows*, use [generate_password_no_color.py][1] file.
  - For *Linux/macOS*, you can use any `.py` file. But if you are using colored version i.e., [generate_password.py][2] make sure you install, *termcolor* package (`python -m pip install termcolor`) in Python.
  - For *Linux*, you need to install `xclip` using command - `sudo apt install xclip`

2. You can use **binaries/executable** version as well.
 - Binaries are in [executables][6] folder.
    - For ***Windows*** -> [Download][3]
    - For ***macOS*** -> [Download][5]
  - After downloading, paste the file in `Documents` folder and open **Terminal/Command Prompt**.
  - Enter the command, `cd Documents`.
  - Run the file by typing `./` followed by file name. For eg., `./generate_password.exe` (for Windows) and `./generate_password` (for macOS).   

**Note:** On *macOS*, before running the file, you might need to run `chmod 755 generate_password` to make it *executable*.

### Available Arguments:
 - Program is divided into two parts:
   - **strong:** *Generates strong random password.* **Usage:** `generate_password strong -h`
      - **-l or --length:** *Optional. This option can be used to specify the length of the password.
        If this option is not used default length will be 12.*
   - **logical:** *Generates password on basis of questions you answered.* **Usage:** `generate_password logical -h`
      - **-q or --ques-number:** *Optional. This option can be used to specify number of questions you want to answer.
        Maximum is 4. If this options is not used default is random between 2 or 3.*
- **-h or --help:** *Displays all the available options.*    
- **-c or --copy:** *Optional. Specifying this option will copy the generated password to clipboard.*

### Color Significance:
 - **Green:** Successful.
 - **Blue:** In process.
 - **Red:** Unsuccessful or Errors.
 - **Yellow:** User Input.

### Licensed: GNU General Public License, version 3

### Developer Information:
- **Website:** https://www.hackhunt.in/
- **Contact:** info@hackhunt.in
- **LinkedIn:** https://www.linkedin.com/company/hackhunt
- **Youtube:** [@hackhunt](https://youtube.com/hackhunt)
- **Instagram:** [@hh.hackhunt](https://www.instagram.com/hh.hackhunt/)
- **Facebook:** [@hh.hackhunt](https://www.facebook.com/hh.hackhunt/)
- **Twitter:** [hh_hackhunt](https://twitter.com/hh_hackhunt/)
- **Patreon:** [@hackhunt](https://www.patreon.com/hackhunt)

[1]: ./generate_password_no_color.py
[2]: ./generate_password.py
[3]: ./executables/windows/
[5]: ./executables/mac/
[6]: ./executables/
