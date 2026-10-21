# TriggerOrphanedActionsTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 692–698 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L692-L698)
- **Class:** [TriggerOrphanedActionsTestCase](../TriggerOrphanedActionsTestCase.md)
- **Module/theme:** trigger

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
      'name' => 'Trigger orphaned actions',
      'description' => 'Test triggering an action that has since been removed.',
      'group' => 'Trigger',
    );
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
