+++
title = "jamfserver"
chapter = false
weight = 5
+++

## Overview
This C2 profile consists of HTTP requests from an agent to the C2 profile container, where messages are then forwarded to Mythic's API. The C2 Profile container acts as a proxy between agents and the Mythic server itself.

The Profile is not proxy aware by default - this is a component left as an exercise for the individual agents. 
### C2 Workflow
{{<mermaid>}}
sequenceDiagram
    participant M as Mythic
    participant J as jamfserver Container
    participant A as Agent
    A ->>+ J: POST for tasking
    J ->>+ M: forward request to Mythic
    M -->>- J: reply with tasking
    J -->>- A: reply with tasking
{{< /mermaid >}}
Legend:

- Solid line is a new connection
- Dotted line is a message within that connection

## Configuration Options
The profile reads a `config.json` file for a set of instances of `Sanic` webservers to stand up (`80` by default) and redirects the content.

```JSON
{
  "instances": [
  {
    "ServerHeaders": {
      "Server": "NetDNA-cache/2.2",
      "Cache-Control": "max-age=0, no-cache",
      "Pragma": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/javascript; charset=utf-8"
    },
    "port": 80,
    "key_path": "privkey.pem",
    "cert_path": "fullchain.pem",
    "debug": true,
    "use_ssl": false
    }
  ]
}
```

You can specify the headers that the profile will set on Server responses. If there's an error, the server will return a `404` message based on `server_error_handler` handler in `C2_Profiles/jamfserver/c2_code/server`.

If you want to use SSL within this container specifically, then you can put your key and cert in the `C2_Profiles/jamfserver/c2_code` folder and update the `key_path` and `cert_path` variables to have the `names` of those files. Alternatively, if you specify `use_ssl` as true and you don't have any certs already placed on disk, then the profile will automatically generate some self-signed certs for you to use.
You should get a notification when the server starts with information about the configuration:

```
Messages will disappear when this dialog is closed.
Received Message:
Started with pid: 16...
Output: Opening config and starting instances...
Debugging statements are enabled. This gives more context, but might be a performance hit
not using SSL for port 80
[2020-07-29 21:48:26 +0000] [16] [INFO] Goin' Fast @ http://0.0.0.0:80
```

A note about debugging:
- With `debug` set to `true`, you'll be able to `view stdout/stderr` from within the UI for the container, but it's not recommended to always have this on (especially if you start using something like SOCKS). There can be a lot of traffic and a lot of debugging information captured here which can be both a performance and memory bottleneck depending on your environment and operational timelines.
- It's recommended to have it on initially to help troubleshoot payload connectivity and configuration issues, but then to set it to `false` for actual operations

### Profile Options

#### Callback Host
The URL for the redirector or Mythic server. This must include the protocol to use (e.g. `http://` or `https://`)

#### Callback Port
Number to specify the port number to callback to. This is split out since you don't _have_ to connect to the normal port (i.e. you could connect to http on port 8080). 

#### Headers
This is an array of headers you want to include in your agent for HTTP comms. By default, this includes a standard User-Agent value and an option to add in a Host header for domain fronting. You can then add in as many other custom headers as you want.

## OPSEC

This profile doesn't do any randomization of network components outside of allowing operators to specify internals/jitter. Every POST request for tasking will be the same. This is important to take into consideration for profiling/beaconing analytics. 

## Development

All of the code for the server is Python3 using `Sanic` and located in `C2_Profiles/jamfserver/c2_code/server`. It loops through the `instances` in the `config.json` file and stands up those individual web servers.
