# CommentUpgradePathTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.comment.test`](../_file.md), lines 7–13 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.comment.test#L7-L13)
- **Class:** [CommentUpgradePathTestCase](../CommentUpgradePathTestCase.md)
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
      'name'  => 'Comment upgrade path',
      'description'  => 'Comment upgrade path tests.',
      'group' => 'Upgrade path',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.comment.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
