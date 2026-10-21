# path_admin_edit()

- **Type:** Function
- **File:** [`modules/path/path.admin.inc`](_file.md), lines 104–114 · [local source](../../../../source/modules/path/path.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc#L104-L114)
- **Module/theme:** path

## Signature

```php
function path_admin_edit($path = array())
```

## Documentation

```text
Page callback: Returns a form creating or editing a path alias.

@param $path
  An array containing the path ID, source, alias, and language code.

@return
  A form for adding or editing a URL alias.

@see path_menu()
```

## Code

```php
function path_admin_edit($path = array()) {
  if ($path) {
    drupal_set_title($path['alias']);
    $output = drupal_get_form('path_admin_form', $path);
  }
  else {
    $output = drupal_get_form('path_admin_form');
  }

  return $output;
}
```

---
_Drupal 7.103 · [modules/path/path.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
