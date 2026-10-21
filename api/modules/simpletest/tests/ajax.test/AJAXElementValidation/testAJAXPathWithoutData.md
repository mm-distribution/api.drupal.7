# AJAXElementValidation::testAJAXPathWithoutData()

- **Type:** Method
- **File:** [`modules/simpletest/tests/ajax.test`](../_file.md), lines 625–632 · [local source](../../../../../../source/modules/simpletest/tests/ajax.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test#L625-L632)
- **Class:** [AJAXElementValidation](../AJAXElementValidation.md)
- **Module/theme:** batch_test

## Signature

```php
function testAJAXPathWithoutData()
```

## Documentation

```text
Try to open default Ajax callback without passing required data.
```

## Code

```php
  function testAJAXPathWithoutData() {
    $this->drupalGet('system/ajax');
    $query_parameters = array(
      ':type' => 'php',
      ':severity' => WATCHDOG_WARNING,
    );
    $this->assertEqual(db_query('SELECT COUNT(*) FROM {watchdog} WHERE type = :type AND severity = :severity', $query_parameters)->fetchField(), 0, 'No warning message appears in the logs.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test) · Licensed GPL-2.0-or-later (see LICENSE)._
