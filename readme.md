# Python Server Password Changer

This Python script allows you to change passwords for multiple servers using SSH connections. It utilizes the netmiko library to establish SSH connections and execute commands remotely.

## Prerequisites

1. Python 3.x.
2. netmiko library.
3. Access to the servers via SSH

## Installation
1. Clone the repository or download the script file to your local machine.
2. Install the required dependencies using the following command:

```bash
pip install netmiko
```
## Usage

1. Open a terminal or command prompt and navigate to the directory where the script is located.

2. Run the script using the following command:
```bash
python password_changer.py
```
3. The script will prompt you to enter the following information:

- Username: Enter the username to access the servers.

- Password: Enter the password for the specified username.

- New User Password: Enter the new password for the specified username.

- New Root Password: Enter the new password for the root user.

4. The script will read the server IPs from a file named "Servers IPs" in the same directory. Each IP should be listed on a separate line.

5. The script will iterate through the server IPs and attempt to establish an SSH connection.

6. If the connection is successful, the script will change the passwords for both the specified username and the root user.

7. The script will print the status of each server, indicating whether the password change was successful or if there was an error.

**Note:** Make sure to provide the correct file name and path for the "Servers IPs" file in the script.

## Troubleshooting
- If the SSH connection fails, ensure that the servers are accessible via SSH and that the provided username and password are correct.
- If the script encounters any errors during the password change process, check the server logs for more information.

## Disclaimer
Use this script responsibly and with proper authorization. Changing passwords on servers without proper authorization may be a violation of security policies or laws.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on the GitHub repository.

## License
This project is licensed under the MIT License.