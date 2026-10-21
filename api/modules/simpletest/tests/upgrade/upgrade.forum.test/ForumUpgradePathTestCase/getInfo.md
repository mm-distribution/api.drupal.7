# ForumUpgradePathTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.forum.test`](../_file.md), lines 7–13 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.forum.test#L7-L13)
- **Class:** [ForumUpgradePathTestCase](../ForumUpgradePathTestCase.md)
- **Module/theme:** batch_test

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
      'name'  => 'Forum upgrade path',
      'description'  => 'Upgrade path tests for the Forum module.',
      'group' => 'Upgrade path',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.forum.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._
