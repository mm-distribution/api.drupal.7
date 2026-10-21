# TriggerOtherTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 551–557 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L551-L557)
- **Class:** [TriggerOtherTestCase](../TriggerOtherTestCase.md)
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
      'name' => 'Trigger other actions',
      'description' => 'Test triggering of user, comment, taxonomy actions.',
      'group' => 'Trigger',
    );
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
