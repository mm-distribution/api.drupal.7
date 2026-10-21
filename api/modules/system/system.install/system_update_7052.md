# system_update_7052()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2562–2564 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2562-L2564)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7052()
```

## Documentation

```text
Rename file to include_file in {menu_router} table.
```

## Code

```php
function system_update_7052() {
  db_change_field('menu_router', 'file', 'include_file', array('type' => 'text', 'size' => 'medium'));
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
