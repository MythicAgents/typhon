+++
title = "jamfserver"
chapter = false
weight = 102
+++

## Summary
The `typhon` agent uses a series of `POST` web requests to send responses for tasking and a series of `GET` requests to get tasking from the Mythic server. 

### Profile Option Deviations

#### Callback Host
The URL for the redirector or Mythic server. This must include the protocol to use (e.g. `http://` or `https://`). 
{{% notice warning %}}
The jamf binrary used for the `typhon` agent cannot connect to self signed certs directly .
{{% /notice %}}

#### Callback Port
The TCP port that the `typhon` Payload will connect to on the Callback Host