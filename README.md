# Port Scanner Tool
![لقطة شاشة 2025-03-12 220537](https://github.com/user-attachments/assets/844dea99-29ab-4b7c-9302-198ef68b04a2)

## Description
The **Port Scanner Tool** is a cybersecurity utility designed to scan open ports on a specified IP address. It helps security professionals assess network security by identifying active services on a target system.

## Features
- Scan a single port or a range of ports on a target IP
- Interactive command-line interface
- Real-time progress updates
- Validates IP addresses and port numbers before scanning

## Requirements
- Python 3.x

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/Abdelrhman-Ahmed1/Port-Scanner.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Port-Scanner
   ```

## Usage
Run the script using Python:
```sh
python3 main.py
```

### Commands:
- `--help` or `-h` : Display available commands and options.
- `pscan [IP_ADDRESS] [PORT]` : Scan a specific port on the target IP.
- `pscan [IP_ADDRESS] [P1]-[P2]` : Scan a range of ports (P1 to P2) on the target IP.
- `--exit` or `-e` : Exit the tool.

### Example Usage:
- Scan port 80 on 192.168.1.1:
  ```sh
  pscan 192.168.1.1 80
  ```
- Scan ports 20 to 100 on 192.168.1.1:
  ```sh
  pscan 192.168.1.1 20-100
  ```

## Disclaimer
This tool is intended for ethical cybersecurity research and educational purposes only. Unauthorized scanning of networks without permission may be illegal.

## Author
- **Name:** Abdelrhman Ahmed
- **Department:** Software Engineer
- **Date of Publish:** 12/03/2025
- **LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/%D9%90abdelrhman-ahmed-82609b296/)

## License
This project is licensed under the MIT License.

