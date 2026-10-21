# UrlAlterFunctionalTest::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/path.test`](../_file.md), lines 141–143 · [local source](../../../../../../source/modules/simpletest/tests/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test#L141-L143)
- **Class:** [UrlAlterFunctionalTest](../UrlAlterFunctionalTest.md)
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
    parent::setUp('path', 'forum', 'url_alter_test');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/path.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
