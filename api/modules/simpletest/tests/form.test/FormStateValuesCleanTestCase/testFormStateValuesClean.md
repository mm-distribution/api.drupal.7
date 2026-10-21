# FormStateValuesCleanTestCase::testFormStateValuesClean()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1647–1673 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1647-L1673)
- **Class:** [FormStateValuesCleanTestCase](../FormStateValuesCleanTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testFormStateValuesClean()
```

## Documentation

```text
Tests form_state_values_clean().
```

## Code

```php
  function testFormStateValuesClean() {
    $values = drupal_json_decode($this->drupalPost('form_test/form-state-values-clean', array(), t('Submit')));

    // Setup the expected result.
    $result = array(
      'beer' => 1000,
      'baz' => array('beer' => 2000),
    );

    // Verify that all internal Form API elements were removed.
    $this->assertFalse(isset($values['form_id']), format_string('%element was removed.', array('%element' => 'form_id')));
    $this->assertFalse(isset($values['form_token']), format_string('%element was removed.', array('%element' => 'form_token')));
    $this->assertFalse(isset($values['form_build_id']), format_string('%element was removed.', array('%element' => 'form_build_id')));
    $this->assertFalse(isset($values['op']), format_string('%element was removed.', array('%element' => 'op')));

    // Verify that all buttons were removed.
    $this->assertFalse(isset($values['foo']), format_string('%element was removed.', array('%element' => 'foo')));
    $this->assertFalse(isset($values['bar']), format_string('%element was removed.', array('%element' => 'bar')));
    $this->assertFalse(isset($values['baz']['foo']), format_string('%element was removed.', array('%element' => 'foo')));
    $this->assertFalse(isset($values['baz']['baz']), format_string('%element was removed.', array('%element' => 'baz')));

    // Verify that nested form value still exists.
    $this->assertTrue(isset($values['baz']['beer']), 'Nested form value still exists.');

    // Verify that actual form values equal resulting form values.
    $this->assertEqual($values, $result, 'Expected form values equal actual form values.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
