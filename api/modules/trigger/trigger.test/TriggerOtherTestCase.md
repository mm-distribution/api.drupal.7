# TriggerOtherTestCase

- **Type:** Class
- **File:** [`modules/trigger/trigger.test`](_file.md), lines 547–685 · [local source](../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L547-L685)
- **Module/theme:** trigger

## Signature

```php
class TriggerOtherTestCase extends TriggerWebTestCase
```

## Documentation

```text
Tests other triggers.
```

## Properties

### $_cleanup_roles

```php
var $_cleanup_roles = array();
```

### $_cleanup_users

```php
var $_cleanup_users = array();
```

## Methods (derived index)

- [getInfo()](TriggerOtherTestCase/getInfo.md)
- [setUp()](TriggerOtherTestCase/setUp.md)
- [testActionsUser()](TriggerOtherTestCase/testActionsUser.md) — Tests triggering on user create and user login.
- [testActionsComment()](TriggerOtherTestCase/testActionsComment.md) — Tests triggering on comment save.
- [testActionsTaxonomy()](TriggerOtherTestCase/testActionsTaxonomy.md) — Tests triggering on taxonomy new term.

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
