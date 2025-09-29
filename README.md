**ADULT CONTENT BLOCKER (ACB)**

**ACB** is a simple background script written in Python that monitors your keyboard input in real-time. If any word you type matches a predefined list of adult or inappropriate terms, your system will automatically shut down as a disciplinary action.

This tool is intended for personal use to help curb unhealthy online habits. Use it at your own risk. **The creator is not responsible for any unintended behavior or system issues caused by using this script.**

**⚙️ How It Works**

ACB uses a keylogger to capture typed input.

It continuously compares typed content against a list of banned words.

If a banned word is detected, the script initiates an automatic shutdown.

If no banned words are found, your system continues functioning normally.

**📦 Installation**

Download the repository.

Locate the keylogger_shutdown.pyw file and copy it.

Ensure Python is installed on your system and that pythonw.exe is available.

Press Win + R, type shell:startup, and hit Enter.

Inside the Startup folder:

Create a new shortcut.

Point it to the keylogger_shutdown.pyw file.

Open Task Manager → Startup tab and make sure the script appears and is enabled.

Restart your machine and voila

Upon system startup, ACB will run silently in the background and begin monitoring.

**🚫 Banned Words**

The script currently checks for 10–15 commonly used adult/inappropriate terms. You can customize this list by editing the banned_words set in the script.

Want to contribute banned word suggestions? Feel free to fork the repo or send a pull request.

**⚠️ Disclaimer**

This tool is experimental and intended for personal use only.

It is currently supported on Windows desktops only.

**Use with caution. Unexpected shutdowns can cause data loss.

The author is not liable for any damage, loss, or misuse.**

**Stay focused. Stay clean. 🛡️**

**⚠️ Disclaimer 02**

This Tool is a bit buggy, It sometimes shutdowns your PC randomly when even non banned words are typed(SORRY FOR THAT, FIX IT IF POSSIBLE THANKS)
