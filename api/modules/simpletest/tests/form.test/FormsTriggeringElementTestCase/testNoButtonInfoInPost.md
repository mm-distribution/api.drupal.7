# FormsTriggeringElementTestCase::testNoButtonInfoInPost()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 2024–2068 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L2024-L2068)
- **Class:** [FormsTriggeringElementTestCase](../FormsTriggeringElementTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testNoButtonInfoInPost()
```

## Documentation

```text
Test the determination of $form_state['triggering_element'] when no button
information is included in the POST data, as is sometimes the case when
the ENTER key is pressed in a textfield in Internet Explorer.
```

## Code

```php
  function testNoButtonInfoInPost() {
    $path = 'form-test/clicked-button';
    $edit = array();
    $form_html_id = 'form-test-clicked-button';

    // Ensure submitting a form with no buttons results in no
    // $form_state['triggering_element'] and the form submit handler not
    // running.
    $this->drupalPost($path, $edit, NULL, array(), array(), $form_html_id);
    $this->assertText('There is no clicked button.', '$form_state[\'triggering_element\'] set to NULL.');
    $this->assertNoText('Submit handler for form_test_clicked_button executed.', 'Form submit handler did not execute.');

    // Ensure submitting a form with one or more submit buttons results in
    // $form_state['triggering_element'] being set to the first one the user has
    // access to. An argument with 'r' in it indicates a restricted
    // (#access=FALSE) button.
    $this->drupalPost($path . '/s', $edit, NULL, array(), array(), $form_html_id);
    $this->assertText('The clicked button is button1.', '$form_state[\'triggering_element\'] set to only button.');
    $this->assertText('Submit handler for form_test_clicked_button executed.', 'Form submit handler executed.');

    $this->drupalPost($path . '/s/s', $edit, NULL, array(), array(), $form_html_id);
    $this->assertText('The clicked button is button1.', '$form_state[\'triggering_element\'] set to first button.');
    $this->assertText('Submit handler for form_test_clicked_button executed.', 'Form submit handler executed.');

    $this->drupalPost($path . '/rs/s', $edit, NULL, array(), array(), $form_html_id);
    $this->assertText('The clicked button is button2.', '$form_state[\'triggering_element\'] set to first available button.');
    $this->assertText('Submit handler for form_test_clicked_button executed.', 'Form submit handler executed.');

    // Ensure submitting a form with buttons of different types results in
    // $form_state['triggering_element'] being set to the first button,
    // regardless of type. For the FAPI 'button' type, this should result in the
    // submit handler not executing. The types are 's'(ubmit), 'b'(utton), and
    // 'i'(mage_button).
    $this->drupalPost($path . '/s/b/i', $edit, NULL, array(), array(), $form_html_id);
    $this->assertText('The clicked button is button1.', '$form_state[\'triggering_element\'] set to first button.');
    $this->assertText('Submit handler for form_test_clicked_button executed.', 'Form submit handler executed.');

    $this->drupalPost($path . '/b/s/i', $edit, NULL, array(), array(), $form_html_id);
    $this->assertText('The clicked button is button1.', '$form_state[\'triggering_element\'] set to first button.');
    $this->assertNoText('Submit handler for form_test_clicked_button executed.', 'Form submit handler did not execute.');

    $this->drupalPost($path . '/i/s/b', $edit, NULL, array(), array(), $form_html_id);
    $this->assertText('The clicked button is button1.', '$form_state[\'triggering_element\'] set to first button.');
    $this->assertText('Submit handler for form_test_clicked_button executed.', 'Form submit handler executed.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
