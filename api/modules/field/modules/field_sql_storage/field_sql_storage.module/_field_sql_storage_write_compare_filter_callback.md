# _field_sql_storage_write_compare_filter_callback()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 452–454 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L452-L454)
- **Module/theme:** field_sql_storage

## Signature

```php
function _field_sql_storage_write_compare_filter_callback($value)
```

## Documentation

```text
Callback for array_filter().
```

## Code

```php
function _field_sql_storage_write_compare_filter_callback($value) {
  return NULL !== $value && '' !== $value;
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
