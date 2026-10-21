# FormsFormWrapperTestCase::testWrapperCallback()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1621–1625 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1621-L1625)
- **Class:** [FormsFormWrapperTestCase](../FormsFormWrapperTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testWrapperCallback()
```

## Documentation

```text
Tests using the form in a usual way.
```

## Code

```php
  function testWrapperCallback() {
    $this->drupalGet('form_test/wrapper-callback');
    $this->assertText('Form wrapper callback element output.', 'The form contains form wrapper elements.');
    $this->assertText('Form builder element output.', 'The form contains form builder elements.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
