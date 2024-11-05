*To install the AWS CLI (Amazon Web Services Command Line Interface), you can follow the steps below based on your operating system or environment. I'll focus on the common installation methods for Linux (including WSL), macOS, and Windows.*

## Install AWS CLI on Linux (Including WSL)
#### Step 1: Update Your System
- Make sure your system's package list is up to date:
    ```bash
    sudo apt update
    ```

#### Step 2: Install Dependencies (Optional)
- If you don’t have `curl` or `unzip` installed, you can install them:
    ```bash
    sudo apt install curl unzip
    ```

#### Step 3: Download AWS CLI v2
- The AWS CLI v2 is the recommended version. Download the AWS CLI v2 installation script:
    ```bash
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    ```

#### Step 4: Extract the ZIP File
- Unzip the downloaded file:
    ```bash
    unzip awscliv2.zip
    ```

#### Step 5: Install the AWS CLI
- Run the install script:
    ```bash
    sudo ./aws/install
    ```

#### Step 6: Verify the Installation
- Check the installed version of AWS CLI:
    ```bash
    aws --version
    ```
- You should see something like:
    ```bash
    aws-cli/2.x.x Python/3.x.x Linux/4.x.x
    ```

## Install AWS CLI on macOS
#### Step 1: Install via Homebrew (Recommended)
- If you use **Homebrew**, the easiest way to install the AWS CLI is via:
    ```bash
    brew install awscli
    ```

#### Step 2: Verify the Installation
- Check the version:
    ```bash
    aws --version
    ```
- You should see something like:
    ```bash
    aws-cli/2.x.x Python/3.x.x Darwin/19.x.x
    ```

## Install AWS CLI on Windows
#### Step 1: Download the Installer
- Go to the [AWS CLI download page for Windows](https://aws.amazon.com/cli/) and download the latest AWS CLI v2 installer for Windows.

- Alternatively, you can directly download the .msi installer:
    - 64-bit: *`awscli-exe-win64.msi`*
    - 32-bit: *`awscli-exe-win32.msi`*
    </br></br>

#### Step 2: Run the Installer
- Double-click the `.msi` installer and follow the installation prompts.
</br></br>

#### Step 3: Verify the Installation
- Open **Command Prompt** (`cmd`) or **PowerShell** and type:
    ```bash
    aws --version
    ```
- You should see something like:
    ```bash
    aws-cli/2.x.x Python/3.x.x Windows/10
    ```
    </br>
    
## Configure AWS CLI
- Once the AWS CLI is installed, you need to configure it with your AWS credentials (access key and secret access key).
    </br>
    Run the following command:
    ```bash
    aws configure
    ```
- It will prompt you for:

    - **AWS Access Key ID**: You can generate this from the AWS Management Console.
    - **AWS Secret Access Key**: This is associated with your Access Key.
    - **Default region name**: (e.g., `ap-southeast-2`, `us-east-1`, etc.)
    - **Default output format**: (e.g., `json`, `text`, or `table`)
- **Example**:
    ```bash
    aws configure
    AWS Access Key ID [None]: YOUR_ACCESS_KEY
    AWS Secret Access Key [None]: YOUR_SECRET_KEY
    Default region name [None]: ap-southeast-2
    Default output format [None]: json
    ```
    </br>

## Test the AWS CLI
- To ensure everything is set up correctly, you can test the AWS CLI by running a simple command, like listing your S3 buckets:
    ```bash
    aws s3 ls
    ```
    If everything is set up properly, you’ll see a list of your S3 buckets (if you have any).