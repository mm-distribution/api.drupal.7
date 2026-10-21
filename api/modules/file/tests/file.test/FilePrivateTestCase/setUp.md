# FilePrivateTestCase::setUp()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1569–1573 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1569-L1573)
- **Class:** [FilePrivateTestCase](../FilePrivateTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp(array('node_access_test', 'field_test'));
    node_access_rebuild();
    variable_set('node_access_test_private', TRUE);
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
