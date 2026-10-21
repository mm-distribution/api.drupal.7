# PathLanguageUITestCase::getInfo()

- **Type:** Method
- **File:** [`modules/path/path.test`](../_file.md), lines 484–490 · [local source](../../../../../source/modules/path/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test#L484-L490)
- **Class:** [PathLanguageUITestCase](../PathLanguageUITestCase.md)
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
      'name' => 'Path aliases with languages',
      'description' => 'Confirm that the Path module user interface works with languages.',
      'group' => 'Path',
    );
  }
```

---
_Drupal 7.103 · [modules/path/path.test](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
