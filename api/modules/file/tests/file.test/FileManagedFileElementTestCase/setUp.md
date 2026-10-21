# FileManagedFileElementTestCase::setUp()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 386–392 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L386-L392)
- **Class:** [FileManagedFileElementTestCase](../FileManagedFileElementTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
public function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  public function setUp() {
    parent::setUp();

    // Disable the displaying of errors, so that the AJAX responses are not
    // contaminated with error messages about exceeding the maximum POST size.
    $this->originalDisplayErrorsValue = ini_set('display_errors', '0');
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
