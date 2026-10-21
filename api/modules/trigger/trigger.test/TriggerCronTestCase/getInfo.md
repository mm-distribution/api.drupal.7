# TriggerCronTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 190–196 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L190-L196)
- **Class:** [TriggerCronTestCase](../TriggerCronTestCase.md)
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
      'name' => 'Trigger cron (system) actions',
      'description' => 'Perform various tests with cron trigger.',
      'group' => 'Trigger',
    );
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
