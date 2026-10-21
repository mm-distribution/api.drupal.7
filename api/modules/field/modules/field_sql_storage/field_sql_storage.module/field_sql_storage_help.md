# field_sql_storage_help()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 11–19 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L11-L19)
- **Module/theme:** field_sql_storage
- **Implements:** [hook_help()](../../../../system/system.api.php/hook_help.md)

## Signature

```php
function field_sql_storage_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function field_sql_storage_help($path, $arg) {
  switch ($path) {
    case 'admin/help#field_sql_storage':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Field SQL storage module stores field data in the database. It is the default field storage module; other field storage mechanisms may be available as contributed modules. See the <a href="@field-help">Field module help page</a> for more information about fields.', array('@field-help' => url('admin/help/field'))) . '</p>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
