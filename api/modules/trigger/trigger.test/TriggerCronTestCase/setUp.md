# TriggerCronTestCase::setUp()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 198–200 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L198-L200)
- **Class:** [TriggerCronTestCase](../TriggerCronTestCase.md)
- **Module/theme:** trigger

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('trigger', 'trigger_test');
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
