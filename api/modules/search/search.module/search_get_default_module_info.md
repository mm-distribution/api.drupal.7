# search_get_default_module_info()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 281–290 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L281-L290)
- **Module/theme:** search

## Signature

```php
function search_get_default_module_info()
```

## Documentation

```text
Returns information about the default search module.

@return
   The search_get_info() array element for the default search module, if any.
```

## Code

```php
function search_get_default_module_info() {
  $info = search_get_info();
  $default = variable_get('search_default_module', 'node');
  if (isset($info[$default])) {
    return $info[$default];
  }
  // The variable setting does not match any active module, so just return
  // the info for the first active module (if any).
  return reset($info);
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
