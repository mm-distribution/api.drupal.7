# field_sync_field_status()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 427–442 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L427-L442)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function field_sync_field_status()
```

## Documentation

```text
Refreshes the 'active' and 'storage_active' columns for fields.
```

## Code

```php
function field_sync_field_status() {
  // Refresh the 'active' and 'storage_active' columns according to the current
  // set of enabled modules.
  $modules = module_list();
  foreach ($modules as $module_name) {
    field_associate_fields($module_name);
  }
  db_update('field_config')
    ->fields(array('active' => 0))
    ->condition('module', $modules, 'NOT IN')
    ->execute();
  db_update('field_config')
    ->fields(array('storage_active' => 0))
    ->condition('storage_module', $modules, 'NOT IN')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
