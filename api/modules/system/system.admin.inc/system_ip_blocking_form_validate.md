# system_ip_blocking_form_validate()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1452–1463 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1452-L1463)
- **Module/theme:** system

## Signature

```php
function system_ip_blocking_form_validate($form, &$form_state)
```

## Documentation

_No docblock in source._

## Code

```php
function system_ip_blocking_form_validate($form, &$form_state) {
  $ip = trim($form_state['values']['ip']);
  if (db_query("SELECT * FROM {blocked_ips} WHERE ip = :ip", array(':ip' => $ip))->fetchField()) {
    form_set_error('ip', t('This IP address is already blocked.'));
  }
  elseif ($ip == ip_address()) {
    form_set_error('ip', t('You may not block your own IP address.'));
  }
  elseif (filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_RES_RANGE) == FALSE) {
    form_set_error('ip', t('Enter a valid IP address.'));
  }
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
