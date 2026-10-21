# system_update_7020()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2268–2271 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2268-L2271)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7020()
```

## Documentation

```text
Enable field and field_ui modules.
```

## Code

```php
function system_update_7020() {
  $module_list = array('field_sql_storage', 'field', 'field_ui');
  module_enable($module_list, FALSE);
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
