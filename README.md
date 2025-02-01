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