# ListFieldUITestCase::testListAllowedValuesBoolean()

- **Type:** Method
- **File:** [`modules/field/modules/list/tests/list.test`](../_file.md), lines 400–422 · [local source](../../../../../../../../source/modules/field/modules/list/tests/list.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test#L400-L422)
- **Class:** [ListFieldUITestCase](../ListFieldUITestCase.md)
- **Module/theme:** list_test

## Signature

```php
function testListAllowedValuesBoolean()
```

## Documentation

```text
List (boolen) : test 'On/Off' values input.
```

## Code

```php
  function testListAllowedValuesBoolean() {
    $this->field_name = 'field_list_boolean';
    $this->createListField('list_boolean');

    // Check that the separate 'On' and 'Off' form fields work.
    $on = $this->randomName();
    $off = $this->randomName();
    $allowed_values = array(1 => $on, 0 => $off);
    $edit = array(
      'on' => $on,
      'off' => $off,
    );
    $this->drupalPost($this->admin_path, $edit, t('Save settings'));
    $this->assertText("Saved field_list_boolean configuration.", "The 'On' and 'Off' form fields work for boolean fields.");
    // Test the allowed_values on the field settings form.
    $this->drupalGet($this->admin_path);
    $this->assertFieldByName('on', $on, "The 'On' value is stored correctly.");
    $this->assertFieldByName('off', $off, "The 'Off' value is stored correctly.");
    $field = field_info_field($this->field_name);
    $this->assertEqual($field['settings']['allowed_values'], $allowed_values, 'The allowed value is correct');
    $this->assertFalse(isset($field['settings']['on']), 'The on value is not saved into settings');
    $this->assertFalse(isset($field['settings']['off']), 'The off value is not saved into settings');
  }
```

---
_Drupal 7.103 · [modules/field/modules/list/tests/list.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test) · Licensed GPL-2.0-or-later (see LICENSE)._
