# Minecraft Velocity Role

Role to deploy a Minecraft Velocity Proxy server instance onto a given host

## Overview

Deploys and manages a Minecraft Velocity Proxy instance on a given host.
Several different methods allow the remote control of the instance. Those
include:

- Installation
- Check for Server Updates
- Install a Server Update

Every mode has its own switch

> [!NOTE]
> It is recommended to only start one mode at a time!
>
> Internally they are mapped in an order, which may not be equal to the
> order of the supplied switch values!

## Mode Switches

```yaml
# install Velocity
mc_velocity_install: false

# check for Velocity update
mc_velocity_check_update: false

# install updated Velocity version
mc_velocity_do_update: false
```

## Modes

Individual modes and their usage

### Installation

**Switch**
```yaml
mc_velocity_install: true
```

**Included variables**
```yaml
mc_velocity__password_hashed:
mc_velocity__openjdk_version:
mc_velocity__proxy_min_ram: 512M
mc_velocity__proxy_max_ram: 512M
mc_velocity__target_version: latest
```

**Installation**

Installs a new Minecraft Velocity Proxy server instance onto the host. Included
is the necessary setup to run the proxy. Currently all proxy server
configurations need to be set manually!

The server will be under the control of a separate user `velocity`. In its home
a dedicated `mc_velocity` will contain the server files. 

When deploying the Velocity instance the installed service on the host will
always run the proxy. Manual control is still possible though.

**Manual Control**

In the home directory of the `velocity` user is a script deployed for manual
control of the server: `mc_velocity_control.sh`.

It allows manual start, stop and messaging. For ease of use all running
instances will be deployed in a screen session.

### Check Update, Apply Update

**Switches**
```yaml
mc_velocity_check_update: true
mc_velocity_do_update: true
```

**Included variables**
```yaml
mc_velocity__target_version: latest

# Check update
mc_velocity__send_telegram_msg: false
mc_velocity__telegram_api_token: 0000000000:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
mc_velocity__telegram_chat_id: 0
```

Checks for an available update with a given Minecraft Velocity version
(either `latest` or a specific, e.g. `340-SNAPSHOT`). Additionally a Telegram
Bot Token can be set and enabled that sends a message to the Bot about a new
version that can be deployed.

When updating the proxy will safely power-cycle and apply the update. Checking
for updates won't apply updates on its own.
