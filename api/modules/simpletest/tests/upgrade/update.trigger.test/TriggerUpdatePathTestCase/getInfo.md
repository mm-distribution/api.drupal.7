# TriggerUpdatePathTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/update.trigger.test`](../_file.md), lines 11–17 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/update.trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.trigger.test#L11-L17)
- **Class:** [TriggerUpdatePathTestCase](../TriggerUpdatePathTestCase.md)
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
      'name'  => 'Trigger update path',
      'description'  => 'Trigger update path tests.',
      'group' => 'Upgrade path',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/update.trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
