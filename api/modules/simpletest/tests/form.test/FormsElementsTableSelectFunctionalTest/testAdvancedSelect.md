# FormsElementsTableSelectFunctionalTest::testAdvancedSelect()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1065–1080 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1065-L1080)
- **Class:** [FormsElementsTableSelectFunctionalTest](../FormsElementsTableSelectFunctionalTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testAdvancedSelect()
```

## Documentation

```text
Test the #js_select property.
```

## Code

```php
  function testAdvancedSelect() {
    // When #multiple = TRUE a Select all checkbox should be displayed by default.
    $this->drupalGet('form_test/tableselect/advanced-select/multiple-true-default');
    $this->assertFieldByXPath('//th[@class="select-all"]', NULL, 'Display a "Select all" checkbox by default when #multiple is TRUE.');

    // When #js_select is set to FALSE, a "Select all" checkbox should not be displayed.
    $this->drupalGet('form_test/tableselect/advanced-select/multiple-true-no-advanced-select');
    $this->assertNoFieldByXPath('//th[@class="select-all"]', NULL, 'Do not display a "Select all" checkbox when #js_select is FALSE.');

    // A "Select all" checkbox never makes sense when #multiple = FALSE, regardless of the value of #js_select.
    $this->drupalGet('form_test/tableselect/advanced-select/multiple-false-default');
    $this->assertNoFieldByXPath('//th[@class="select-all"]', NULL, 'Do not display a "Select all" checkbox when #multiple is FALSE.');

    $this->drupalGet('form_test/tableselect/advanced-select/multiple-false-advanced-select');
    $this->assertNoFieldByXPath('//th[@class="select-all"]', NULL, 'Do not display a "Select all" checkbox when #multiple is FALSE, even when #js_select is TRUE.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
