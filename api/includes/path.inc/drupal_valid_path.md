# drupal_valid_path()

- **Type:** Function
- **File:** [`includes/path.inc`](_file.md), lines 558–580 · [local source](../../../source/includes/path.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/path.inc#L558-L580)

## Signature

```php
function drupal_valid_path($path, $dynamic_allowed = FALSE)
```

## Documentation

```text
Checks a path exists and the current user has access to it.

@param $path
  The path to check.
@param $dynamic_allowed
  Whether paths with menu wildcards (like user/%) should be allowed.

@return
  TRUE if it is a valid path AND the current user has access permission,
  FALSE otherwise.
```

## Code

```php
function drupal_valid_path($path, $dynamic_allowed = FALSE) {
  global $menu_admin;
  // We indicate that a menu administrator is running the menu access check.
  $menu_admin = TRUE;
  if ($path == '<front>' || url_is_external($path)) {
    $item = array('access' => TRUE);
  }
  elseif ($dynamic_allowed && preg_match('/\/\%/', $path)) {
    // Path is dynamic (ie 'user/%'), so check directly against menu_router table.
    if ($item = db_query("SELECT * FROM {menu_router} where path = :path", array(':path' => $path))->fetchAssoc()) {
      $item['link_path']  = $item['path'];
      $item['link_title'] = $item['title'];
      $item['external']   = FALSE;
      $item['options'] = '';
      _menu_link_translate($item);
    }
  }
  else {
    $item = menu_get_item($path);
  }
  $menu_admin = FALSE;
  return $item && $item['access'];
}
```

---
_Drupal 7.103 · [includes/path.inc](https://github.com/drupal/drupal/blob/7.103/includes/path.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
