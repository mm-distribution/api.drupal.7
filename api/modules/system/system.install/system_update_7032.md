# system_update_7032()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2307–2311 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2307-L2311)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7032()
```

## Documentation

```text
Alter field hostname to identifier in the {flood} table.
```

## Code

```php
function system_update_7032() {
  db_drop_index('flood', 'allow');
  db_change_field('flood', 'hostname', 'identifier', array('type' => 'varchar', 'length' => 128, 'not null' => TRUE, 'default' => ''));
  db_add_index('flood', 'allow', array('event', 'identifier', 'timestamp'));
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
