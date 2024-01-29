# BUILD.md

## Introduction
This document provides instructions for building the `DogDisplayForPython` application from source. Aimed at users interested in setting up and running the application in their environments, it offers a clear guide to the build process. The build process has been tested in the following environments:

- **Windows:** 
  - Microsoft Windows 10 Pro.
  - GitHub Actions environment running Microsoft Windows NT 10.0.

- **Linux:** 
  - Ubuntu 22.04.3 LTS, as utilized in a Docker container.
  - GitHub Actions environment running Ubuntu 22.04.3 LTS.

These instructions primarily target the above environments but may be applicable to similar configurations.

## Index
1. **[Linux Installation Guide](#linux-installation-guide)**
   - [1.1 Setting Up the Environment](#--11-setting-up-the-environment)
   - [1.2 Preparing the Project](#--12-preparing-the-project)
   - [1.3 Setting up Dependencies](#%EF%B8%8F--13-setting-up-dependencies)
   - [1.4 Running Tests (Optional)](#--14-running-tests-optional)
   - [1.5 Running the Application](#--15-running-the-application)

2. **[Windows Installation Guide](#windows-installation-guide)**
   - [2.1 Setting Up the Environment](#--21-setting-up-the-environment)
     - [2.1.1 GUI Method (Option #1)](#211-gui-method-option-1)
     - [2.1.2 PowerShell Method (Option #2)](#212-powershell-method-option-2)
   - [2.2 Preparing the Project](#--22-preparing-the-project)
   - [2.3 Setting up Dependencies](#%EF%B8%8F--23-setting-up-dependencies)
   - [2.4 Running Tests (Optional)](#--24-running-tests-optional)
   - [2.5 Running the Application](#--25-running-the-application)

3. **[Conclusion](#conclusion)**

## Linux Installation Guide
### 🌍-🌍-🌍-🌍-🌍-🌍-🌍-🌍-🌍-🌍-🌍
### 🌍 &nbsp; 1.1 Setting Up the Environment
### 🌍-🌍-🌍-🌍-🌍-🌍-🌍

This section provides instructions for setting up the necessary environment to run the `DogDisplayForPython` application on Linux. The setup process involves installing several key dependencies through the command line.

1. **Update Package Lists:**
   ```bash
   apt-get update
   ```

2. **Install Python 3 and Pip:**
   ```bash
   apt-get install -y python3
   ```
   
   ```bash
   apt-get install -y python3-pip
   ```

3. **Install Git:**
   ```bash
   apt-get install -y git
   ```

### Verify Dependency Installation Success (Optional)

If you wish to verify the installations from the previous step, you can use one or more of the following commands:

<details>
<summary><ins><b>Verify Installation Success:</b></ins> Click here to EXPAND/COLLAPSE section on install verification commands!</summary>


```bash
python3 --version
```

```bash
pip3 --version
```

```bash
git --version
```

</div>
</details>

---
### 📚-📚-📚-📚-📚-📚-📚-📚-📚-📚
### 📚 &nbsp; 1.2 Preparing the Project 
### 📚-📚-📚-📚-📚-📚-📚

Before runn the application, you need to clone the project repository and navigate to its directory:

1. **Clone the Repository:**
   Clone the `DogDisplayForPython` project from GitHub:
   ```bash
   git clone https://www.github.com/mittons/DogDisplayForPython.git
   ```

2. **Navigate to the Project Directory:**
   Change to the newly created project directory:
   ```bash
   cd DogDisplayForPython
   ```

Now that the project is cloned to your local machine, you can proceed to setting up the dependencies, and then run the program.

---
### ⚙️-⚙️-⚙️-⚙️-⚙️-⚙️-⚙️-⚙️-⚙️-⚙️
### ⚙️ &nbsp; 1.3 Setting up Dependencies
### ⚙️-⚙️-⚙️-⚙️-⚙️-⚙️-⚙️

Set up the projects dependencies using pip in a console window:

```bash
pip3 install -r requirements.txt
```

```bash
pip3 install -e .
```

---
### 🧪-🧪-🧪-🧪-🧪-🧪-🧪-🧪-🧪-🧪
### 🧪 &nbsp; 1.4 Running Tests (Optional)
### 🧪-🧪-🧪-🧪-🧪-🧪-🧪

### 1.4.1 Running Unit/Integration Tests (Optional)

After building the application, you can optionally run the unit and integration tests to verify the functionality:

```bash
python3 run_server_tests.py
```

---
### 🚀-🚀-🚀-🚀-🚀-🚀-🚀-🚀-🚀-🚀
### 🚀 &nbsp; 1.5 Running the Application
### 🚀-🚀-🚀-🚀-🚀-🚀-🚀

You can set the environment to production settings, for the app to connect to an already set up data endpoint:
```bash
set FLASK_ENV=production
```


After setting up and configuring the dependencies for`DogDisplayForPython`, you can run it directly:

```bash
python3 main.py
```

The application will start and listen on localhost port 5678.

You can view its contents in a web browser at [http://localhost:5678](http://localhost:5678).


## Windows Installation Guide

### 🌍-🌍-🌍-🌍-🌍-🌍-🌍-🌍-🌍-🌍-🌍
### 🌍 &nbsp; 2.1 Setting Up the Environment
### 🌍-🌍-🌍-🌍-🌍-🌍-🌍

This section provides instructions for setting up the necessary environment to run the `DogDisplayForPython` application on Windows. There are two methods to set up your environment on Windows: through the graphical user interface (GUI) and using PowerShell commands. 

### 2.1.1 GUI Method (Option #1)
For users who prefer using the graphical interface:

1. **Python:**
   - Download Python 3.12.0 from [Python's official website](https://www.python.org/downloads/).
   - During installation, select the option to add Python to PATH.

2. **Git:**
   - Download Git from [Git for Windows](https://gitforwindows.org/).
   - Follow the installation instructions, ensuring Git is added to PATH.

### 2.1.2 PowerShell Method (Option #2)
For users comfortable with PowerShell:

1. **Install Python:**
   ```powershell
   Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.0/python-3.12.0.exe' -OutFile 'PythonInstaller.exe'
   Start-Process 'PythonInstaller.exe' -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1 Include_test=0 TargetDir=C:\Python312' -Wait
   ```
   Verify that Python is installed and has been added to PATH:
   ```powershell
   python --version
   ```
   If verification is unsuccessful, update PATH, then reverify:
   ```powershell
   $pythonPath = "C:\Python312"
   $env:Path += ";$pythonPath"
   $env:Path += ";$pythonPath\Scripts"
   python --version
   ```

2. **Install Git:**
   ```powershell
   Invoke-WebRequest -Uri 'https://github.com/git-for-windows/git/releases/download/v2.43.0.windows.1/Git-2.43.0-64-bit.exe' -OutFile 'GitInstaller.exe'
   Start-Process 'GitInstaller.exe' -ArgumentList '/VERYSILENT' -Wait
   ```
   Verify that Git is installed and has been added to PATH:
   ```powershell
   git --version
   ```
   If verification is unsuccessful, update PATH, then reverify:
   ```powershell
   $gitPath = "C:\Program Files\Git\bin"
   $env:Path += ";$gitPath"
   git --version
   ```

---
### 📚-📚-📚-📚-📚-📚-📚-📚-📚-📚
### 📚 &nbsp; 2.2 Preparing the Project
### 📚-📚-📚-📚-📚-📚-📚

Before building the application, you need to clone the project repository and navigate to its directory:

1. **Clone the Repository:**
   Clone the `DogDisplayForPython` project from GitHub:
   ```powershell
   git clone https://www.github.com/mittons/DogDisplayForPython.git
   ```

2. **Navigate to the Project Directory:**
   Change to the newly created project directory:
   ```powershell
   cd DogDisplayForPython
   ```

Now that the project is cloned to your local machine, you can proceed to build it.


---

### ⚙️-⚙️-⚙️-⚙️-⚙️-⚙️-⚙️-⚙️-⚙️-⚙️
### ⚙️ &nbsp; 2.3 Setting up Dependencies
### ⚙️-⚙️-⚙️-⚙️-⚙️-⚙️-⚙️

Set up the projects dependencies using pip in a console window:

   ```powershell
   pip install -r requirements.txt
   ```
   
   ```powershell
   pip install -e .
   ```

---
### 🧪-🧪-🧪-🧪-🧪-🧪-🧪-🧪-🧪-🧪
### 🧪 &nbsp; 2.4 Running Tests (Optional)
### 🧪-🧪-🧪-🧪-🧪-🧪-🧪

### 2.4.1 Running Unit/Integration Tests (Optional)

After building the application, you can optionally run the unit and integration tests to verify the functionality:

   ```powershell
   python run_server_tests.py
   ```

---
### 🚀-🚀-🚀-🚀-🚀-🚀-🚀-🚀-🚀-🚀
### 🚀 &nbsp; 2.5 Running the Application
### 🚀-🚀-🚀-🚀-🚀-🚀-🚀

You can set the environment to production settings, for the app to connect to an already set up data endpoint:
```powershell
$env:FLASK_ENV = 'production'
```


After setting up and configuring the dependencies for`DogDisplayForPython`, you can run it directly:

   ```powershell
   python main.py
   ```

The application will be running and available on localhost port 5678.

You can view its contents in a web browser at [http://localhost:5678](http://localhost:5678).


## Conclusion 

Congratulations on successfully completing the setup process for the `DogDisplayForPython` application. This guide has supported you through the setup of the environment, configuring dependencies, and the execution of the program for your selected platform.

I trust that the steps provided have been clear and helpful in guiding you to this point. Thank you for engaging with the `DogDisplayForPython` build process, and I hope your experience with the application has been insightful.
