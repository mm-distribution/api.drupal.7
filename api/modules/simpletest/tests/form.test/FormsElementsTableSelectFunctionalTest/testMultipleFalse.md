# FormsElementsTableSelectFunctionalTest::testMultipleFalse()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1006–1018 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1006-L1018)
- **Class:** [FormsElementsTableSelectFunctionalTest](../FormsElementsTableSelectFunctionalTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testMultipleFalse()
```

## Documentation

```text
Test the display of radios when #multiple is FALSE.
```

## Code

```php
  function testMultipleFalse() {
    $this->drupalGet('form_test/tableselect/multiple-false');

    $this->assertNoText(t('Empty text.'), 'Empty text should not be displayed.');

    // Test for the absence of the Select all rows tableheader.
    $this->assertNoFieldByXPath('//th[@class="select-all"]', '', 'Absence of the "Select all" checkbox.');

    $rows = array('row1', 'row2', 'row3');
    foreach ($rows as $row) {
      $this->assertFieldByXPath('//input[@type="radio"]', $row, format_string('Radio button for value @row.', array('@row' => $row)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
