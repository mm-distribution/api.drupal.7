# FormsTestCase::testSelect()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 261–320 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L261-L320)
- **Class:** [FormsTestCase](../FormsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSelect()
```

## Documentation

```text
Tests validation of #type 'select' elements.
```

## Code

```php
  function testSelect() {
    $form = $form_state = array();
    $form = form_test_select($form, $form_state);
    $error = '!name field is required.';
    $this->drupalGet('form-test/select');

    // Posting without any values should throw validation errors.
    $this->drupalPost(NULL, array(), 'Submit');
    $this->assertNoText(t($error, array('!name' => $form['select']['#title'])));
    $this->assertNoText(t($error, array('!name' => $form['select_required']['#title'])));
    $this->assertNoText(t($error, array('!name' => $form['select_optional']['#title'])));
    $this->assertNoText(t($error, array('!name' => $form['empty_value']['#title'])));
    $this->assertNoText(t($error, array('!name' => $form['empty_value_one']['#title'])));
    $this->assertText(t($error, array('!name' => $form['no_default']['#title'])));
    $this->assertNoText(t($error, array('!name' => $form['no_default_optional']['#title'])));
    $this->assertText(t($error, array('!name' => $form['no_default_empty_option']['#title'])));
    $this->assertNoText(t($error, array('!name' => $form['no_default_empty_option_optional']['#title'])));
    $this->assertText(t($error, array('!name' => $form['no_default_empty_value']['#title'])));
    $this->assertText(t($error, array('!name' => $form['no_default_empty_value_one']['#title'])));
    $this->assertNoText(t($error, array('!name' => $form['no_default_empty_value_optional']['#title'])));
    $this->assertNoText(t($error, array('!name' => $form['multiple']['#title'])));
    $this->assertNoText(t($error, array('!name' => $form['multiple_no_default']['#title'])));
    $this->assertText(t($error, array('!name' => $form['multiple_no_default_required']['#title'])));

    // Post values for required fields.
    $edit = array(
      'no_default' => 'three',
      'no_default_empty_option' => 'three',
      'no_default_empty_value' => 'three',
      'no_default_empty_value_one' => 'three',
      'multiple_no_default_required[]' => 'three',
    );
    $this->drupalPost(NULL, $edit, 'Submit');
    $values = drupal_json_decode($this->drupalGetContent());

    // Verify expected values.
    $expected = array(
      'select' => 'one',
      'empty_value' => 'one',
      'empty_value_one' => 'one',
      'no_default' => 'three',
      'no_default_optional' => 'one',
      'no_default_optional_empty_value' => '',
      'no_default_empty_option' => 'three',
      'no_default_empty_option_optional' => '',
      'no_default_empty_value' => 'three',
      'no_default_empty_value_one' => 'three',
      'no_default_empty_value_optional' => 0,
      'multiple' => array('two' => 'two'),
      'multiple_no_default' => array(),
      'multiple_no_default_required' => array('three' => 'three'),
    );
    foreach ($expected as $key => $value) {
      $this->assertIdentical($values[$key], $value, format_string('@name: @actual is equal to @expected.', array(
        '@name' => $key,
        '@actual' => var_export($values[$key], TRUE),
        '@expected' => var_export($value, TRUE),
      )));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
