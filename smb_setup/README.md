# Linux NFS Role

Setup role for deploying a mapped SMB share onto a host

## Overview

Will create a mount directory where a given set of SMB shares can be mapped
into.

The shares are mounted via a `serviced` entry so that they will persist
reboots.

## Default Vars

```yaml
smb__user: user
smb__pass: password
```
- Default credentials for the SMB user
- Will be stored as `root`-protected file on the host

---

```yaml
smb__server_ip: 10.0.0.2
```
- SMB server address
- Must be a valid IP address

---

```yaml
smb__server_name: FILES
```
- Hostname of the server
- Will be added as optional hostname in the `hosts` file

---

```yaml
smb__mount_dir: /media
```
- Mount path inside the **host**
- Every SMB share will be mounted in here

---

```yaml
smb__targets:
  - { share_name: "library", mount_point: "library" }
```
- List of SMB share names to include
- Contains the **SMB hosts share name** (exported SMB name)
and the name of the mount point **inside** the **host**

---

```yaml
smb__uid: 1000
smb__gid: 1000
```
- UID and GID for the given shares to set
- May be set to the **local hosts** UID and GID

---

```yaml
smb__perms: rw
```
- Default permissions for the deployed SMB shares

---

```yaml
smb__charset: utf8
```
- Default charset to use inside the SMB share
- Imported on filesystem level

---

```yaml
smb__timeout: 30
```
- Timeout when trying to mount the SMB share

---

```yaml
smb__automount_timeout: 300
```
- Timeout for all directories as automount directories
- Will disconnect the shares after given seconds