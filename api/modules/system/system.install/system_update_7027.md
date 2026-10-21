# system_update_7027()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2286–2289 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2286-L2289)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7027()
```

## Documentation

```text
Enable field type modules.
```

## Code

```php
function system_update_7027() {
  $module_list = array('text', 'number', 'list', 'options');
  module_enable($module_list, FALSE);
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
