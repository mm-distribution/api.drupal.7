# FormsTriggeringElementTestCase::testAttemptAccessControlBypass()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 2074–2097 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L2074-L2097)
- **Class:** [FormsTriggeringElementTestCase](../FormsTriggeringElementTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAttemptAccessControlBypass()
```

## Documentation

```text
Test that $form_state['triggering_element'] does not get set to a button
with #access=FALSE.
```

## Code

```php
  function testAttemptAccessControlBypass() {
    $path = 'form-test/clicked-button';
    $form_html_id = 'form-test-clicked-button';

    // Retrieve a form where 'button1' has #access=FALSE and 'button2' doesn't.
    $this->drupalGet($path . '/rs/s');

    // Submit the form with 'button1=button1' in the POST data, which someone
    // trying to get around security safeguards could easily do. We have to do
    // a little trickery here, to work around the safeguards in drupalPost(): by
    // renaming the text field that is in the form to 'button1', we can get the
    // data we want into $_POST.
    $elements = $this->xpath('//form[@id="' . $form_html_id . '"]//input[@name="text"]');
    $elements[0]['name'] = 'button1';
    $this->drupalPost(NULL, array('button1' => 'button1'), NULL, array(), array(), $form_html_id);

    // Ensure that $form_state['triggering_element'] was not set to the
    // restricted button. Do this with both a negative and positive assertion,
    // because negative assertions alone can be brittle. See
    // testNoButtonInfoInPost() for why the triggering element gets set to
    // 'button2'.
    $this->assertNoText('The clicked button is button1.', '$form_state[\'triggering_element\'] not set to a restricted button.');
    $this->assertText('The clicked button is button2.', '$form_state[\'triggering_element\'] not set to a restricted button.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
