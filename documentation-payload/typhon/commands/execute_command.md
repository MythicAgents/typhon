+++
title = "execute_command"
chapter = false
weight = 100
hidden = false
+++

## Summary


This runs {command} in a an embedded bash instance within the JAMF process based on the `script` content of a JAMF XML Policy.

WARNING! THIS SCRIPT IS INSERTED DIRECTLY INTO AN XML FILE, IF YOUR SCRIPT CONTAINS CHARACTERS THAT BREAK THE XML INTEGRITY YOU *WILL* HAVE WEIRD BEHAVIOUR!
     
- Needs Admin: False  
- Version: 1  
- Author: @sclow  

### Arguments

#### command

- Description: Command to run  
- Required Value: True  
- Default Value: None  

## Usage
### Without Popup

```
execute_command {command}
```

## MITRE ATT&CK Mapping

- T1059  
## Detailed Summary
This uses the JXA doShellScript command to execute the specified command. A few things to note though:
- This is single threaded, so commands executed in this way have a potential to hang the entire agent
- This spawns `/bin/sh -c [command]` on the command line
- This is actually `/bin/bash` emulating `/bin/sh` which causes some weirdness, so I do some redirection when you try to actually background a task
- This returns results using `\r` instead of `\n` or `\r\n` which is odd, so that is replaced before being returned.