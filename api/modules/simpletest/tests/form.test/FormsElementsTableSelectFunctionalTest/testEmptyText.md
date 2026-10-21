# FormsElementsTableSelectFunctionalTest::testEmptyText()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1023–1026 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1023-L1026)
- **Class:** [FormsElementsTableSelectFunctionalTest](../FormsElementsTableSelectFunctionalTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testEmptyText()
```

## Documentation

```text
Test the display of the #empty text when #options is an empty array.
```

## Code

```php
  function testEmptyText() {
    $this->drupalGet('form_test/tableselect/empty-text');
    $this->assertText(t('Empty text.'), 'Empty text should be displayed.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
