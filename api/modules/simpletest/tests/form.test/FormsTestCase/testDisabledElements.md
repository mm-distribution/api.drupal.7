# FormsTestCase::testDisabledElements()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 327–375 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L327-L375)
- **Class:** [FormsTestCase](../FormsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDisabledElements()
```

## Documentation

```text
Test handling of disabled elements.

@see _form_test_disabled_elements()
```

## Code

```php
  function testDisabledElements() {
    // Get the raw form in its original state.
    $form_state = array();
    $form = _form_test_disabled_elements(array(), $form_state);

    // Build a submission that tries to hijack the form by submitting input for
    // elements that are disabled.
    $edit = array();
    foreach (element_children($form) as $key) {
      if (isset($form[$key]['#test_hijack_value'])) {
        if (is_array($form[$key]['#test_hijack_value'])) {
          foreach ($form[$key]['#test_hijack_value'] as $subkey => $value) {
            $edit[$key . '[' . $subkey . ']'] = $value;
          }
        }
        else {
          $edit[$key] = $form[$key]['#test_hijack_value'];
        }
      }
    }

    // Submit the form with no input, as the browser does for disabled elements,
    // and fetch the $form_state['values'] that is passed to the submit handler.
    $this->drupalPost('form-test/disabled-elements', array(), t('Submit'));
    $returned_values['normal'] = drupal_json_decode($this->content);

    // Do the same with input, as could happen if JavaScript un-disables an
    // element. drupalPost() emulates a browser by not submitting input for
    // disabled elements, so we need to un-disable those elements first.
    $this->drupalGet('form-test/disabled-elements');
    $disabled_elements = array();
    foreach ($this->xpath('//*[@disabled]') as $element) {
      $disabled_elements[] = (string) $element['name'];
      unset($element['disabled']);
    }

    // All the elements should be marked as disabled, including the ones below
    // the disabled container.
    $this->assertEqual(count($disabled_elements), 32, 'The correct elements have the disabled property in the HTML code.');

    $this->drupalPost(NULL, $edit, t('Submit'));
    $returned_values['hijacked'] = drupal_json_decode($this->content);

    // Ensure that the returned values match the form's default values in both
    // cases.
    foreach ($returned_values as $type => $values) {
      $this->assertFormValuesDefault($values, $form);
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
