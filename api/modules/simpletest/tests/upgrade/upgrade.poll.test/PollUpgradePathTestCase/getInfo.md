# PollUpgradePathTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.poll.test`](../_file.md), lines 13–19 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.poll.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.poll.test#L13-L19)
- **Class:** [PollUpgradePathTestCase](../PollUpgradePathTestCase.md)
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
      'name'  => 'Poll upgrade path',
      'description'  => 'Poll upgrade path tests.',
      'group' => 'Upgrade path',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.poll.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.poll.test) · Licensed GPL-2.0-or-later (see LICENSE)._
