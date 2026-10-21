# UpdateCoreTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 65–71 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L65-L71)
- **Class:** [UpdateCoreTestCase](../UpdateCoreTestCase.md)
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
      'name' => 'Update core functionality',
      'description' => 'Tests the Update Manager module through a series of functional tests using mock XML data.',
      'group' => 'Update',
    );
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
