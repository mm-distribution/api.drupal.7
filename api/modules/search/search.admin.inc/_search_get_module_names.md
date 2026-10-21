# _search_get_module_names()

- **Type:** Function
- **File:** [`modules/search/search.admin.inc`](_file.md), lines 31–41 · [local source](../../../../source/modules/search/search.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.admin.inc#L31-L41)
- **Module/theme:** search

## Signature

```php
function _search_get_module_names()
```

## Documentation

```text
Helper function to get real module names.
```

## Code

```php
function _search_get_module_names() {

  $search_info = search_get_info(TRUE);
  $system_info = system_get_info('module');
  $names = array();
  foreach ($search_info as $module => $info) {
    $names[$module] = $system_info[$module]['name'];
  }
  asort($names, SORT_STRING);
  return $names;
}
```

---
_Drupal 7.103 · [modules/search/search.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/search/search.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
