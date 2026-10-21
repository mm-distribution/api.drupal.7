# AJAXTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/ajax.test`](../_file.md), lines 4–10 · [local source](../../../../../../source/modules/simpletest/tests/ajax.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test#L4-L10)
- **Class:** [AJAXTestCase](../AJAXTestCase.md)
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
    $modules = func_get_args();
    if (isset($modules[0]) && is_array($modules[0])) {
      $modules = $modules[0];
    }
    parent::setUp(array_unique(array_merge(array('ajax_test', 'ajax_forms_test'), $modules)));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test) · Licensed GPL-2.0-or-later (see LICENSE)._
