# FileFieldDisplayTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1140–1146 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1140-L1146)
- **Class:** [FileFieldDisplayTestCase](../FileFieldDisplayTestCase.md)
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
      'name' => 'File field display tests',
      'description' => 'Test the display of file fields in node and views.',
      'group' => 'File',
    );
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
