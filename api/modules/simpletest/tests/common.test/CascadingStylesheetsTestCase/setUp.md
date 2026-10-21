# CascadingStylesheetsTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 757–761 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L757-L761)
- **Class:** [CascadingStylesheetsTestCase](../CascadingStylesheetsTestCase.md)
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
    parent::setUp('php', 'locale', 'common_test');
    // Reset drupal_add_css() before each test.
    drupal_static_reset('drupal_add_css');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
