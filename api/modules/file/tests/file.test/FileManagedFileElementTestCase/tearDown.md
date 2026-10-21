# FileManagedFileElementTestCase::tearDown()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 394–398 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L394-L398)
- **Class:** [FileManagedFileElementTestCase](../FileManagedFileElementTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
public function tearDown()
```

## Documentation

_No docblock in source._

## Code

```php
  public function tearDown() {
    ini_set('display_errors', $this->originalDisplayErrorsValue);

    parent::tearDown();
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
