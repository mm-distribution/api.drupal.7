# field_sql_storage_field_storage_info()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 24–31 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L24-L31)
- **Module/theme:** field_sql_storage
- **Implements:** [hook_field_storage_info()](../../../field.api.php/hook_field_storage_info.md)

## Signature

```php
function field_sql_storage_field_storage_info()
```

## Documentation

```text
Implements hook_field_storage_info().
```

## Code

```php
function field_sql_storage_field_storage_info() {
  return array(
    'field_sql_storage' => array(
      'label' => t('Default SQL storage'),
      'description' => t('Stores fields in the local SQL database, using per-field tables.'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
