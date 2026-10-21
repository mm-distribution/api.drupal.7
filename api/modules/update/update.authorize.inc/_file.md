# modules/update/update.authorize.inc

- **Source:** [local](../../../../source/modules/update/update.authorize.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.authorize.inc) · 340 lines
- **Module/theme:** update

## File documentation

```text
@file
Callbacks and related functions invoked by authorize.php to update projects.

We use the Batch API to actually update each individual project on the site.
All of the code in this file is run at a low bootstrap level (modules are not
loaded), so these functions cannot assume access to the rest of the code of
the Update Manager module.
```

## Functions (derived index)

- [update_authorize_run_update()](update_authorize_run_update.md) — Updates existing projects when invoked by authorize.php.
- [update_authorize_run_install()](update_authorize_run_install.md) — Installs a new project when invoked by authorize.php.
- [update_authorize_batch_copy_project()](update_authorize_batch_copy_project.md) — Implements callback_batch_operation().
- [update_authorize_update_batch_finished()](update_authorize_update_batch_finished.md) — Implements callback_batch_finished().
- [update_authorize_install_batch_finished()](update_authorize_install_batch_finished.md) — Implements callback_batch_finished().
- [_update_batch_create_message()](_update_batch_create_message.md) — Creates a structure of log messages.
- [_update_authorize_clear_update_status()](_update_authorize_clear_update_status.md) — Clears cached available update status data.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
