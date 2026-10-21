# FormValidationTestCase::testMultiFormSameNameErrorClass()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 762–768 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L762-L768)
- **Class:** [FormValidationTestCase](../FormValidationTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMultiFormSameNameErrorClass()
```

## Documentation

```text
 Tests error border of multiple fields with same name in a page.
```

## Code

```php
  function testMultiFormSameNameErrorClass() {
    $this->drupalGet('form-test/double-form');
    $edit = array();
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertFieldByXpath('//input[@id="edit-name" and contains(@class, "error")]', NULL, 'Error input form element class found for first element.');
    $this->assertNoFieldByXpath('//input[@id="edit-name--2" and contains(@class, "error")]', NULL, 'No error input form element class found for second element.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
