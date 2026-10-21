# PathMonolingualTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/path/path.test`](../_file.md), lines 560–566 · [local source](../../../../../source/modules/path/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test#L560-L566)
- **Class:** [PathMonolingualTestCase](../PathMonolingualTestCase.md)
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
      'name' => 'Paths on non-English monolingual sites',
      'description' => 'Confirm that paths are not changed on monolingual non-English sites',
      'group' => 'Path',
    );
  }
```

---
_Drupal 7.103 · [modules/path/path.test](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
