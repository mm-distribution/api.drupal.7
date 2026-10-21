# system_update_7078()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3304–3313 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3304-L3313)
- **Module/theme:** system
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function system_update_7078()
```

## Documentation

```text
Add binary to {date_formats}.format.
```

## Code

```php
function system_update_7078() {
  db_drop_unique_key('date_formats', 'formats');
  db_change_field('date_formats', 'format', 'format', array(
    'description' => 'The date format string.',
    'type' => 'varchar',
    'length' => 100,
    'not null' => TRUE,
    'binary' => TRUE,
  ), array('unique keys' => array('formats' => array('format', 'type'))));
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
