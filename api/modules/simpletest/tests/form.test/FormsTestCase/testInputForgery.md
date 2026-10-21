# FormsTestCase::testInputForgery()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 466–472 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L466-L472)
- **Class:** [FormsTestCase](../FormsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testInputForgery()
```

## Documentation

```text
Test Form API protections against input forgery.

@see _form_test_input_forgery()
```

## Code

```php
  function testInputForgery() {
    $this->drupalGet('form-test/input-forgery');
    $checkbox = $this->xpath('//input[@name="checkboxes[two]"]');
    $checkbox[0]['value'] = 'FORGERY';
    $this->drupalPost(NULL, array('checkboxes[one]' => TRUE, 'checkboxes[two]' => TRUE), t('Submit'));
    $this->assertText('An illegal choice has been detected.', 'Input forgery was detected.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
