# SimpleTestFunctionalTest::assertNothing()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 204–206 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L204-L206)
- **Class:** [SimpleTestFunctionalTest](../SimpleTestFunctionalTest.md)
- **Module/theme:** simpletest

## Signature

```php
function assertNothing()
```

## Documentation

```text
Assert nothing.
```

## Code

```php
  function assertNothing() {
    $this->pass("This is nothing.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
