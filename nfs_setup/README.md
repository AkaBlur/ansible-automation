# Linux NFS Role

Setup role for deploying a mapped NFS share onto a host

## Overview

Will create a mount directory where a given set of NFS shares can be mapped
into.

The shares are mounted via a `serviced` entry so that they will persist
reboots.

## Default Vars

```yaml
nfs__server_ip: 10.0.0.2
```
- NFS server address
- Must be a valid IP address

---

```yaml
nfs__server_name: FILES
```
- Hostname of the server
- Will be added as optional hostname in the `hosts` file

---

```yaml
nfs__server_export_path: /export
```
- Export path on the **NFS host** which exports the NFS share
- May be given as **absolute** path

---

```yaml
nfs__mount_dir: /media
```
- Mount path inside the **host**
- Every NFS share will be mounted in here

---

```yaml
nfs__targets:
  - { share_name: "library", mount_point: "library" }
```
- List of NFS share names to include
- Contains the **NFS hosts share name** (exported NFS value)
and the name of the mount point **inside** the **host**

---

```yaml
nfs__security_lvl: sys
```
- Security level of the NFS share

---

```yaml
nfs__perms: rw
```
- Permission for the NFS share
- Only affect system level read/write
- Does not affect user management!

---

```yaml
nfs__version: 4
```
- Version of NFS to use
- Must match NFS version of the NFS host

---

```yaml
nfs__timeout: 30
```
- Timeout when trying to mount the NFS share

---

```yaml
nfs__automount_timeout: 300
```
- Timeout for all directories as automount directories
- Will disconnect the shares after given seconds