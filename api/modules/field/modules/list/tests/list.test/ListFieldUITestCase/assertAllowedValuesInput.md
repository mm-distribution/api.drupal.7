# ListFieldUITestCase::assertAllowedValuesInput()

- **Type:** Method
- **File:** [`modules/field/modules/list/tests/list.test`](../_file.md), lines 477–489 · [local source](../../../../../../../../source/modules/field/modules/list/tests/list.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test#L477-L489)
- **Class:** [ListFieldUITestCase](../ListFieldUITestCase.md)
- **Module/theme:** list_test

## Signature

```php
function assertAllowedValuesInput($input_string, $result, $message)
```

## Documentation

```text
Tests a string input for the 'allowed values' form element.

@param $input_string
  The input string, in the pipe-linefeed format expected by the form
  element.
@param $result
  Either an expected resulting array in
  $field['settings']['allowed_values'], or an expected error message.
@param $message
  Message to display.
```

## Code

```php
  function assertAllowedValuesInput($input_string, $result, $message) {
    $edit = array('field[settings][allowed_values]' => $input_string);
    $this->drupalPost($this->admin_path, $edit, t('Save settings'));

    if (is_string($result)) {
      $this->assertText($result, $message);
    }
    else {
      field_info_cache_clear();
      $field = field_info_field($this->field_name);
      $this->assertIdentical($field['settings']['allowed_values'], $result, $message);
    }
  }
```

---
_Drupal 7.103 · [modules/field/modules/list/tests/list.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test) · Licensed GPL-2.0-or-later (see LICENSE)._
