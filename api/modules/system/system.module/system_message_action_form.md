# system_message_action_form()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3320–3330 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3320-L3330)
- **Module/theme:** system

## Signature

```php
function system_message_action_form($context)
```

## Documentation

_No docblock in source._

## Code

```php
function system_message_action_form($context) {
  $form['message'] = array(
    '#type' => 'textarea',
    '#title' => t('Message'),
    '#default_value' => isset($context['message']) ? $context['message'] : '',
    '#required' => TRUE,
    '#rows' => '8',
    '#description' => t('The message to be displayed to the current user. You may include placeholders like [node:title], [user:name], and [comment:body] to represent data that will be different each time message is sent. Not all placeholders will be available in all contexts.'),
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
