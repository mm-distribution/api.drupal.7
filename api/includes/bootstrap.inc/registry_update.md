# registry_update()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3632–3650 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3632-L3650)
- **Topics:** [registry](../../topics/registry.md)

## Signature

```php
function registry_update()
```

## Documentation

```text
Updates the registry based on the latest files listed in the database.

This function should be used when system_rebuild_module_data() does not need
to be called, because it is already known that the list of files in the
{system} table matches those in the file system.

@return
  TRUE if the registry was rebuilt, FALSE if another thread was rebuilding
  in parallel and the current thread just waited for completion.

@see registry_rebuild()
```

## Code

```php
function registry_update() {
  // install_system_module() calls module_enable() which calls into this
  // function during initial system installation, so the lock system is neither
  // loaded nor does its storage exist yet.
  $in_installer = drupal_installation_attempted();
  if (!$in_installer && !lock_acquire(__FUNCTION__)) {
    // Another request got the lock, wait for it to finish.
    lock_wait(__FUNCTION__);
    return FALSE;
  }

  require_once DRUPAL_ROOT . '/includes/registry.inc';
  _registry_update();

  if (!$in_installer) {
    lock_release(__FUNCTION__);
  }
  return TRUE;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
