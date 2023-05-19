+++
title = "add_user"
chapter = false
weight = 100
hidden = false
+++

## Summary

Add a local user to the system using the embedded JAMF functionality. 
- Needs Admin: True  
- Version: 1  
- Author: @calhall 


### Arguments

#### password

- Description: p@55w0rd_here for new user  
- Required Value: True  
- Default Value: None  

#### home_directory

- Description: /Users/.jamf_support  
- Required Value: True  
- Default Value: None  

#### fullname

- Description: Full user name  
- Required Value: True  
- Default Value: Jamf Support User  

#### username

- Description: POSIX username for account  
- Required Value: True  
- Default Value: .jamf_support  

#### administrator

- Description: Should the account be an admin account  
- Required Value: False  
- Default Value: False  

## Usage

```
add_user
```

## MITRE ATT&CK Mapping

- T1136  
- T1169  

## Detailed Summary

This is a very noisy and non-opsec safe command since it results in a new user visible within the authentication dialogue.