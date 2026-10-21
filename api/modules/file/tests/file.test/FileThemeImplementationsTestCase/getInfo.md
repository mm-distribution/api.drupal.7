# FileThemeImplementationsTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 2010–2016 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L2010-L2016)
- **Class:** [FileThemeImplementationsTestCase](../FileThemeImplementationsTestCase.md)
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
      'name' => 'Theme implementations declared in file_theme()',
      'description' => 'Unit tests theme functions in the file module.',
      'group' => 'File',
    );
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
