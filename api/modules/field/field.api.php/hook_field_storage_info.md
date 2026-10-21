# hook_field_storage_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1692–1700 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1692-L1700)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_storage](../../../topics/field_storage.md)

## Signature

```php
function hook_field_storage_info()
```

## Documentation

```text
Expose Field API storage backends.

@return
  An array describing the storage backends implemented by the module.
  The keys are storage backend names. To avoid name clashes, storage backend
  names should be prefixed with the name of the module that exposes them.
  The values are arrays describing the storage backend, with the following
  key/value pairs:
  - label: The human-readable name of the storage backend.
  - description: A short description for the storage backend.
  - settings: An array whose keys are the names of the settings available
    for the storage backend, and whose values are the default values for
    those settings.
```

## Code

```php
function hook_field_storage_info() {
  return array(
    'field_sql_storage' => array(
      'label' => t('Default SQL storage'),
      'description' => t('Stores fields in the local SQL database, using per-field tables.'),
      'settings' => array(),
    ),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_storage_info()".

- [field_sql_storage_field_storage_info()](../modules/field_sql_storage/field_sql_storage.module/field_sql_storage_field_storage_info.md) — `modules/field/modules/field_sql_storage/field_sql_storage.module`
- [field_test_field_storage_info()](../tests/field_test.storage.inc/field_test_field_storage_info.md) — `modules/field/tests/field_test.storage.inc`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
