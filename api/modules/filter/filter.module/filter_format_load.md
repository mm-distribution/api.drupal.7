# filter_format_load()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 173–176 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L173-L176)
- **Module/theme:** filter

## Signature

```php
function filter_format_load($format_id)
```

## Documentation

```text
Loads a text format object from the database.

@param $format_id
  The format ID.

@return
  A fully-populated text format object, if the requested format exists and
  is enabled. If the format does not exist, or exists in the database but
  has been marked as disabled, FALSE is returned.

@see filter_format_exists()
```

## Code

```php
function filter_format_load($format_id) {
  $formats = filter_formats();
  return isset($formats[$format_id]) ? $formats[$format_id] : FALSE;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
