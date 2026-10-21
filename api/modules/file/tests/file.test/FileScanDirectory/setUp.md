# FileScanDirectory::setUp()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1972–1976 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1972-L1976)
- **Class:** [FileScanDirectory](../FileScanDirectory.md)
- **Module/theme:** file_module_test

## Signature

```php
function setUp()
```

## Documentation

```text
{@inheritdoc}
```

## Code

```php
  function setUp() {
    parent::setUp();

    $this->path = 'modules/file/tests/fixtures/file_scan_ignore';
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
