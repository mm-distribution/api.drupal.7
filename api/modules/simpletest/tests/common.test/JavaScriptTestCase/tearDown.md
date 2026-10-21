# JavaScriptTestCase::tearDown()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1548–1552 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1548-L1552)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function tearDown()
```

## Documentation

_No docblock in source._

## Code

```php
  function tearDown() {
    // Restore configured value for JavaScript preprocessing.
    variable_set('preprocess_js', $this->preprocess_js);
    parent::tearDown();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
