# FileTokenReplaceTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1486–1492 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1486-L1492)
- **Class:** [FileTokenReplaceTestCase](../FileTokenReplaceTestCase.md)
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
      'name' => 'File token replacement',
      'description' => 'Generates text using placeholders for dummy content to check file token replacement.',
      'group' => 'File',
    );
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
