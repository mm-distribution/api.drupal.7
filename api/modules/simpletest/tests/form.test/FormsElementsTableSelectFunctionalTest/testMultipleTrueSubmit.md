# FormsElementsTableSelectFunctionalTest::testMultipleTrueSubmit()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1031–1051 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1031-L1051)
- **Class:** [FormsElementsTableSelectFunctionalTest](../FormsElementsTableSelectFunctionalTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testMultipleTrueSubmit()
```

## Documentation

```text
Test the submission of single and multiple values when #multiple is TRUE.
```

## Code

```php
  function testMultipleTrueSubmit() {

    // Test a submission with one checkbox checked.
    $edit = array();
    $edit['tableselect[row1]'] = TRUE;
    $this->drupalPost('form_test/tableselect/multiple-true', $edit, 'Submit');

    $this->assertText(t('Submitted: row1 = row1'), 'Checked checkbox row1');
    $this->assertText(t('Submitted: row2 = 0'), 'Unchecked checkbox row2.');
    $this->assertText(t('Submitted: row3 = 0'), 'Unchecked checkbox row3.');

    // Test a submission with multiple checkboxes checked.
    $edit['tableselect[row1]'] = TRUE;
    $edit['tableselect[row3]'] = TRUE;
    $this->drupalPost('form_test/tableselect/multiple-true', $edit, 'Submit');

    $this->assertText(t('Submitted: row1 = row1'), 'Checked checkbox row1.');
    $this->assertText(t('Submitted: row2 = 0'), 'Unchecked checkbox row2.');
    $this->assertText(t('Submitted: row3 = row3'), 'Checked checkbox row3.');

  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
