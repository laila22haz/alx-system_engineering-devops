# Web Server Project

Welcome to the ALX Africa Web Server Project! In this project, you will learn the fundamentals of setting up and configuring a web server using Nginx on an Ubuntu 16.04 LTS machine. This project aims to teach you essential skills in web server administration, including file transfer, server installation, domain setup, redirection, and error handling.

## Project Overview

In this project, you will perform the following tasks:

1. **Transfer a File to Your Server**: You will write a Bash script that transfers a file from a client to a server using the `scp` command. This script will accept four parameters: the path to the file to be transferred, the IP address of the server, the username for the SSH connection, and the path to the SSH private key.

2. **Install Nginx Web Server**: You will create a Bash script that installs Nginx on your web server (web-01). Nginx should be configuredto listen on port 80 and return a "Hello World!" page when queried at its root with a GET request.

3. **Setup a Domain Name**: You will configure a domain name for your web server. This involves configuring DNS records with an A entry so that your root domain points to your web-01 IP address.

4. **Redirection**: You will configure Nginx to perform a 301 Moved Permanently redirection from the `/redirect_me` path to another page.

5. **Custom 404 Page**: You will configure Nginx to have a custom 404 error page that contains the string "Ceci n'est pas une page" when a page is not found.

## Project Requirements

To successfully complete this project, please note the following requirements:

- You should use the allowed editors: `vi`, `vim`, or `emacs`.
- All your files will be interpreted on Ubuntu 16.04 LTS.
- All your files should end with a newline character.
- A `README.md` file, at the root of the project folder, is mandatory.
- All your Bash script files must be executable.
- Your Bash scripts must pass Shellcheck (version 0.3.7) without any error.
- The first line of all your Bash scripts should be `#!/usr/bin/env bash`.
- The second line of all your Bash scripts should be a comment explaining what the script is doing.
- Do not use `systemctl` for restarting a process.

## Learning Objectives

By the end of this project, you are expected to achieve the following learning objectives:

### General

- Understand the main role of a web server.
- Learn about child processes and why web servers usually have parent and child processes.
- Familiarize yourself with the main HTTP requests.

### DNS

- Learn what DNS stands for and its main role.
- Understand different DNS record types, including A, CNAME, TXT, and MX records.

## Project Structure

The project is organized into multiple tasks, each of which corresponds to a specific configuration or setup on your web server. Be sure to follow the instructions for each task and ensure that your solutions meet the requirements.

## How to Test Your Scripts

You can test your Bash scripts by reproducing the checker environment. Here are the general steps:

1. Start a Ubuntu 16.04 sandbox or virtual machine.
2. Run your script on the sandbox.
3. Observe how it behaves and check if it meets the project requirements.

Remember that the checker will execute your script as the root user, so you do not need to use the `sudo` command.

## Additional Resources

To complete this project successfully, consider referring to the following resources:

- How the web works
- Nginx documentation and tutorials
- Child process concept page
- Understanding DNS, DNS record types
- HTTP requests and response codes
- Linux logs and troubleshooting

## Conclusion

This ALX Africa Web Server Project will equip you with valuable skills in setting up and configuring a web server, which is a fundamental task for any DevOps or System Administrator. Embrace the opportunity to learn, automate, and gain practical experience in web server management. Good luck with your project!