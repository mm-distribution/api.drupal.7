# TriggerUnassignTestCase::testUnassignAccessDenied()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 766–769 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L766-L769)
- **Class:** [TriggerUnassignTestCase](../TriggerUnassignTestCase.md)
- **Module/theme:** trigger

## Signature

```php
function testUnassignAccessDenied()
```

## Documentation

```text
Tests an attempt to unassign triggers when none are assigned.
```

## Code

```php
  function testUnassignAccessDenied() {
    $this->drupalGet('admin/structure/trigger/unassign');
    $this->assertResponse(403, 'If there are no actions available, return access denied.');
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
