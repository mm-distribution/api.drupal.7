# system_update_7018()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2258–2263 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2258-L2263)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7018()
```

## Documentation

```text
Shorten the {system}.type column and modify indexes.
```

## Code

```php
function system_update_7018() {
  db_drop_index('system', 'modules');
  db_drop_index('system', 'type_name');
  db_change_field('system', 'type', 'type', array('type' => 'varchar', 'length' => 12, 'not null' => TRUE, 'default' => ''));
  db_add_index('system', 'type_name', array('type', 'name'));
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
