# system_action_delete_orphans_post()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 3257–3261 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L3257-L3261)
- **Module/theme:** system

## Signature

```php
function system_action_delete_orphans_post($orphaned)
```

## Documentation

```text
Post-deletion operations for deleting action orphans.

@param $orphaned
  An array of orphaned actions.
```

## Code

```php
function system_action_delete_orphans_post($orphaned) {
  foreach ($orphaned as $callback) {
    drupal_set_message(t("Deleted orphaned action (%action).", array('%action' => $callback)));
  }
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
