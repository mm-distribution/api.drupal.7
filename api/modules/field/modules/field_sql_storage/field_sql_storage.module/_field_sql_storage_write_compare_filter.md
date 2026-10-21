# _field_sql_storage_write_compare_filter()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 468–490 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L468-L490)
- **Module/theme:** field_sql_storage

## Signature

```php
function _field_sql_storage_write_compare_filter($field, $array)
```

## Documentation

```text
Cleanup field values for later values comparison.

@param array $field
  Field info as returned by field_info_field_by_id().

@param array $array
  Field values to cleanup.

@return array
  Filtered values.
```

## Code

```php
function _field_sql_storage_write_compare_filter($field, $array) {
  foreach ($array as $language => $items) {
    if (empty($items)) {
      unset($array[$language]);
    }
    else {
      foreach ($items as $delta => $item) {
        // This should not happen but some modules provide invalid data to the
        // field API.
        if (!is_array($item)) {
          continue;
        }
        // Let's start by pruning empty values and non storable values.
        $array[$language][$delta] = array_filter(array_intersect_key($item, $field['columns']), '_field_sql_storage_write_compare_filter_callback');
        // Ordering is important because for widget elements and loaded columns
        // from database order might differ and give false positives on field
        // value change, especially with complex fields such as image fields.
        ksort($array[$language][$delta]);
      }
    }
  }
  return $array;
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
