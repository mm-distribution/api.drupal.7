# SchemaTestCase::assertFieldCharacteristics()

- **Type:** Method
- **File:** [`modules/simpletest/tests/schema.test`](../_file.md), lines 355–383 · [local source](../../../../../../source/modules/simpletest/tests/schema.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/schema.test#L355-L383)
- **Class:** [SchemaTestCase](../SchemaTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function assertFieldCharacteristics($table_name, $field_name, $field_spec)
```

## Documentation

```text
Assert that a newly added field has the correct characteristics.
```

## Code

```php
  protected function assertFieldCharacteristics($table_name, $field_name, $field_spec) {
    // Check that the initial value has been registered.
    if (isset($field_spec['initial'])) {
      // There should be no row with a value different then $field_spec['initial'].
      $count = db_select($table_name)
        ->fields($table_name, array('serial_column'))
        ->condition($field_name, $field_spec['initial'], '<>')
        ->countQuery()
        ->execute()
        ->fetchField();
      $this->assertEqual($count, 0, 'Initial values filled out.');
    }

    // Check that the default value has been registered.
    if (isset($field_spec['default'])) {
      // Try inserting a row, and check the resulting value of the new column.
      $id = db_insert($table_name)
        ->useDefaults(array('serial_column'))
        ->execute();
      $field_value = db_select($table_name)
        ->fields($table_name, array($field_name))
        ->condition('serial_column', $id)
        ->execute()
        ->fetchField();
      $this->assertEqual($field_value, $field_spec['default'], 'Default value registered.');
    }

    db_drop_field($table_name, $field_name);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/schema.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/schema.test) · Licensed GPL-2.0-or-later (see LICENSE)._
