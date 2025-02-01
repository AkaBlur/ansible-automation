# Steam Server Role

Sets up an instance of a Steam server.

## Overview

Provides the possibility to include different **game files** / deployments
through an `applist.txt` which holds all installed games. Those games
get installed with their respecting Steam ID.

An **update** is possible via modification of the `applist.txt` and an updater
script `update_applist.sh`.

**Running** the server is done via `start_server.sh` which will spawn a new
server instance on a Screen on the host. This gives the user the ability to
exit the shell without the server closing.

## Default Vars

```yaml
steam_server__password_hashed: ""
```
- Hashed password for the user `steam`
- Gets deployed as new user on the host

---

```yaml
steam_server__content_install:
  - { app_id: 4020, app_dir: "gmdds" }
```
- Games (via ID) to install in the role

---

```yaml
steam_server__cmd_startup_vars:
  - { name: "MAXPLAYERS", value: 10 }
```
- Startup parameters to include in the runner command
- Can be set like local variables

---

```yaml
steam_server__cmd_startup_cmd: "gmdds/srcds_run \
  +maxplayers ${MAXPLAYERS} -console \
  +gamemode prop_hunt"
```
- Startup command for the server
- Can reference set variables from startup vars
