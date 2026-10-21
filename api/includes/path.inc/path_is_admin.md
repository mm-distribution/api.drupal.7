# path_is_admin()

- **Type:** Function
- **File:** [`includes/path.inc`](_file.md), lines 500–508 · [local source](../../../source/includes/path.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/path.inc#L500-L508)

## Signature

```php
function path_is_admin($path)
```

## Documentation

```text
Determines whether a path is in the administrative section of the site.

By default, paths are considered to be non-administrative. If a path does
not match any of the patterns in path_get_admin_paths(), or if it matches
both administrative and non-administrative patterns, it is considered
non-administrative.

@param $path
  A Drupal path.

@return
  TRUE if the path is administrative, FALSE otherwise.

@see path_get_admin_paths()
@see hook_admin_paths()
@see hook_admin_paths_alter()
```

## Code

```php
function path_is_admin($path) {
  $path_map = &drupal_static(__FUNCTION__);
  if (!isset($path_map['admin'][$path])) {
    $patterns = path_get_admin_paths();
    $path_map['admin'][$path] = drupal_match_path($path, $patterns['admin']);
    $path_map['non_admin'][$path] = drupal_match_path($path, $patterns['non_admin']);
  }
  return $path_map['admin'][$path] && !$path_map['non_admin'][$path];
}
```

---
_Drupal 7.103 · [includes/path.inc](https://github.com/drupal/drupal/blob/7.103/includes/path.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
