# update_manager_local_transfers_allowed()

- **Type:** Function
- **File:** [`modules/update/update.manager.inc`](_file.md), lines 931–943 · [local source](../../../../source/modules/update/update.manager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc#L931-L943)
- **Module/theme:** update
- **Topics:** [update_manager_file](../../../topics/update_manager_file.md)

## Signature

```php
function update_manager_local_transfers_allowed()
```

## Documentation

```text
Determines if file transfers will be performed locally.

If the server is configured such that webserver-created files have the same
owner as the configuration directory (e.g., sites/default) where new code
will eventually be installed, the update manager can transfer files entirely
locally, without changing their ownership (in other words, without prompting
the user for FTP, SSH or other credentials).

This server configuration is an inherent security weakness because it allows
a malicious webserver process to append arbitrary PHP code and then execute
it. However, it is supported here because it is a common configuration on
shared hosting, and there is nothing Drupal can do to prevent it.

@return
  TRUE if local file transfers are allowed on this server, or FALSE if not.

@see update_manager_update_ready_form_submit()
@see update_manager_install_form_submit()
@see install_check_requirements()
```

## Code

```php
function update_manager_local_transfers_allowed() {
  // Compare the owner of a webserver-created temporary file to the owner of
  // the configuration directory to determine if local transfers will be
  // allowed.
  $temporary_file = drupal_tempnam('temporary://', 'update_');
  $local_transfers_allowed = fileowner($temporary_file) === fileowner(conf_path());

  // Clean up. If this fails, we can ignore it (since this is just a temporary
  // file anyway).
  @drupal_unlink($temporary_file);

  return $local_transfers_allowed;
}
```

---
_Drupal 7.103 · [modules/update/update.manager.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
