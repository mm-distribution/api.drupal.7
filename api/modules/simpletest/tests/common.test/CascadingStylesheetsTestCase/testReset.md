# CascadingStylesheetsTestCase::testReset()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 812–815 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L812-L815)
- **Class:** [CascadingStylesheetsTestCase](../CascadingStylesheetsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testReset()
```

## Documentation

```text
Makes sure that reseting the CSS empties the cache.
```

## Code

```php
  function testReset() {
    drupal_static_reset('drupal_add_css');
    $this->assertEqual(array(), drupal_add_css(), 'Resetting the CSS empties the cache.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
