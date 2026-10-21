# entity_info_cache_clear()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8097–8101 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8097-L8101)

## Signature

```php
function entity_info_cache_clear()
```

## Documentation

```text
Resets the cached information about entity types.
```

## Code

```php
function entity_info_cache_clear() {
  drupal_static_reset('entity_get_info');
  // Clear all languages.
  cache_clear_all('entity_info:', 'cache', TRUE);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
