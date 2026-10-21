# TriggerContentTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 44–50 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L44-L50)
- **Class:** [TriggerContentTestCase](../TriggerContentTestCase.md)
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
      'name' => 'Trigger content (node) actions',
      'description' => 'Perform various tests with content actions.',
      'group' => 'Trigger',
    );
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
