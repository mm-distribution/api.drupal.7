# TriggerActionTestCase::assignSystemMessageAction()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 333–348 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L333-L348)
- **Class:** [TriggerActionTestCase](../TriggerActionTestCase.md)
- **Module/theme:** trigger

## Signature

```php
function assignSystemMessageAction($trigger)
```

## Documentation

```text
Assigns a system message action to the passed-in trigger.

@param $trigger
  For example, 'user_login'
```

## Code

```php
  function assignSystemMessageAction($trigger) {
    $form_name = "trigger_{$trigger}_assign_form";
    $form_html_id = strtr($form_name, '_', '-');
    // Assign a configurable action 'System message' to the passed trigger.
    $action_edit = array(
      'actions_label' => $trigger . "_system_message_action_" . $this->randomName(16),
      'message' => $this->generateMessageWithTokens($trigger),
    );

    // Configure an advanced action that we can assign.
    $aid = $this->configureAdvancedAction('system_message_action', $action_edit);

    $edit = array('aid' => drupal_hash_base64($aid));
    $this->drupalPost('admin/structure/trigger/user', $edit, t('Assign'), array(), array(), $form_html_id);
    drupal_static_reset('trigger_get_asssigned_actions');
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
