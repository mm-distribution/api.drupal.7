# TriggerUnassignTestCase::setUp()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 757–761 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L757-L761)
- **Class:** [TriggerUnassignTestCase](../TriggerUnassignTestCase.md)
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
    $web_user = $this->drupalCreateUser(array('administer actions'));
    $this->drupalLogin($web_user);
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
