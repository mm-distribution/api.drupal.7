# system_ip_blocking_delete_submit()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1491–1499 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1491-L1499)
- **Module/theme:** system

## Signature

```php
function system_ip_blocking_delete_submit($form, &$form_state)
```

## Documentation

```text
Process system_ip_blocking_delete form submissions.
```

## Code

```php
function system_ip_blocking_delete_submit($form, &$form_state) {
  $blocked_ip = $form_state['values']['blocked_ip'];
  db_delete('blocked_ips')
    ->condition('iid', $blocked_ip['iid'])
    ->execute();
  watchdog('user', 'Deleted %ip', array('%ip' => $blocked_ip['ip']));
  drupal_set_message(t('The IP address %ip was deleted.', array('%ip' => $blocked_ip['ip'])));
  $form_state['redirect'] = 'admin/config/people/ip-blocking';
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
