# system_find_base_themes()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2731–2733 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2731-L2733)
- **Module/theme:** system

## Signature

```php
function system_find_base_themes($themes, $key, $used_keys = array())
```

## Documentation

```text
Find all the base themes for the specified theme.

This function has been deprecated in favor of drupal_find_base_themes().
```

## Code

```php
function system_find_base_themes($themes, $key, $used_keys = array()) {
  return drupal_find_base_themes($themes, $key, $used_keys);
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
