# TriggerActionTestCase::assertSystemMessageTokenReplacement()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 402–406 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L402-L406)
- **Class:** [TriggerActionTestCase](../TriggerActionTestCase.md)
- **Module/theme:** trigger

## Signature

```php
function assertSystemMessageTokenReplacement($trigger, $account)
```

## Documentation

```text
Asserts correct token replacement for the given trigger and account.

@param $trigger
  A trigger like 'user_login'.
@param $account
  The user account which triggered the action.
```

## Code

```php
  function assertSystemMessageTokenReplacement($trigger, $account) {
    $expected = $this->generateTokenExpandedComparison($trigger, $account);
    $this->assertText($expected,
      format_string('Expected system message to contain token-replaced text "@expected" found in configured system message action', array('@expected' => $expected )) );
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
