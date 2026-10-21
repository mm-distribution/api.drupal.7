# DrupalHTTPRequestTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1162–1164 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1162-L1164)
- **Class:** [DrupalHTTPRequestTestCase](../DrupalHTTPRequestTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('system_test', 'locale');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
