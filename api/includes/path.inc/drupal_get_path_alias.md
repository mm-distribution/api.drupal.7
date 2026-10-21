# drupal_get_path_alias()

- **Type:** Function
- **File:** [`includes/path.inc`](_file.md), lines 235–245 · [local source](../../../source/includes/path.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/path.inc#L235-L245)

## Signature

```php
function drupal_get_path_alias($path = NULL, $path_language = NULL)
```

## Documentation

```text
Given an internal Drupal path, return the alias set by the administrator.

If no path is provided, the function will return the alias of the current
page.

@param $path
  An internal Drupal path.
@param $path_language
  An optional language code to look up the path in.

@return
  An aliased path if one was found, or the original path if no alias was
  found.
```

## Code

```php
function drupal_get_path_alias($path = NULL, $path_language = NULL) {
  // If no path is specified, use the current page's path.
  if ($path == NULL) {
    $path = $_GET['q'];
  }
  $result = $path;
  if ($alias = drupal_lookup_path('alias', $path, $path_language)) {
    $result = $alias;
  }
  return $result;
}
```

---
_Drupal 7.103 · [includes/path.inc](https://github.com/drupal/drupal/blob/7.103/includes/path.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
