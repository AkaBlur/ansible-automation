# Plex Media Server Role

Manages deployment of a Plex media server on a given hosts with actions
for maintenance.

## Overview

Deploys and manages a Plex media server instance on a given host.
Several different methods allow for remote control of the instance.
This includes:

- Installation
- Backup creation (main server configuration)
- Backup restoration

Every mode has its own switch

> [!NOTE]
> It is recommended to only start one mode at a time!
>
> Internally they are mapped in an order, which may not be equal to the
> order of the supplied switch values!

## Mode Switches

```yaml
# Install Plex server
plex__do_install: false
# Run Backup creation of Plex configuration
plex__do_backup: false
# Restore Plex backup on host
plex__do_backup_restore: false
```

## Modes

Individual modes and their usage

### Installation

**Switch**
```yaml
plex__do_install: false
```

**Included variables**
```yaml
plex__install_user_password_hashed: XXXXXXX
plex__install_platform: Linux
plex__install_architecture: x86_64
plex__install_distro: debian
```

**Installation**

This will install the latest Plex media server package onto the host system.
For installation the correct host settings need to be supplied with the included
variables.

> [!NOTE]
> 
> Currently only Linux-based installation procedures are defined in this role.

A specific Plex user `plex` will be installed on the host system. For this a
hashed password must be specified.

### Backup creation and restoration

**Switches**
```yaml
plex__do_backup: false
plex__do_backup_restore: false
```

**Included variables**
```yaml
# Backup creation
plex__backup_user: plex
plex__backup_group: plex
# both modes
plex__backup_directory: /media/backup/plex
```

**Backup Creation**

Will create a compressed archive file as backup from the current server
configuration. This includes all main configuration switches and the main
Plex database. See the official
[support entry](https://support.plex.tv/articles/201539237-backing-up-plex-media-server-data/)
for a detailed overview of the contained data.

> [!NOTE]
>
> Currently only the main Linux version of the Plex database will be saved!
> The main location is under /var/lib.

The backup data will be stored inside the host in a remote location specified
(preferable a net-share).

**Backup Restoration**

Will copy the created archive from beforehand (**file name left unchanged!**)
and copies the contents in the original directory from the installed Plex media
server.

A copy of the currently installed database will be made inside the
`Application Support` directory.
