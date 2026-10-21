# FormsTestCase::testRequiredFields()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 30–126 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L30-L126)
- **Class:** [FormsTestCase](../FormsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRequiredFields()
```

## Documentation

```text
Check several empty values for required forms elements.

Carriage returns, tabs, spaces, and unchecked checkbox elements are not
valid content for a required field.

If the form field is found in form_get_errors() then the test pass.
```

## Code

```php
  function testRequiredFields() {
    // Originates from http://drupal.org/node/117748
    // Sets of empty strings and arrays.
    $empty_strings = array('""' => "", '"\n"' => "\n", '" "' => " ", '"\t"' => "\t", '" \n\t "' => " \n\t ", '"\n\n\n\n\n"' => "\n\n\n\n\n");
    $empty_arrays = array('array()' => array());
    $empty_checkbox = array(NULL);

    $elements['textfield']['element'] = array('#title' => $this->randomName(), '#type' => 'textfield');
    $elements['textfield']['empty_values'] = $empty_strings;

    $elements['password']['element'] = array('#title' => $this->randomName(), '#type' => 'password');
    $elements['password']['empty_values'] = $empty_strings;

    $elements['password_confirm']['element'] = array('#title' => $this->randomName(), '#type' => 'password_confirm');
    // Provide empty values for both password fields.
    foreach ($empty_strings as $key => $value) {
      $elements['password_confirm']['empty_values'][$key] = array('pass1' => $value, 'pass2' => $value);
    }

    $elements['textarea']['element'] = array('#title' => $this->randomName(), '#type' => 'textarea');
    $elements['textarea']['empty_values'] = $empty_strings;

    $elements['radios']['element'] = array('#title' => $this->randomName(), '#type' => 'radios', '#options' => array('' => t('None'), $this->randomName(), $this->randomName(), $this->randomName()));
    $elements['radios']['empty_values'] = $empty_arrays;

    $elements['checkbox']['element'] = array('#title' => $this->randomName(), '#type' => 'checkbox', '#required' => TRUE);
    $elements['checkbox']['empty_values'] = $empty_checkbox;

    $elements['checkboxes']['element'] = array('#title' => $this->randomName(), '#type' => 'checkboxes', '#options' => array($this->randomName(), $this->randomName(), $this->randomName()));
    $elements['checkboxes']['empty_values'] = $empty_arrays;

    $elements['select']['element'] = array('#title' => $this->randomName(), '#type' => 'select', '#options' => array('' => t('None'), $this->randomName(), $this->randomName(), $this->randomName()));
    $elements['select']['empty_values'] = $empty_strings;

    $elements['file']['element'] = array('#title' => $this->randomName(), '#type' => 'file');
    $elements['file']['empty_values'] = $empty_strings;

    // Regular expression to find the expected marker on required elements.
    $required_marker_preg = '@<label.*<span class="form-required" title="This field is required\.">\*</span></label>@';

    // Go through all the elements and all the empty values for them.
    foreach ($elements as $type => $data) {
      foreach ($data['empty_values'] as $key => $empty) {
        foreach (array(TRUE, FALSE) as $required) {
          $form_id = $this->randomName();
          $form = array();
          $form_state = form_state_defaults();
          form_clear_error();
          $form['op'] = array('#type' => 'submit', '#value' => t('Submit'));
          $element = $data['element']['#title'];
          $form[$element] = $data['element'];
          $form[$element]['#required'] = $required;
          $form_state['input'][$element] = $empty;
          $form_state['input']['form_id'] = $form_id;
          $form_state['method'] = 'post';

          // The form token CSRF protection should not interfere with this test,
          // so we bypass it by marking this test form as programmed.
          $form_state['programmed'] = TRUE;
          drupal_prepare_form($form_id, $form, $form_state);
          drupal_process_form($form_id, $form, $form_state);
          $errors = form_get_errors();
          // Form elements of type 'radios' throw all sorts of PHP notices
          // when you try to render them like this, so we ignore those for
          // testing the required marker.
          // @todo Fix this work-around (http://drupal.org/node/588438).
          $form_output = ($type == 'radios') ? '' : drupal_render($form);
          if ($required) {
            // Make sure we have a form error for this element.
            $this->assertTrue(isset($errors[$element]), "Check empty($key) '$type' field '$element'");
            if (!empty($form_output)) {
              // Make sure the form element is marked as required.
              $this->assertTrue(preg_match($required_marker_preg, $form_output), "Required '$type' field is marked as required");
            }
          }
          else {
            if (!empty($form_output)) {
              // Make sure the form element is *not* marked as required.
              $this->assertFalse(preg_match($required_marker_preg, $form_output), "Optional '$type' field is not marked as required");
            }
            if ($type == 'select') {
              // Select elements are going to have validation errors with empty
              // input, since those are illegal choices. Just make sure the
              // error is not "field is required".
              $this->assertTrue((empty($errors[$element]) || strpos('field is required', $errors[$element]) === FALSE), "Optional '$type' field '$element' is not treated as a required element");
            }
            else {
              // Make sure there is *no* form error for this element.
              $this->assertTrue(empty($errors[$element]), "Optional '$type' field '$element' has no errors with empty input");
            }
          }
        }
      }
    }
    // Clear the expected form error messages so they don't appear as exceptions.
    drupal_get_messages();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
