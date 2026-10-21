# ModuleUnitTest::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/module.test`](../_file.md), lines 25–28 · [local source](../../../../../../source/modules/simpletest/tests/module.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test#L25-L28)
- **Class:** [ModuleUnitTest](../ModuleUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
public function setUp()
```

## Documentation

```text
{@inheritdoc}
```

## Code

```php
  public function setUp() {
    $GLOBALS['drupal_test_info']['test_class'] = __CLASS__;
    parent::setUp();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/module.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test) · Licensed GPL-2.0-or-later (see LICENSE)._
