# system_message_action()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3351–3358 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3351-L3358)
- **Module/theme:** system
- **Topics:** [actions](../../../topics/actions.md)

## Signature

```php
function system_message_action(&$entity, $context = array())
```

## Documentation

```text
Sends a message to the current user's screen.

@param object $entity
  An optional node object, which will be added as $context['node'] if
  provided.
@param array $context
  Array with the following elements:
  - 'message': The message to send. This will be passed through
    token_replace().
  - Other elements will be used as the data for token replacement in
    the message.

@ingroup actions
```

## Code

```php
function system_message_action(&$entity, $context = array()) {
  if (empty($context['node'])) {
    $context['node'] = $entity;
  }

  $context['message'] = token_replace(filter_xss_admin($context['message']), $context);
  drupal_set_message($context['message']);
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
