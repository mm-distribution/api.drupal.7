# _search_menu_access()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 295–297 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L295-L297)
- **Module/theme:** search

## Signature

```php
function _search_menu_access($name)
```

## Documentation

```text
Access callback for search tabs.
```

## Code

```php
function _search_menu_access($name) {
  return user_access('search content') && (!function_exists($name . '_search_access') || module_invoke($name, 'search_access'));
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
