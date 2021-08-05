<p align="center">
  <img alt="Typhon Logo" src="agent_icons/typhon.svg" height="30%" width="30%">
</p>

# Typhon

Typhon is a macOS specific payload aimed at targetting Jamf managed devices. This payload can be used to manipulate macOS devices into communicating with a Mythic instance, which acts as a Jamf server with the ability to execute commands.

## Talks & Publications

- Typhon was presented in the Black Hat USA 2021 talk [Come to the Dark Side, We Have Apples: Turning macOS Management Evil](https://www.blackhat.com/us-21/briefings/schedule/index.html#come-to-the-dark-side-we-have-apples-turning-macos-management-evil-23582).

- Further information about detecting typhon can be found at [TheMacPack.io - Detecting Orthrus and Typhon](https://themacpack.io/posts/Detecting-Orthrus-and-Typhon/)

## Installation
To install typhon, you'll need Mythic installed on a remote computer. You can find installation instructions for Mythic at the [Mythic project page](https://github.com/its-a-feature/Mythic/).

From the Mythic install root, run the command:

`./mythic-cli install github https://github.com/MythicAgents/typhon.git`

Once installed, restart Mythic to build a new agent.

## Notable Features

The typhon agent utilises functionality provided by the Jamf binary. As such no additional code needs to be introduced to the compromised device for this agent to operate.

The client-side Jamf agent contains a variety of functionality that may be utilised by this Mythic payload/profile, however the main focus of the initial release is providing code execution through the agent itself. Any additional feature requests are welcomed. 

## Commands Manual Quick Reference

The agent currently employs three commands that imitate standard Jamf policy instructions.

### Commands 

Command | Syntax | Description
------- | ------ | -----------
add_user | `add_user` | Add a standard or administrative user to the device.
delete_user | `delete_user` | Deletes a user account on the device.
execute_command | `execute_command` | Executes a bash command on the target device with root privileges.

