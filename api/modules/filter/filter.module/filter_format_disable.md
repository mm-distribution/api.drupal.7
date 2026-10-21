# filter_format_disable()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 299–311 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L299-L311)
- **Module/theme:** filter

## Signature

```php
function filter_format_disable($format)
```

## Documentation

```text
Disables a text format.

There is no core facility to re-enable a disabled format. It is not deleted
to keep information for contrib and to make sure the format ID is never
reused. As there might be content using the disabled format, this would lead
to data corruption.

@param $format
  The text format object to be disabled.
```

## Code

```php
function filter_format_disable($format) {
  db_update('filter_format')
    ->fields(array('status' => 0))
    ->condition('format', $format->format)
    ->execute();

  // Allow modules to react on text format deletion.
  module_invoke_all('filter_format_disable', $format);

  // Clear the filter cache whenever a text format is disabled.
  filter_formats_reset();
  cache_clear_all($format->format . ':', 'cache_filter', TRUE);
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
