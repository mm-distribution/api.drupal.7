# JavaScriptTestCase::resetStaticVariables()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2056–2060 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2056-L2060)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function resetStaticVariables()
```

## Documentation

```text
Resets static variables related to adding JavaScript to a page.
```

## Code

```php
  function resetStaticVariables() {
    drupal_static_reset('drupal_add_js');
    drupal_static_reset('drupal_add_library');
    drupal_static_reset('drupal_get_library');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
