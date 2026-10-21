# system_actions_remove_orphans()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 3266–3269 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L3266-L3269)
- **Module/theme:** system

## Signature

```php
function system_actions_remove_orphans()
```

## Documentation

```text
Remove actions that are in the database but not supported by any enabled module.
```

## Code

```php
function system_actions_remove_orphans() {
  actions_synchronize(TRUE);
  drupal_goto('admin/config/system/actions/manage');
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
