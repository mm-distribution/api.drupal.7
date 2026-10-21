# SimpleTestFunctionalTest::getTestIdFromResults()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 244–251 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L244-L251)
- **Class:** [SimpleTestFunctionalTest](../SimpleTestFunctionalTest.md)
- **Module/theme:** simpletest

## Signature

```php
function getTestIdFromResults()
```

## Documentation

```text
Fetch the test id from the test results.
```

## Code

```php
  function getTestIdFromResults() {
    foreach ($this->childTestResults['assertions'] as $assertion) {
      if (preg_match('@^Test ID is ([0-9]*)\.$@', $assertion['message'], $matches)) {
        return $matches[1];
      }
    }
    return NULL;
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
