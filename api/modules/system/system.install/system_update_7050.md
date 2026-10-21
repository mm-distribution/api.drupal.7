# system_update_7050()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2548–2550 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2548-L2550)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7050()
```

## Documentation

```text
Change {batch}.id column from serial to regular int.
```

## Code

```php
function system_update_7050() {
  db_change_field('batch', 'bid', 'bid', array('description' => 'Primary Key: Unique batch ID.', 'type' => 'int', 'unsigned' => TRUE, 'not null' => TRUE));
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
