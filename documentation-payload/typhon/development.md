+++
title = "Development"
chapter = false
weight = 20
pre = "<b>3. </b>"
+++

## Development Environment

Unfortunately there isn't a single great environment for doing development of typhon. 

Ultimately your development will result in scripts being delivered to the `execute_command` structure and can be any script that you can write in bash. 

## Adding Commands

Commands can be added within the typhon Payload_Type/typhon/typhon/agent_functions folder. 
Fundamentally you will need to create tasks that modify the "script" parameter to include bash scripts that do not break the XML structure of the JAMF policies. 
