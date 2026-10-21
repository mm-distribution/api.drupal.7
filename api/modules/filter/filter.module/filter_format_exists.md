# filter_format_exists()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 326–328 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L326-L328)
- **Module/theme:** filter

## Signature

```php
function filter_format_exists($format_id)
```

## Documentation

```text
Determines if a text format exists.

@param $format_id
  The ID of the text format to check.

@return
  TRUE if the text format exists, FALSE otherwise. Note that for disabled
  formats filter_format_exists() will return TRUE while filter_format_load()
  will return FALSE.

@see filter_format_load()
```

## Code

```php
function filter_format_exists($format_id) {
  return (bool) db_query_range('SELECT 1 FROM {filter_format} WHERE format = :format', 0, 1, array(':format' => $format_id))->fetchField();
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
