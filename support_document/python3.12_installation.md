*To upgrade Python to version 3.12 on a Linux system, including within WSL (Windows Subsystem for Linux), follow the steps below. This guide will ensure you either install or upgrade Python to the latest 3.12.x version.*

#### Step 1: Update System Packages
- Start by updating your system’s package list to ensure you are installing the latest available packages.
    ```bash
    sudo apt update
    ```

#### Step 2: Install Dependencies for Building Python (if needed)
- If you need to build Python from source (which is recommended for getting the latest version), you will first need to install the necessary build dependencies.
    ```bash
    sudo apt install -y build-essential checkinstall zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev curl
    ```
    These dependencies are needed to compile Python properly from source.
    </br></br>

#### Step 3: Download Python 3.12 Source Code
- Next, download the latest Python 3.12.x release from the official Python website. Use wget to fetch the tarball.
    ```bash
    cd /tmp
    wget https://www.python.org/ftp/python/3.12.0/Python-3.12.0.tgz
    ```
    **Note: You can replace `3.12.0` with the latest minor/patch version if a newer release of Python 3.12 is available.**
    </br></br>

#### Step 4: Extract the Tarball
- Extract the downloaded file:
    ```bash
    tar -xvzf Python-3.12.0.tgz
    cd Python-3.12.0
    ```

#### Step 5: Configure and Build Python 3.12
- Now, configure the build environment and compile Python.
    ```bash
    ./configure --enable-optimizations
    ```
    `--enable-optimizations` is optional but helps optimize the Python binary for performance. This may make the build process take longer.
- After that, start the compilation:
    ```bash
    make -j $(nproc)
    ```
    `-j $(nproc)` speeds up the process by using multiple CPU cores. This is useful for faster builds on multi-core systems.
    </br></br>

#### Step 6: Install Python 3.12
- Once the compilation is complete, install the newly built Python version.
    ```bash
    sudo make altinstall
    ```
    **Note: Using `altinstall` instead of `install` ensures that the default system `python3` remains unchanged and avoids replacing the default Python version, which could break system tools that depend on a specific version.**
    </br></br>

#### Step 7: Verify the Installation
- Check that Python 3.12 is installed correctly by verifying the version:
    ```bash
    python3.12 --version
    ```
- You should see something like:
    ```bash
    Python 3.12.0
    ```

#### Step 8: Set Python 3.12 as the Default (Optional)
- If you want to make Python 3.12 the default `python3` version on your system (i.e., when you run `python3`), you can update the symbolic links.</br>
**Update the `python3` symlink**:
    ```bash
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.12 1
    ```
- If you have multiple versions of Python 3 installed, you can choose the default version interactively.</br>
**Configure the default version (if needed)**:
    ```bash
    sudo update-alternatives --config python3
    ```
    This will display a list of available Python versions. You can select Python 3.12 as the default by choosing its number.
    </br></br>

#### Step 9: Upgrade pip for Python 3.12 (Optional)
- To ensure that pip is upgraded for Python 3.12, use the following commands:
    ```bash
    python3.12 -m ensurepip --upgrade
    python3.12 -m pip install --upgrade pip
    ```