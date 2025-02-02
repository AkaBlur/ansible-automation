# Ansible Automation

Welcome fellow Internet user 👋

This is a collection of my personal automation tasks and roles I created
for managing several different applications inside my Homelab.

Feel free to explore some of them.

## Roles

Roles dedicated for complex tasks:

- [NFS-Share Deployment](nfs_setup/README.md)
- [SMB-Share Deployment](smb_setup/README.md)
- [Steam Game Server Deployment](steam_server/README.md)
- [Minecraft Game Server](mc_vanilla/README.md)
- [Minecraft Paper Game Server](mc_paper/README.md)
- [Minecraft Velocity Proxy Server](mc_velocity/README.md)

## Task Setups

**Simple automation tasks**

- Disable `resolved` stub listener (default on Ubuntu, listens on port 53)
- Deploy an [emby](https://emby.media/) server instance
- Firewall control (via UFW)
- Timezone settings
- Deploy an [unbound](https://www.nlnetlabs.nl/projects/unbound/about/) instance
- Update `apt` packages
- Install cronjobs

---

**Control tasks for complex role setups**

Each role has its own variables. See their references for those.

- Manage a Minecraft Vanilla Server instance
- Manage a Minecraft Paper Server instance
- Deploy NFS network shares
- Deploy SMB network shares

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

```yaml
unbound_access_allow: ...
```

### Cronjob setup
The cronjob setup expects a specified cronjob file on the host that acts as
cron facts storage. This is encoded as JSON.

The following variables can be set inside the control file:
- `cron_minute`
- `cron_hour`
- `cron_day`
- `cron_month`
- `cron_weekday`

Example:
```json
{
    "cron_minute": "20",
    "cron_hour": "4"
}
```

This will output `20 4 * * *` inside the crontab entry. When nothing is
supplied for given variable **\* is assumed!**

Further settings include the user the cronjob gets installed, an internally
referenced name (for Ansible) and the command to execute.

**Vars**
```yaml
cronfile: "/file/on/host.something"
cron_description: "My cronjob"
cron_job: "echo 'Meddl Loide' > /dev/null"
cron_user: "root"
```

## Dev
### Prerequisites
- Python (>= 3.11)
- Installed `requirements.txt`
- Installed Ansible Galaxy roles inside [roles/requirements.yml](roles/requirements.yml)

### Util
**ansible_gen_hashed_pw.sh**

- Generates a hashed password
- For usage inside roles for hashed pw values when deploying new users

