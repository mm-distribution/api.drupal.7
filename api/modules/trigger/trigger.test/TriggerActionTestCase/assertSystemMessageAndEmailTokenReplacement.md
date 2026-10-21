# TriggerActionTestCase::assertSystemMessageAndEmailTokenReplacement()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 389–392 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L389-L392)
- **Class:** [TriggerActionTestCase](../TriggerActionTestCase.md)
- **Module/theme:** trigger

## Signature

```php
function assertSystemMessageAndEmailTokenReplacement($trigger, $account, $email_depth = 1)
```

## Documentation

```text
Asserts correct token replacement in both system message and email.

@param $trigger
  A trigger like 'user_login'.
@param $account
  The user account which triggered the action.
@param $email_depth
  Number of emails to scan, starting with most recent.
```

## Code

```php
  function assertSystemMessageAndEmailTokenReplacement($trigger, $account, $email_depth = 1) {
    $this->assertSystemMessageTokenReplacement($trigger, $account);
    $this->assertSystemEmailTokenReplacement($trigger, $account, $email_depth);
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
