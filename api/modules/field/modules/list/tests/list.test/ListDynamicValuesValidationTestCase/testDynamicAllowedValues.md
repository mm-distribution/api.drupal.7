# ListDynamicValuesValidationTestCase::testDynamicAllowedValues()

- **Type:** Method
- **File:** [`modules/field/modules/list/tests/list.test`](../_file.md), lines 181–206 · [local source](../../../../../../../../source/modules/field/modules/list/tests/list.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test#L181-L206)
- **Class:** [ListDynamicValuesValidationTestCase](../ListDynamicValuesValidationTestCase.md)
- **Module/theme:** list_test

## Signature

```php
function testDynamicAllowedValues()
```

## Documentation

```text
Test that allowed values function gets the entity.
```

## Code

```php
  function testDynamicAllowedValues() {
    // Verify that the test passes against every value we had.
    foreach ($this->test as $key => $value) {
      $this->entity->test_list[LANGUAGE_NONE][0]['value'] = $value;
      try {
        field_attach_validate('test_entity', $this->entity);
        $this->pass("$key should pass");
      }
      catch (FieldValidationException $e) {
        // This will display as an exception, no need for a separate error.
        throw($e);
      }
    }
    // Now verify that the test does not pass against anything else.
    foreach ($this->test as $key => $value) {
      $this->entity->test_list[LANGUAGE_NONE][0]['value'] = is_numeric($value) ? (100 - $value) : ('X' . $value);
      $pass = FALSE;
      try {
        field_attach_validate('test_entity', $this->entity);
      }
      catch (FieldValidationException $e) {
        $pass = TRUE;
      }
      $this->assertTrue($pass, $key . ' should not pass');
    }
  }
```

---
_Drupal 7.103 · [modules/field/modules/list/tests/list.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test) · Licensed GPL-2.0-or-later (see LICENSE)._
