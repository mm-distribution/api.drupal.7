# FormsFileInclusionTestCase::testLoadCustomInclude()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 2194–2197 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L2194-L2197)
- **Class:** [FormsFileInclusionTestCase](../FormsFileInclusionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testLoadCustomInclude()
```

## Documentation

```text
Tests loading a custom specified inlcude.
```

## Code

```php
  function testLoadCustomInclude() {
    $this->drupalPost('form-test/load-include-custom', array(), t('Save'));
    $this->assertText('Submit callback called.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
