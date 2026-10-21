# TriggerActionTestCase::generateMessageWithTokens()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 270–275 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L270-L275)
- **Class:** [TriggerActionTestCase](../TriggerActionTestCase.md)
- **Module/theme:** trigger

## Signature

```php
function generateMessageWithTokens($trigger)
```

## Documentation

```text
Creates a message with tokens.

@param $trigger

@return
  A message with embedded tokens.
```

## Code

```php
  function generateMessageWithTokens($trigger) {
    // Note that subject is limited to 254 characters in action configuration.
    $message = t('Action was triggered by trigger @trigger user:name=[user:name] user:uid=[user:uid] user:mail=[user:mail] user:url=[user:url] user:edit-url=[user:edit-url] user:created=[user:created]',
      array('@trigger' => $trigger));
    return trim($message);
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
