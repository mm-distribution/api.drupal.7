# system_update_7071()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3212–3220 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3212-L3220)
- **Module/theme:** system
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function system_update_7071()
```

## Documentation

```text
Add index missed during upgrade, and fix field default.
```

## Code

```php
function system_update_7071() {
  db_drop_index('date_format_type', 'title');
  db_add_index('date_format_type', 'title', array('title'));
  db_change_field('registry', 'filename', 'filename', array(
    'type' => 'varchar',
    'length' => 255,
    'not null' => TRUE,
  ));
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
