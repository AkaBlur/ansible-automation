# Cronjob setup

Setup role for installing a cronjob from a supplied file

## Overview

The cronjob setup expects a specified cronjob file on the host that acts as
cron facts storage. This is encoded as JSON.

The following variables can be set inside the control file:
- `cron_minute`
- `cron_hour`
- `cron_day`
- `cron_month`
- `cron_weekday`
- `cron_description`
- `cron_job`

Besides the time settings the job and a description get set. The job is equal
to the exact command that gets executed inside the crontab entry. The
description is just an internal reference for Ansible about this specific
crontab entry.

Example:
```json
{
    "cron_minute": "20",
    "cron_hour": "4",
    "cron_job": "echo 'Hello'",
    "cron_description": "My new task"
}
```

This will output `20 4 * * *` inside the crontab entry. When nothing is
supplied for given time variable **\* is assumed!**

## Default Vars
```yaml
cron_cronfile: "/file/on/host.something"
```
- Supplied cronfile
- File on host

---

```yaml
cron_user: "root"
```
- User into whose crontab the job will be installed