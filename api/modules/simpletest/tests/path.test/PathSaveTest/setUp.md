# PathSaveTest::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/path.test`](../_file.md), lines 360–364 · [local source](../../../../../../source/modules/simpletest/tests/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test#L360-L364)
- **Class:** [PathSaveTest](../PathSaveTest.md)
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
    // Enable a helper module that implements hook_path_update().
    parent::setUp('path_test');
    path_test_reset();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/path.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
