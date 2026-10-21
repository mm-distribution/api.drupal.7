# UpdateTestUploadCase::getInfo()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 700–706 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L700-L706)
- **Class:** [UpdateTestUploadCase](../UpdateTestUploadCase.md)
- **Module/theme:** update

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
      'name' => 'Upload and extract module functionality',
      'description' => 'Tests the Update Manager module\'s upload and extraction functionality.',
      'group' => 'Update',
    );
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
