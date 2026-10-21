# filter_format_allowcache()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 649–652 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L649-L652)
- **Module/theme:** filter

## Signature

```php
function filter_format_allowcache($format_id)
```

## Documentation

```text
Checks if the text in a certain text format is allowed to be cached.

This function can be used to check whether the result of the filtering
process can be cached. A text format may allow caching depending on the
filters enabled.

@param $format_id
  The text format ID to check.

@return
  TRUE if the given text format allows caching, FALSE otherwise.
```

## Code

```php
function filter_format_allowcache($format_id) {
  $format = filter_format_load($format_id);
  return !empty($format->cache);
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
