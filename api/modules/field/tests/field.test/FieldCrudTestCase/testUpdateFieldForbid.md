# FieldCrudTestCase::testUpdateFieldForbid()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2792–2811 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2792-L2811)
- **Class:** [FieldCrudTestCase](../FieldCrudTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testUpdateFieldForbid()
```

## Documentation

```text
Test field type modules forbidding an update.
```

## Code

```php
  function testUpdateFieldForbid() {
    $field = array('field_name' => 'forbidden', 'type' => 'test_field', 'settings' => array('changeable' => 0, 'unchangeable' => 0));
    $field = field_create_field($field);
    $field['settings']['changeable']++;
    try {
      field_update_field($field);
      $this->pass(t("A changeable setting can be updated."));
    }
    catch (FieldException $e) {
      $this->fail(t("An unchangeable setting cannot be updated."));
    }
    $field['settings']['unchangeable']++;
    try {
      field_update_field($field);
      $this->fail(t("An unchangeable setting can be updated."));
    }
    catch (FieldException $e) {
      $this->pass(t("An unchangeable setting cannot be updated."));
    }
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
