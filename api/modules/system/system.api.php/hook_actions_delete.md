# hook_actions_delete()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4052–4056 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4052-L4056)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_actions_delete($aid)
```

## Documentation

```text
Executes code after an action is deleted.

@param $aid
  The action ID.
```

## Code

```php
function hook_actions_delete($aid) {
  db_delete('actions_assignments')
    ->condition('aid', $aid)
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_actions_delete()".

- [trigger_actions_delete()](../../trigger/trigger.module/trigger_actions_delete.md) — `modules/trigger/trigger.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
