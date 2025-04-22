# Plex Media Server Role

Manages deployment of a Plex media server on a given hosts with actions
for maintenance.

## Overview

Deploys and manages a Plex media server instance on a given host.
Several different methods allow for remote control of the instance.
This includes:

- Backup creation (main server configuration)

Every mode has its own switch

> [!NOTE]
> It is recommended to only start one mode at a time!
>
> Internally they are mapped in an order, which may not be equal to the
> order of the supplied switch values!

## Mode Switches

```yaml
# Run Backup creation of Plex configuration
plex__do_backup: false
```

## Modes

Individual modes and their usage

### Backup creation

**Switch**
```yaml
plex__do_backup: false
```

**Included variables**
```yaml
plex__backup_directory: /media/backup/plex
plex__backup_user: plex
plex__backup_group: plex
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
