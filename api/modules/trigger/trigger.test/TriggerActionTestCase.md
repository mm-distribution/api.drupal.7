# TriggerActionTestCase

- **Type:** Class
- **File:** [`modules/trigger/trigger.test`](_file.md), lines 256–426 · [local source](../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L256-L426)
- **Module/theme:** trigger

## Signature

```php
class TriggerActionTestCase extends TriggerWebTestCase
```

## Documentation

```text
Provides a base class with trigger assignments and test comparisons.
```

## Methods (derived index)

- [setUp()](TriggerActionTestCase/setUp.md)
- [generateMessageWithTokens()](TriggerActionTestCase/generateMessageWithTokens.md) — Creates a message with tokens.
- [generateTokenExpandedComparison()](TriggerActionTestCase/generateTokenExpandedComparison.md) — Generates a comparison message to match the pre-token-replaced message.
- [assignSimpleAction()](TriggerActionTestCase/assignSimpleAction.md) — Assigns a simple (non-configurable) action to a trigger.
- [assignSystemMessageAction()](TriggerActionTestCase/assignSystemMessageAction.md) — Assigns a system message action to the passed-in trigger.
- [assignSystemEmailAction()](TriggerActionTestCase/assignSystemEmailAction.md) — Assigns a system_send_email_action to the passed-in trigger.
- [assertSystemMessageAndEmailTokenReplacement()](TriggerActionTestCase/assertSystemMessageAndEmailTokenReplacement.md) — Asserts correct token replacement in both system message and email.
- [assertSystemMessageTokenReplacement()](TriggerActionTestCase/assertSystemMessageTokenReplacement.md) — Asserts correct token replacement for the given trigger and account.
- [assertSystemEmailTokenReplacement()](TriggerActionTestCase/assertSystemEmailTokenReplacement.md) — Asserts correct token replacement for the given trigger and account.

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
