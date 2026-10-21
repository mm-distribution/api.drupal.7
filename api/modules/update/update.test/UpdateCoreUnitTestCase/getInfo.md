# UpdateCoreUnitTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 801–807 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L801-L807)
- **Class:** [UpdateCoreUnitTestCase](../UpdateCoreUnitTestCase.md)
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
      'name' => "Unit tests",
      'description' => 'Test update funcionality unrelated to the database.',
      'group' => 'Update',
    );
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
