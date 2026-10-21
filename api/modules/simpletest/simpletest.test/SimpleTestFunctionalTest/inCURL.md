# SimpleTestFunctionalTest::inCURL()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 341–343 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L341-L343)
- **Class:** [SimpleTestFunctionalTest](../SimpleTestFunctionalTest.md)
- **Module/theme:** simpletest

## Signature

```php
function inCURL()
```

## Documentation

```text
Check if the test is being run from inside a CURL request.
```

## Code

```php
  function inCURL() {
    return (bool) drupal_valid_test_ua();
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
