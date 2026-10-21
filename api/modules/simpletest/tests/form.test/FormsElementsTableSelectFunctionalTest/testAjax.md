# FormsElementsTableSelectFunctionalTest::testAjax()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1133–1149 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1133-L1149)
- **Class:** [FormsElementsTableSelectFunctionalTest](../FormsElementsTableSelectFunctionalTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testAjax()
```

## Documentation

```text
Test presence of ajax functionality
```

## Code

```php
  function testAjax() {
    $rows = array('row1', 'row2', 'row3');
    // Test checkboxes (#multiple == TRUE).
    foreach ($rows as $row) {
      $element = 'tableselect[' . $row . ']';
      $edit = array($element => TRUE);
      $result = $this->drupalPostAJAX('form_test/tableselect/multiple-true', $edit, $element);
      $this->assertFalse(empty($result), t('Ajax triggers on checkbox for @row.', array('@row' => $row)));
    }
    // Test radios (#multiple == FALSE).
    $element = 'tableselect';
    foreach ($rows as $row) {
      $edit = array($element => $row);
      $result = $this->drupalPostAjax('form_test/tableselect/multiple-false', $edit, $element);
      $this->assertFalse(empty($result), t('Ajax triggers on radio for @row.', array('@row' => $row)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
