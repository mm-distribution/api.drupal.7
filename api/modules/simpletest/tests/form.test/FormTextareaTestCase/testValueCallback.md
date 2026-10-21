# FormTextareaTestCase::testValueCallback()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 2328–2342 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L2328-L2342)
- **Class:** [FormTextareaTestCase](../FormTextareaTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testValueCallback()
```

## Documentation

```text
Tests that textarea value is properly set.
```

## Code

```php
  public function testValueCallback() {
    $element = array();
    $form_state = array();
    $test_cases = array(
      array(NULL, FALSE),
      array(NULL, NULL),
      array('', array('test')),
      array('test', 'test'),
      array('123', 123),
    );
    foreach ($test_cases as $test_case) {
      list($expected, $input) = $test_case;
      $this->assertIdentical($expected, form_type_textarea_value($element, $input, $form_state));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
