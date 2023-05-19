+++
title = "typhon"
chapter = false
weight = 5
+++

![logo](/agents/typhon/typhon.svg?width=200px)
## Summary

typhon is a MythicAgent for macOS that emulates a JAMF server. 

### Highlighted Agent Features
- This agent operates by overriding the JAMF server location on a legitimate JAMF installation.
- When JAMF polls; then the agent will talk to the configured jamfserver instead of the legitimate host.
- The legitimate host will not know that the JAMF client has been overriden
- The typhon jamfserver will execute commands wrapped in valid XML policy files for JAMF. 


### Important Notes
The entire agent is single threaded due to the nature of executing singular commands wrapped within a JAMF policy file.

## Authors
@sclow

### Special Thanks to These Contributors
- @its_a_feature_
- @calhall
