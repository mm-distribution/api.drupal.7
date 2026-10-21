# system_action_info()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3157–3184 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3157-L3184)
- **Module/theme:** system
- **Implements:** [hook_action_info()](../system.api.php/hook_action_info.md)

## Signature

```php
function system_action_info()
```

## Documentation

```text
Implements hook_action_info().
```

## Code

```php
function system_action_info() {
  return array(
    'system_message_action' => array(
      'type' => 'system',
      'label' => t('Display a message to the user'),
      'configurable' => TRUE,
      'triggers' => array('any'),
    ),
    'system_send_email_action' => array(
      'type' => 'system',
      'label' => t('Send e-mail'),
      'configurable' => TRUE,
      'triggers' => array('any'),
    ),
    'system_block_ip_action' => array(
      'type' => 'user',
      'label' => t('Ban IP address of current user'),
      'configurable' => FALSE,
      'triggers' => array('any'),
    ),
    'system_goto_action' => array(
      'type' => 'system',
      'label' => t('Redirect to URL'),
      'configurable' => TRUE,
      'triggers' => array('any'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
