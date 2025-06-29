# Ansible Automation

Welcome fellow Internet user 👋

This is a collection of my personal automation tasks and roles I created
for managing several different applications inside my Homelab.

Feel free to explore some of them.

> [!WARNING]
> Many of those roles and tasks may only support Ubuntu / Debian-based distros!
> 
> Others are not tested by me.

## Roles

Roles dedicated for complex tasks:

- [NFS-Share Deployment](nfs_setup/README.md)
- [SMB-Share Deployment](smb_setup/README.md)
- [Steam Game Server Deployment](steam_server/README.md)
- [Minecraft Game Server](mc_vanilla/README.md)
- [Minecraft Paper Game Server](mc_paper/README.md)
- [Minecraft Velocity Proxy Server](mc_velocity/README.md)
- [Cronjob Setup](cron_job/README.md)
- [Plex Media Server Setup](plex_setup/README.md)

## Task Setups

**Simple automation tasks**

- Disable `resolved` stub listener (default on Ubuntu, listens on port 53)
- Deploy an [emby](https://emby.media/) server instance
- Firewall control (via UFW)
- Timezone settings
- Deploy an [unbound](https://www.nlnetlabs.nl/projects/unbound/about/) instance
- Update `apt` packages
- Install cronjobs
- Deploy automated Python scripts
- Deploy a Gitea runner instance (Docker runner)

---

**Control tasks for complex role setups**

Each role has its own variables. See their references for those.

- Manage a Minecraft Vanilla Server instance
- Manage a Minecraft Paper Server instance
- Deploy NFS network shares
- Deploy SMB network shares
- Install a crontab via a control file
- Manage a Plex Media Server instance

---

**Host selection**

Generally (also for my personal Ansible Semaphore setup) hosts will be passed
via the variable `vm_hosts`. This defaults to an empty list. It can be supplied
via the `-e` switch

```bash
ansible-playbook -K some_tasks.yaml -e vm_hosts=myhostgroup
```

Further defined are special variables for simpler tasks setups that can be set:

### Firewall Setup

Requires a list of allowed ports, rules and protocols defined.

For the general policy a value is needed.

**Vars**

```yaml
fw_allow:
  - { port: 420, rule: allow, proto: tcp }
  - { port: 420, rule: allow, proto: udp }
fw_rule_general: deny
```

### Timezone Setup

The timezone setup requires the timezone string.

**Vars**
```yaml
timezone_string: "Europe/Berlin"
```

### Apt Update control

The apt updater needs a Telegram Bot token to notify the user. Yes, this is
hardcoded 😎.

**Vars**

```yaml
telegram_api_token:
telegram_chat_id: 
```

### Unbound

Unbound needs an access control list. This is specified in l3d's
[repository](https://github.com/roles-ansible/ansible_role_unbound) under
`unbound_access_control`

**Vars**

```yaml
unbound_access_allow: ...
```

### Python Automation Deploy

Deploys an automated Python script to the host with supported crontab entry.
Besides the cron and SMB setup roles only the automation user needs to be
specified. Additionally a list of necessary packages (package manager) can
be supplied as well. Furthermore a python virtual environment can be created,
which needs a `requirements.txt` file for pip to install requirements.

**Vars**

```yaml
automation_user:
automation_user_group:
automation_user_pw_hash:
automation_dependencies:
  - package_1
  - package_2
  - ...
automation_install_pyvenv:
```

### Gitea runner deployment

Deploys a Gitea runner on the host machine. The runner is the default Gitea
Docker runner to enable task execution on the host.

Configuration is currently set to the default runner config
(runs `ubuntu` tasks).

**Vars**
```yaml
gitea_address:
gitea_runner_token:
gitea_runner_name:
gitea_runner_user:
gitea_runner_pass:
```

Server address must be entered via `gitea_address`, may be FQDN or some sort of
IP address. Runner token must be specified for Gitea to detect the runner.

Runner labels will be the default `ubuntu-*` ones.

User password must be a hashed password.

## Dev
### Prerequisites

- Python (>= 3.11)
- Installed `requirements.txt`
- Installed Ansible Galaxy roles inside [roles/requirements.yml](roles/requirements.yml)

### Util

**ansible_gen_hashed_pw.sh**

- Generates a hashed password
- For usage inside roles for hashed pw values when deploying new users

