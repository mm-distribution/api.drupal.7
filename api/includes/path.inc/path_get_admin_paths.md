# path_get_admin_paths()

- **Type:** Function
- **File:** [`includes/path.inc`](_file.md), lines 522–544 · [local source](../../../source/includes/path.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/path.inc#L522-L544)

## Signature

```php
function path_get_admin_paths()
```

## Documentation

```text
Gets a list of administrative and non-administrative paths.

@return array
  An associative array containing the following keys:
  'admin': An array of administrative paths and regular expressions
           in a format suitable for drupal_match_path().
  'non_admin': An array of non-administrative paths and regular expressions.

@see hook_admin_paths()
@see hook_admin_paths_alter()
```

## Code

```php
function path_get_admin_paths() {
  $patterns = &drupal_static(__FUNCTION__);
  if (!isset($patterns)) {
    $paths = module_invoke_all('admin_paths');
    drupal_alter('admin_paths', $paths);
    // Combine all admin paths into one array, and likewise for non-admin paths,
    // for easier handling.
    $patterns = array();
    $patterns['admin'] = array();
    $patterns['non_admin'] = array();
    foreach ($paths as $path => $enabled) {
      if ($enabled) {
        $patterns['admin'][] = $path;
      }
      else {
        $patterns['non_admin'][] = $path;
      }
    }
    $patterns['admin'] = implode("\n", $patterns['admin']);
    $patterns['non_admin'] = implode("\n", $patterns['non_admin']);
  }
  return $patterns;
}
```

---
_Drupal 7.103 · [includes/path.inc](https://github.com/drupal/drupal/blob/7.103/includes/path.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
