# hook_field_storage_details()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1738–1756 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1738-L1756)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_storage](../../../topics/field_storage.md)

## Signature

```php
function hook_field_storage_details($field)
```

## Documentation

```text
Reveal the internal details about the storage for a field.

For example, an SQL storage module might return the Schema API structure for
the table. A key/value storage module might return the server name,
authentication credentials, and bin name.

Field storage modules are not obligated to implement this hook. Modules
that rely on these details must only use them for read operations.

@param $field
  A field structure.

@return
  An array of details.
   - The first dimension is a store type (sql, solr, etc).
   - The second dimension indicates the age of the values in the store
     FIELD_LOAD_CURRENT or FIELD_LOAD_REVISION.
   - Other dimensions are specific to the field storage module.

@see hook_field_storage_details_alter()
```

## Code

```php
function hook_field_storage_details($field) {
  $details = array();

  // Add field columns.
  foreach ((array) $field['columns'] as $column_name => $attributes) {
    $real_name = _field_sql_storage_columnname($field['field_name'], $column_name);
    $columns[$column_name] = $real_name;
  }
  return array(
    'sql' => array(
      FIELD_LOAD_CURRENT => array(
        _field_sql_storage_tablename($field) => $columns,
      ),
      FIELD_LOAD_REVISION => array(
        _field_sql_storage_revision_tablename($field) => $columns,
      ),
    ),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_storage_details()".

- [field_sql_storage_field_storage_details()](../modules/field_sql_storage/field_sql_storage.module/field_sql_storage_field_storage_details.md) — `modules/field/modules/field_sql_storage/field_sql_storage.module`
- [field_test_field_storage_details()](../tests/field_test.storage.inc/field_test_field_storage_details.md) — `modules/field/tests/field_test.storage.inc`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
