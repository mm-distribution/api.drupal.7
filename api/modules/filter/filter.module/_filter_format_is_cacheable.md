# _filter_format_is_cacheable()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 669–681 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L669-L681)
- **Module/theme:** filter

## Signature

```php
function _filter_format_is_cacheable($format)
```

## Documentation

```text
Helper function to determine whether the output of a given text format can be cached.

The output of a given text format can be cached when all enabled filters in
the text format allow caching.

@param $format
  The text format object to check.

@return
  TRUE if all the filters enabled in the given text format allow caching,
  FALSE otherwise.

@see filter_format_save()
```

## Code

```php
function _filter_format_is_cacheable($format) {
  if (empty($format->filters)) {
    return TRUE;
  }
  $filter_info = filter_get_filters();
  foreach ($format->filters as $name => $filter) {
    // By default, 'cache' is TRUE for all filters unless specified otherwise.
    if (!empty($filter['status']) && isset($filter_info[$name]['cache']) && !$filter_info[$name]['cache']) {
      return FALSE;
    }
  }
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
