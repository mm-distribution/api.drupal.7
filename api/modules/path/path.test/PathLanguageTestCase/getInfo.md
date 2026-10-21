# PathLanguageTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/path/path.test`](../_file.md), lines 343–349 · [local source](../../../../../source/modules/path/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test#L343-L349)
- **Class:** [PathLanguageTestCase](../PathLanguageTestCase.md)
- **Module/theme:** path

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
      'name' => 'Path aliases with translated nodes',
      'description' => 'Confirm that paths work with translated nodes',
      'group' => 'Path',
    );
  }
```

---
_Drupal 7.103 · [modules/path/path.test](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
