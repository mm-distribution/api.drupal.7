# FileFieldValidateTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1247–1253 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1247-L1253)
- **Class:** [FileFieldValidateTestCase](../FileFieldValidateTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'File field validation tests',
      'description' => 'Tests validation functions such as file type, max file size, max size per node, and required.',
      'group' => 'File',
    );
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
