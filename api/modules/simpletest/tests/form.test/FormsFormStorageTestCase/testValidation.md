# FormsFormStorageTestCase::testValidation()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1302–1305 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1302-L1305)
- **Class:** [FormsFormStorageTestCase](../FormsFormStorageTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testValidation()
```

## Documentation

```text
Tests validation when form storage is used.
```

## Code

```php
  function testValidation() {
    $this->drupalPost('form_test/form-storage', array('title' => '', 'value' => 'value_is_set'), 'Continue submit');
    $this->assertPattern('/value_is_set/', 'The input values have been kept.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
