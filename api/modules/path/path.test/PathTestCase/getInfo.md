# PathTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/path/path.test`](../_file.md), lines 12–18 · [local source](../../../../../source/modules/path/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test#L12-L18)
- **Class:** [PathTestCase](../PathTestCase.md)
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
      'name' => 'Path alias functionality',
      'description' => 'Add, edit, delete, and change alias and verify its consistency in the database.',
      'group' => 'Path',
    );
  }
```

---
_Drupal 7.103 · [modules/path/path.test](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
