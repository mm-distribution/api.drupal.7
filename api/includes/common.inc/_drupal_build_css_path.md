# _drupal_build_css_path()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 3803–3818 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L3803-L3818)

## Signature

```php
function _drupal_build_css_path($matches, $base = NULL)
```

## Documentation

```text
Prefixes all paths within a CSS file for drupal_build_css_cache().
```

## Code

```php
function _drupal_build_css_path($matches, $base = NULL) {
  $_base = &drupal_static(__FUNCTION__);
  // Store base path for preg_replace_callback.
  if (isset($base)) {
    $_base = $base;
  }

  // Prefix with base and remove '../' segments where possible.
  $path = $_base . (isset($matches[1]) ? $matches[1] : '');
  $last = '';
  while ($path != $last) {
    $last = $path;
    $path = preg_replace('`(^|/)(?!\.\./)([^/]+)/\.\./`', '$1', $path);
  }
  return 'url(' . $path . ')';
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
