
# Python and PyCharm Installation Guide


## Table of Contents

1. Installing Python on Windows  
2. Installing PyCharm on Windows  
3. Installing Python on Linux  
4. Installing PyCharm on Linux  

---

## 1. Installing Python on Windows

### Step 1: Download Python

1. Visit the official Python website: https://www.python.org/downloads/  
2. Click on the latest version for Windows.  
3. Download the executable installer (e.g., `python-3.x.x.exe`).  

### Step 2: Install Python

1. Run the downloaded installer.  
2. Check the box that says **Add Python to PATH**.  
3. Click on **Customize installation** (optional) or **Install Now**.  
4. Follow the prompts to complete installation.  

### Step 3: Verify Installation

1. Open **Command Prompt**.  
2. Type:  
```

python --version

```
or  
```

py --version

```
You should see the installed Python version displayed.  

---

## 2. Installing PyCharm on Windows

### Step 1: Download PyCharm

1. Visit the JetBrains website: https://www.jetbrains.com/pycharm/download/  
2. Choose between:  
- **Professional** (Paid with full features)  
- **Community** (Free and open-source)  
3. Download the appropriate installer for Windows.  

### Step 2: Install PyCharm

1. Run the downloaded `.exe` installer.  
2. Follow the setup wizard.  
3. You may select options such as:  
- Create Desktop Shortcut  
- Add "Open Folder as Project"  
- Update PATH variable  
4. Click **Install**, then **Finish**.  

### Step 3: First Launch

1. Launch PyCharm.  
2. Choose whether to import previous settings.  
3. Configure theme and keymap (optional).  
4. Start a new project or open an existing one.  

---

## 3. Installing Python on Linux

Most Linux distributions come with Python pre-installed. You can verify and update it as needed.

### Step 1: Check Existing Python Version

Open the terminal and type:  
```

python3 --version

```

### Step 2: Install Python (if needed)

#### On Debian/Ubuntu:

```

sudo apt update
sudo apt install python3 python3-pip

```

#### On Fedora:

```

sudo dnf install python3 python3-pip

```

#### On Arch Linux:

```

sudo pacman -S python python-pip

```

### Step 3: Verify Installation

```

python3 --version
pip3 --version

```

---

## 4. Installing PyCharm on Linux
check system- cat /etc/os-release
### Option 1: Using Snap (Recommended for Ubuntu)

For the Community edition:
```
sudo apt update
sudo apt install snapd

# optional
sudo systemctl enable snapd
sudo systemctl start snapd


sudo snap install pycharm-community --classic

```

For the Professional edition:
```

sudo snap install pycharm-professional --classic

```

### Option 2: Manual Installation

1. Download from: https://www.jetbrains.com/pycharm/download/  
2. Choose the appropriate edition and download the `.tar.gz` file.  
3. Extract the archive:  
```

tar -xzf pycharm-\*.tar.gz

```
4. Navigate to the `bin` directory:  
```

cd pycharm-\*/bin

```
5. Run PyCharm:  
```

./pycharm.sh

```

### Step 3: Create Desktop Entry (Optional)

From within PyCharm:  
1. Go to **Tools** > **Create Desktop Entry**.  
2. Check the box to make it available for all users (optional).  





