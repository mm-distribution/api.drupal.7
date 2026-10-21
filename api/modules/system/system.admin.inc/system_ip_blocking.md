# system_ip_blocking()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1403–1424 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1403-L1424)
- **Module/theme:** system

## Signature

```php
function system_ip_blocking($default_ip = '')
```

## Documentation

```text
Menu callback. Display blocked IP addresses.

@param $default_ip
  Optional IP address to be passed on to drupal_get_form() for
  use as the default value of the IP address form field.
```

## Code

```php
function system_ip_blocking($default_ip = '') {
  $rows = array();
  $header = array(t('Blocked IP addresses'), t('Operations'));
  $result = db_query('SELECT * FROM {blocked_ips}');
  foreach ($result as $ip) {
    $rows[] = array(
      $ip->ip,
      l(t('delete'), "admin/config/people/ip-blocking/delete/$ip->iid"),
    );
  }

  $build['system_ip_blocking_form'] = drupal_get_form('system_ip_blocking_form', $default_ip);

  $build['system_ip_blocking_table'] = array(
    '#theme' => 'table',
    '#header' => $header,
    '#rows' => $rows,
    '#empty' => t('No blocked IP addresses available.'),
  );

  return $build;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
