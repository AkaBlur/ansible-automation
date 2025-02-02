# Minecraft Paper Role

Role to deploy a Minecraft Paper server instance onto a given host

## Overview

Deploys and manages a Minecraft Paper instance on a given host.
Several different methods allow the remote control of the instance. Those
include:

- Installation
- Start / Stop / Restart commands
- Check for Server Updates
- Install a Server Update
- Save the Servers world
- Backup (copy) the Servers world inside the host

Every mode has its own switch

> [!NOTE]
> It is recommended to only start one mode at a time!
>
> Internally they are mapped in an order, which may not be equal to the
> order of the supplied switch values!

## Mode Switches

```yaml
# Install a Minecraft instance
mc_install: false

# Start a managed instance
mc_start: false

# Stop a managed instance
mc_stop: false

# Restart a managed instance
mc_restart: false

# Check for updates on a managed instance
mc_check_update: false

# Update a managed instance
mc_do_update: false

# Save the world on a managed instance
mc_do_save: false

# Copy a saved world from the server somewhere else
mc_do_copy_world: false
```

## Modes

Individual modes and their usage

### Installation

**Switch**
```yaml
mc_install: true
```

**Included variables**
```yaml
mc__openjdk_version:
mc__accept_eula:
mc__password_hashed:
mc__mc_target_version:
mc__prepare_velocity_backend:
mc__velocity_shared_secret:
mc__ramsize_min_init:
mc__ramsize_max:
mc__option_difficulty:
mc__option_gamemode:
mc__option_world_name:
mc__option_max_players:
mc__option_motd:
mc__option_online_mode:
mc__option_pvp:
mc__option_server_ip:
```

**Installation**

Installs a new Minecraft Vanilla server instance onto the host. Included
is the necessary setup to run the server. All variables with `mc__option_` refer
to the `server.properties` settings of the server.

When deploying some simple server settings can be made with the provided
variables.

The server will be under the control of a separate user `mcpaper`. In its home
a dedicated `mc_paper_server` will contain the server files. 

When enabling `mc__prepare_velocity_backend` the server will be setup for a
**Velocity Proxy**. This will put the server into **offline mode!** In that case
a shared secret is needed to ensure secured communication between the server and
the proxy.

**Manual Control**

In the home directory of the `mcpaper` user is a script deployed for manual
control of the server: `mc_server_control.sh`.

It allows manual start, stop and messaging. For ease of use all running
instances will be deployed in a screen session.

### Start, Stop, Restart

**Switches**
```yaml
mc_start: true
mc_stop: true
mc_restart: true
```

No additional variables needed if the role detects the managed Minecraft
instance.

**Start**, **Stop** and **Restart** will always create a screen instance (or
shutdown) within the user `mcpaper` session.

### Check Update, Apply Update

**Switches**
```yaml
mc_check_update: true
mc_do_update: true
```

**Included variables**
```yaml
mc__mc_target_version: latest

# Check update
mc__send_telegram_msg: false
mc__telegram_api_token: 0000000000:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
mc__telegram_chat_id: 000000000
```

Checks for an available update with a given Minecraft version (typical version
string, e.g. 1.20.1). Additionally a Telegram Bot Token can be set and enabled
that sends a message to the Bot about a new version that can be deployed.

When updating the server will safely power-cycle and apply the update. Checking
for updates won't apply updates on its own.

With Minecraft Paper an additional check is performed for an update of Paper
itself (also for the same Minecraft version). This will also notify the user
but only once!

Applying an update will always get the latest build of Paper.

### Saving, Copy to backup

**Switches**
```yaml
mc_do_save: true
mc_do_copy_world: true
```

**Included variables**
```yaml
mc__copy_location: "/tmp"
mc__copy_uid: 1000
mc__copy_gid: 1000
```

This option will power-cycle the server and save the world as `.tar.gz` archive
into the `mcpaper` users home directory.

Optionally a copy operation can also be appended to copy the archive to a given
location **on the host**. This can be also some mapped network share for remote
storage.

**Manual control**

The server save script `mc_server_save_world.sh` inside the `mcpaper` users
home directory can be called manually and will create an archive of the current
servers world.

This file will also be stored inside the users home.