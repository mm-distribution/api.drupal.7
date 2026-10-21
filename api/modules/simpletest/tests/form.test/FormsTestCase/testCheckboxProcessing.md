# FormsTestCase::testCheckboxProcessing()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 233–256 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L233-L256)
- **Class:** [FormsTestCase](../FormsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testCheckboxProcessing()
```

## Documentation

```text
Test default value handling for checkboxes.

@see _form_test_checkbox()
```

## Code

```php
  function testCheckboxProcessing() {
    // First, try to submit without the required checkbox.
    $edit = array();
    $this->drupalPost('form-test/checkbox', $edit, t('Submit'));
    $this->assertRaw(t('!name field is required.', array('!name' => 'required_checkbox')), 'A required checkbox is actually mandatory');

    // Now try to submit the form correctly.
    $values = drupal_json_decode($this->drupalPost(NULL, array('required_checkbox' => 1), t('Submit')));
    $expected_values = array(
      'disabled_checkbox_on' => 'disabled_checkbox_on',
      'disabled_checkbox_off' => 0,
      'checkbox_on' => 'checkbox_on',
      'checkbox_off' => 0,
      'zero_checkbox_on' => '0',
      'zero_checkbox_off' => 0,
    );
    foreach ($expected_values as $widget => $expected_value) {
      $this->assertIdentical($values[$widget], $expected_value, format_string('Checkbox %widget returns expected value (expected: %expected, got: %value)', array(
        '%widget' => var_export($widget, TRUE),
        '%expected' => var_export($expected_value, TRUE),
        '%value' => var_export($values[$widget], TRUE),
      )));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
