+++
title = "OPSEC"
chapter = false
weight = 10
pre = "<b>1. </b>"
+++

## Considerations

- The agent is single-threaded. While most times this won't be an issue (other than only being able to run one command at a time), this comes into play for the `execute_command` command since it spawns a shell command and _wait for the program to finish_. So, if you run something like `execute_command sudo whoami` and sudo prompts for the password, your agent will never come back because it's waiting for that input.


### Process Execution

- The `execute_command` command spawns and internal copy of `/bin/bash` which may be subject to command-line logging.

### Potential Popups

The following commands can generate popups:
- `add_user` - may generate a popup asking for terminal to administer users and accounts.
- `delete_user` - may generate a popup asking for terminal to administer users and accounts.
