# FileThemeImplementationsTestCase::testThemeFileUploadHelp()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 2018–2024 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L2018-L2024)
- **Class:** [FileThemeImplementationsTestCase](../FileThemeImplementationsTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function testThemeFileUploadHelp()
```

## Documentation

_No docblock in source._

## Code

```php
  function testThemeFileUploadHelp() {
    $variables = array(
      'description' => NULL,
      'upload_validators' => NULL,
    );
    $this->assertEqual('', theme_file_upload_help($variables), 'Empty string returned by theme_file_upload_help() with NULL inputs.');
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
