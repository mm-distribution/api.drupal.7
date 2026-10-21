# TriggerActionTestCase::assignSystemEmailAction()

- **Type:** Method
- **File:** [`modules/trigger/trigger.test`](../_file.md), lines 357–377 · [local source](../../../../../source/modules/trigger/trigger.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test#L357-L377)
- **Class:** [TriggerActionTestCase](../TriggerActionTestCase.md)
- **Module/theme:** trigger

## Signature

```php
function assignSystemEmailAction($trigger)
```

## Documentation

```text
Assigns a system_send_email_action to the passed-in trigger.

@param $trigger
  For example, 'user_login'
```

## Code

```php
  function assignSystemEmailAction($trigger) {
    $form_name = "trigger_{$trigger}_assign_form";
    $form_html_id = strtr($form_name, '_', '-');

    $message = $this->generateMessageWithTokens($trigger);
    // Assign a configurable action 'System message' to the passed trigger.
    $action_edit = array(
      // 'actions_label' => $trigger . "_system_send_message_action_" . $this->randomName(16),
      'actions_label' => $trigger . "_system_send_email_action",
      'recipient' => '[user:mail]',
      'subject' => $message,
      'message' => $message,
    );

    // Configure an advanced action that we can assign.
    $aid = $this->configureAdvancedAction('system_send_email_action', $action_edit);

    $edit = array('aid' => drupal_hash_base64($aid));
    $this->drupalPost('admin/structure/trigger/user', $edit, t('Assign'), array(), array(), $form_html_id);
    drupal_static_reset('trigger_get_assigned_actions');
  }
```

---
_Drupal 7.103 · [modules/trigger/trigger.test](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.test) · Licensed GPL-2.0-or-later (see LICENSE)._
