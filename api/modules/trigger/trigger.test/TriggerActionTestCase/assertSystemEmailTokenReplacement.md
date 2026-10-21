# TriggerActionTestCase::assertSystemEmailTokenReplacement()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 419–425 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L419-L425)
- **Class:** [TriggerActionTestCase](../TriggerActionTestCase.md)
- **Module/theme:** trigger

## Signature

```php
function assertSystemEmailTokenReplacement($trigger, $account, $email_depth = 1)
```

## Documentation

```text
Asserts correct token replacement for the given trigger and account.

@param $trigger
  A trigger like 'user_login'.
@param $account
  The user account which triggered the action.
@param $email_depth
  Number of emails to scan, starting with most recent.
```

## Code

```php
  function assertSystemEmailTokenReplacement($trigger, $account, $email_depth = 1) {
    $this->verboseEmail($email_depth);
    $expected = $this->generateTokenExpandedComparison($trigger, $account);
    $this->assertMailString('subject', $expected, $email_depth);
    $this->assertMailString('body', $expected, $email_depth);
    $this->assertMail('to', $account->mail, 'Mail sent to correct destination');
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
