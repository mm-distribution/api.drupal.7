# system_ip_blocking_form_submit()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1465–1473 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1465-L1473)
- **Module/theme:** system

## Signature

```php
function system_ip_blocking_form_submit($form, &$form_state)
```

## Documentation

_No docblock in source._

## Code

```php
function system_ip_blocking_form_submit($form, &$form_state) {
  $ip = trim($form_state['values']['ip']);
  db_insert('blocked_ips')
    ->fields(array('ip' => $ip))
    ->execute();
  drupal_set_message(t('The IP address %ip has been blocked.', array('%ip' => $ip)));
  $form_state['redirect'] = 'admin/config/people/ip-blocking';
  return;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
