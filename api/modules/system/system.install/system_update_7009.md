# system_update_7009()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2089–2095 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2089-L2095)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7009()
```

## Documentation

```text
Rename the variable for primary links.
```

## Code

```php
function system_update_7009() {
  $current_primary = variable_get('menu_primary_links_source');
  if (isset($current_primary)) {
    variable_set('menu_main_links_source', $current_primary);
    variable_del('menu_primary_links_source');
  }
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
