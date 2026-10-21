# drupal_clear_js_cache()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 5268–5272 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L5268-L5272)

## Signature

```php
function drupal_clear_js_cache()
```

## Documentation

```text
Deletes old cached JavaScript files and variables.
```

## Code

```php
function drupal_clear_js_cache() {
  variable_del('javascript_parsed');
  variable_del('drupal_js_cache_files');
  file_scan_directory('public://js', '/.*/', array('callback' => 'drupal_delete_file_if_stale'));
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
