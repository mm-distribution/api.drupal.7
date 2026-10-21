# system_update_7003()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 1961–1998 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L1961-L1998)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7003()
```

## Documentation

```text
Update {blocked_ips} with valid IP addresses from {access}.
```

## Code

```php
function system_update_7003() {
  $messages = array();
  $type = 'host';
  $result = db_query("SELECT mask FROM {access} WHERE status = :status AND type = :type", array(
    ':status' => 0,
    ':type' => $type,
  ));
  foreach ($result as $blocked) {
    if (filter_var($blocked->mask, FILTER_VALIDATE_IP, FILTER_FLAG_NO_RES_RANGE) !== FALSE) {
      db_insert('blocked_ips')
        ->fields(array('ip' => $blocked->mask))
        ->execute();
    }
    else {
      $invalid_host = check_plain($blocked->mask);
      $messages[] = t('The host !host is no longer blocked because it is not a valid IP address.', array('!host' => $invalid_host ));
    }
  }
  if (isset($invalid_host)) {
    drupal_set_message('Drupal no longer supports wildcard IP address blocking. Visitors whose IP addresses match ranges you have previously set using <em>access rules</em> will no longer be blocked from your site when you put the site online. See the <a href="http://drupal.org/node/24302">IP address and referrer blocking Handbook page</a> for alternative methods.', 'warning');
  }
  // Make sure not to block any IP addresses that were specifically allowed by access rules.
  if (!empty($result)) {
    $result = db_query("SELECT mask FROM {access} WHERE status = :status AND type = :type", array(
      ':status' => 1,
      ':type' => $type,
    ));
    $or = db_condition('or');
    foreach ($result as $allowed) {
      $or->condition('ip', $allowed->mask, 'LIKE');
    }
    if (count($or)) {
      db_delete('blocked_ips')
        ->condition($or)
        ->execute();
    }
  }
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
