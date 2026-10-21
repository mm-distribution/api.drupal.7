# system_update_7044()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2465–2469 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2465-L2469)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7044()
```

## Documentation

```text
Drop the actions_aid table.
```

## Code

```php
function system_update_7044() {
  // The current value of the increment has been taken into account when
  // creating the sequences table in update_fix_d7_requirements().
  db_drop_table('actions_aid');
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
