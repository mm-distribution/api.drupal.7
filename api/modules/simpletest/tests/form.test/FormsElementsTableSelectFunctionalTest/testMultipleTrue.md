# FormsElementsTableSelectFunctionalTest::testMultipleTrue()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 988–1001 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L988-L1001)
- **Class:** [FormsElementsTableSelectFunctionalTest](../FormsElementsTableSelectFunctionalTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testMultipleTrue()
```

## Documentation

```text
Test the display of checkboxes when #multiple is TRUE.
```

## Code

```php
  function testMultipleTrue() {

    $this->drupalGet('form_test/tableselect/multiple-true');

    $this->assertNoText(t('Empty text.'), 'Empty text should not be displayed.');

    // Test for the presence of the Select all rows tableheader.
    $this->assertFieldByXPath('//th[@class="select-all"]', NULL, 'Presence of the "Select all" checkbox.');

    $rows = array('row1', 'row2', 'row3');
    foreach ($rows as $row) {
      $this->assertFieldByXPath('//input[@type="checkbox"]', $row, format_string('Checkbox for value @row.', array('@row' => $row)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
