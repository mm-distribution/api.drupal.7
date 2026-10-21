# SimpleTestBrokenSetUp::tearDown()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 610–619 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L610-L619)
- **Class:** [SimpleTestBrokenSetUp](../SimpleTestBrokenSetUp.md)
- **Module/theme:** simpletest

## Signature

```php
function tearDown()
```

## Documentation

_No docblock in source._

## Code

```php
  function tearDown() {
    // If the test is being run from the main site, tear down normally.
    if (!drupal_valid_test_ua()) {
      parent::tearDown();
    }
    else {
      // If the test is being run from within simpletest, output a message.
      $this->pass(t('The tearDown() method has run.'));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
