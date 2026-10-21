# FieldSqlStorageTestCase::testFieldUpdateFailure()

- **Type:** Method
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.test`](../_file.md), lines 403–427 · [local source](../../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test#L403-L427)
- **Class:** [FieldSqlStorageTestCase](../FieldSqlStorageTestCase.md)
- **Module/theme:** field_sql_storage

## Signature

```php
function testFieldUpdateFailure()
```

## Documentation

```text
Test that failure to create fields is handled gracefully.
```

## Code

```php
  function testFieldUpdateFailure() {
    // Create a text field.
    $field = array('field_name' => 'test_text', 'type' => 'text', 'settings' => array('max_length' => 255));
    $field = field_create_field($field);

    // Attempt to update the field in a way that would break the storage. The
    // parenthesis suffix is needed because SQLite has *very* relaxed rules for
    // data types, so we actually need to provide an invalid SQL syntax in order
    // to break it.
    // @see https://www.sqlite.org/datatype3.html
    $prior_field = $field;
    $field['settings']['max_length'] = '-1)';
    try {
      field_update_field($field);
      $this->fail(t('Update succeeded.'));
    }
    catch (Exception $e) {
      $this->pass(t('Update properly failed.'));
    }

    // Ensure that the field tables are still there.
    foreach (_field_sql_storage_schema($prior_field) as $table_name => $table_info) {
      $this->assertTrue(db_table_exists($table_name), format_string('Table %table exists.', array('%table' => $table_name)));
    }
  }
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test) · Licensed GPL-2.0-or-later (see LICENSE)._
