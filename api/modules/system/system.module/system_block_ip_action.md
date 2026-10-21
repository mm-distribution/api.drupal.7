# system_block_ip_action()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3402–3409 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3402-L3409)
- **Module/theme:** system
- **Topics:** [actions](../../../topics/actions.md)

## Signature

```php
function system_block_ip_action()
```

## Documentation

```text
Blocks the current user's IP address.

@ingroup actions
```

## Code

```php
function system_block_ip_action() {
  $ip = ip_address();
  db_merge('blocked_ips')
    ->key(array('ip' => $ip))
    ->fields(array('ip' => $ip))
    ->execute();
  watchdog('action', 'Banned IP address %ip', array('%ip' => $ip));
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
