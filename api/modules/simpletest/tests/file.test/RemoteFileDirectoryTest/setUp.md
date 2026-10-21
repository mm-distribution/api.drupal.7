# RemoteFileDirectoryTest::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1248–1251 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1248-L1251)
- **Class:** [RemoteFileDirectoryTest](../RemoteFileDirectoryTest.md)
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
    parent::setUp('file_test');
    variable_set('file_default_scheme', 'dummy-remote');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
