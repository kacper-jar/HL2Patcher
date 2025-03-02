# HL2Patcher <img src="assets/icon.png" alt="HL2Patcher Logo" width="50" align="right">

**HL2Patcher** makes *Half-Life 2* playable on modern ARM Macs that only support 64-bit applications. Its goal is to simplify the patching process into an easy-to-use app, so anyone can enjoy the game again without hassle.  

## 🛠 How It Works  

With Apple dropping support for 32-bit applications, *Half-Life 2* and its version of the Source Engine no longer function on macOS. HL2Patcher resolves this by retrieving a modified version of the Source Engine code and compiling it for ARM-based 64-bit architecture, so the game can run again.  

## 🔧 Requirements  

- macOS **Big Sur (11.0)** or later
- A copy of *Half-Life 2* installed via Steam

## 📥 Installation  

1. Download the latest release from [GitHub Releases](https://github.com/KZL00/HL2Patcher/releases).  
2. Extract the app and move it to the Applications folder.  
3. Launch HL2Patcher and follow the on-screen instructions.

## 🗂 Why Does HL2Patcher Need Access to the Documents Folder?  

macOS asks for permission to access your Documents folder because of the file picker functionality in HL2Patcher. This is a standard permission request when the app needs to interact with files on your system.  

It is **recommended** that you allow this permission for HL2Patcher to function as intended, but everything should work fine as long as you don't select the "Documents" folder during the file selection process. 

## 🏗 How to Build  

To build HL2Patcher from source, you'll need **Python 3.12 or newer**.  

1. Clone the repository
2. Assign execution permissions to the build script:
   ```sh
    chmod +x build-macos.sh
    ```
3. Run the build script:
   ```sh
    ./build-macos.sh
    ```

## 🤝 How to Contribute  

Contributions are welcome! If you'd like to contribute:  

1. Fork the repository  
2. Create a new branch for your feature or fix  
3. Commit your changes and push them to your fork  
4. Open a pull request with a clear description of your changes  

## ⚠ Disclaimer  

HL2Patcher is an independent project and is **not affiliated with Valve Corporation**. It uses modified Source Engine code to restore functionality on macOS, but you must own a legal copy of *Half-Life 2* to use it.  

## ⚠ Liability Warning  

By using HL2Patcher, you acknowledge that you do so **at your own risk**. While the app is designed to help, the developer **cannot be held responsible** for any issues, including data loss, system instability, or other unintended consequences.  

## 📜 License  

HL2Patcher is licensed under the **MIT License**. See the `LICENSE` file for details.