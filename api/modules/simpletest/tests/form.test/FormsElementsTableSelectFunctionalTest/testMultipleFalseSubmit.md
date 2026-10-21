# FormsElementsTableSelectFunctionalTest::testMultipleFalseSubmit()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1056–1060 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1056-L1060)
- **Class:** [FormsElementsTableSelectFunctionalTest](../FormsElementsTableSelectFunctionalTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testMultipleFalseSubmit()
```

## Documentation

```text
Test submission of values when #multiple is FALSE.
```

## Code

```php
  function testMultipleFalseSubmit() {
    $edit['tableselect'] = 'row1';
    $this->drupalPost('form_test/tableselect/multiple-false', $edit, 'Submit');
    $this->assertText(t('Submitted: row1'), 'Selected radio button');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
