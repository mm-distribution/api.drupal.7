# system_send_email_action_form()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3198–3233 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3198-L3233)
- **Module/theme:** system

## Signature

```php
function system_send_email_action_form($context)
```

## Documentation

```text
Return a form definition so the Send email action can be configured.

@param $context
  Default values (if we are editing an existing action instance).

@return
  Form definition.

@see system_send_email_action_validate()
@see system_send_email_action_submit()
```

## Code

```php
function system_send_email_action_form($context) {
  // Set default values for form.
  if (!isset($context['recipient'])) {
    $context['recipient'] = '';
  }
  if (!isset($context['subject'])) {
    $context['subject'] = '';
  }
  if (!isset($context['message'])) {
    $context['message'] = '';
  }

  $form['recipient'] = array(
    '#type' => 'textfield',
    '#title' => t('Recipient'),
    '#default_value' => $context['recipient'],
    '#maxlength' => '254',
    '#description' => t('The email address to which the message should be sent OR enter [node:author:mail], [comment:author:mail], etc. if you would like to send an e-mail to the author of the original post.'),
  );
  $form['subject'] = array(
    '#type' => 'textfield',
    '#title' => t('Subject'),
    '#default_value' => $context['subject'],
    '#maxlength' => '254',
    '#description' => t('The subject of the message.'),
  );
  $form['message'] = array(
    '#type' => 'textarea',
    '#title' => t('Message'),
    '#default_value' => $context['message'],
    '#cols' => '80',
    '#rows' => '20',
    '#description' => t('The message that should be sent. You may include placeholders like [node:title], [user:name], and [comment:body] to represent data that will be different each time message is sent. Not all placeholders will be available in all contexts.'),
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
