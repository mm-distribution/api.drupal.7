# drupal_clear_css_cache()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 3967–3970 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L3967-L3970)

## Signature

```php
function drupal_clear_css_cache()
```

## Documentation

```text
Deletes old cached CSS files.
```

## Code

```php
function drupal_clear_css_cache() {
  variable_del('drupal_css_cache_files');
  file_scan_directory('public://css', '/.*/', array('callback' => 'drupal_delete_file_if_stale'));
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
