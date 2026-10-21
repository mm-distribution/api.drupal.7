# FieldCrudTestCase::testUpdateNonExistentField()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2719–2728 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2719-L2728)
- **Class:** [FieldCrudTestCase](../FieldCrudTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testUpdateNonExistentField()
```

## Documentation

_No docblock in source._

## Code

```php
  function testUpdateNonExistentField() {
    $test_field = array('field_name' => 'does_not_exist', 'type' => 'number_decimal');
    try {
      field_update_field($test_field);
      $this->fail(t('Cannot update a field that does not exist.'));
    }
    catch (FieldException $e) {
      $this->pass(t('Cannot update a field that does not exist.'));
    }
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
