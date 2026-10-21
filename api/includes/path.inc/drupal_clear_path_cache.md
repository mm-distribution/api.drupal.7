# drupal_clear_path_cache()

- **Type:** Function
- **File:** [`includes/path.inc`](_file.md), lines 588–592 · [local source](../../../source/includes/path.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/path.inc#L588-L592)

## Signature

```php
function drupal_clear_path_cache($source = NULL)
```

## Documentation

```text
Clear the path cache.

@param $source
  An optional system path for which an alias is being changed.
```

## Code

```php
function drupal_clear_path_cache($source = NULL) {
  // Clear the drupal_lookup_path() static cache.
  drupal_static_reset('drupal_lookup_path');
  drupal_path_alias_whitelist_rebuild($source);
}
```

---
_Drupal 7.103 · [includes/path.inc](https://github.com/drupal/drupal/blob/7.103/includes/path.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
