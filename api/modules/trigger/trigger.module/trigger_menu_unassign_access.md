# trigger_menu_unassign_access()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 86–95 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L86-L95)
- **Module/theme:** trigger

## Signature

```php
function trigger_menu_unassign_access()
```

## Documentation

```text
Access callback: Determines if triggers can be unassigned.

@return bool
  TRUE if there are triggers that the user can unassign, FALSE otherwise.

@see trigger_menu()
```

## Code

```php
function trigger_menu_unassign_access() {
  if (!user_access('administer actions')) {
    return FALSE;
  }
  $count = db_select('trigger_assignments')
    ->countQuery()
    ->execute()
    ->fetchField();
  return $count > 0;
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
