# system_update_7062()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3092–3096 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3092-L3096)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7062()
```

## Documentation

```text
Replace 'system_list' index with 'bootstrap' index on {system}.
```

## Code

```php
function system_update_7062() {
  db_drop_index('system', 'bootstrap');
  db_drop_index('system', 'system_list');
  db_add_index('system', 'system_list', array('status', 'bootstrap', 'type', 'weight', 'name'));
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
