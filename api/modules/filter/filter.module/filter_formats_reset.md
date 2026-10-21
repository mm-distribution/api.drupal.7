# filter_formats_reset()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 459–464 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L459-L464)
- **Module/theme:** filter

## Signature

```php
function filter_formats_reset()
```

## Documentation

```text
Resets the text format caches.

@see filter_formats()
```

## Code

```php
function filter_formats_reset() {
  cache_clear_all('filter_formats', 'cache', TRUE);
  cache_clear_all('filter_list_format', 'cache', TRUE);
  drupal_static_reset('filter_list_format');
  drupal_static_reset('filter_formats');
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
