# FileScanDirectory::getInfo()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1961–1967 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1961-L1967)
- **Class:** [FileScanDirectory](../FileScanDirectory.md)
- **Module/theme:** file_module_test

## Signature

```php
public static function getInfo()
```

## Documentation

```text
{@inheritdoc}
```

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'File ScanDirectory',
      'description' => 'Tests the file_scan_directory() function.',
      'group' => 'File',
    );
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
