# Ansible Automation

Welcome fellow Internet user 👋

This is a collection of my personal automation tasks and roles I created
for managing several different applications inside my Homelab.

Feel free to explore some of them.

## Roles

Roles dedicated for complex tasks.

- [NFS-Share Deployment](nfs_setup/README.md)
- [SMB-Share Deployment](smb_setup/README.md)
- [Steam Game Server Deployment](steam_server/README.md)
- [Minecraft Game Server](mc_vanilla/README.md)
- [Minecraft Paper Game Server](mc_paper/README.md)
- [Minecraft Velocity Proxy Server](mc_velocity/README.md)

## Task Setups

Simple automation tasks:

- Disable `resolved` stub listener (default on Ubuntu, listens on port 53)
- Deploy an [emby](https://emby.media/) server instance
- Firewall control (via UFW)
- Timezone settings
- Deploy an [unbound](https://www.nlnetlabs.nl/projects/unbound/about/) instance
- Update `apt` packages

Control tasks for complex role setups:

- Manage a Minecraft Vanilla Server instance
- Manage a Minecraft Paper Server instance
- Deploy NFS network shares
- Deploy SMB network shares

## Dev
### Prerequisites
- Python (>= 3.11)
- Installed `requirements.txt`
- Installed Ansible Galaxy roles inside [roles/requirements.yml](roles/requirements.yml)

### Util
**ansible_gen_hashed_pw.sh**

- Generates a hashed password
- For usage inside roles for hashed pw values when deploying new users

