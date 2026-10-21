# system_send_email_action()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3280–3305 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3280-L3305)
- **Module/theme:** system
- **Topics:** [actions](../../../topics/actions.md)

## Signature

```php
function system_send_email_action($entity, $context)
```

## Documentation

```text
Sends an e-mail message.

@param object $entity
  An optional node object, which will be added as $context['node'] if
  provided.
@param array $context
  Array with the following elements:
  - 'recipient': E-mail message recipient. This will be passed through
    token_replace().
  - 'subject': The subject of the message. This will be passed through
    token_replace().
  - 'message': The message to send. This will be passed through
    token_replace().
  - Other elements will be used as the data for token replacement.

@ingroup actions
```

## Code

```php
function system_send_email_action($entity, $context) {
  if (empty($context['node'])) {
    $context['node'] = $entity;
  }

  $recipient = token_replace($context['recipient'], $context);

  // If the recipient is a registered user with a language preference, use
  // the recipient's preferred language. Otherwise, use the system default
  // language.
  $recipient_account = user_load_by_mail($recipient);
  if ($recipient_account) {
    $language = user_preferred_language($recipient_account);
  }
  else {
    $language = language_default();
  }
  $params = array('context' => $context);

  if (drupal_mail('system', 'action_send_email', $recipient, $language, $params)) {
    watchdog('action', 'Sent email to %recipient', array('%recipient' => $recipient));
  }
  else {
    watchdog('error', 'Unable to send email to %recipient', array('%recipient' => $recipient));
  }
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
