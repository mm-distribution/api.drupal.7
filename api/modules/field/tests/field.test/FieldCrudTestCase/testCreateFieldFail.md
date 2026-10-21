# FieldCrudTestCase::testCreateFieldFail()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2522–2543 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2522-L2543)
- **Class:** [FieldCrudTestCase](../FieldCrudTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testCreateFieldFail()
```

## Documentation

```text
Test failure to create a field.
```

## Code

```php
  function testCreateFieldFail() {
    $field_name = 'duplicate';
    $field_definition = array('field_name' => $field_name, 'type' => 'test_field', 'storage' => array('type' => 'field_test_storage_failure'));
    $query = db_select('field_config')->condition('field_name', $field_name)->countQuery();

    // The field does not appear in field_config.
    $count = $query->execute()->fetchField();
    $this->assertEqual($count, 0, 'A field_config row for the field does not exist.');

    // Try to create the field.
    try {
      $field = field_create_field($field_definition);
      $this->assertTrue(FALSE, 'Field creation (correctly) fails.');
    }
    catch (Exception $e) {
      $this->assertTrue(TRUE, 'Field creation (correctly) fails.');
    }

    // The field does not appear in field_config.
    $count = $query->execute()->fetchField();
    $this->assertEqual($count, 0, 'A field_config row for the field does not exist.');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
