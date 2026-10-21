# drupal_is_denied()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2245–2264 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2245-L2264)

## Signature

```php
function drupal_is_denied($ip)
```

## Documentation

```text
Checks to see if an IP address has been blocked.

Blocked IP addresses are stored in the database by default. However for
performance reasons we allow an override in settings.php. This allows us
to avoid querying the database at this critical stage of the bootstrap if
an administrative interface for IP address blocking is not required.

@param $ip
  IP address to check.

@return bool
  TRUE if access is denied, FALSE if access is allowed.
```

## Code

```php
function drupal_is_denied($ip) {
  // Because this function is called on every page request, we first check
  // for an array of IP addresses in settings.php before querying the
  // database.
  $blocked_ips = variable_get('blocked_ips');
  $denied = FALSE;
  if (isset($blocked_ips) && is_array($blocked_ips)) {
    $denied = in_array($ip, $blocked_ips);
  }
  // Only check if database.inc is loaded already. If
  // $conf['page_cache_without_database'] = TRUE; is set in settings.php,
  // then the database won't be loaded here so the IPs in the database
  // won't be denied. However the user asked explicitly not to use the
  // database and also in this case it's quite likely that the user relies
  // on higher performance solutions like a firewall.
  elseif (class_exists('Database', FALSE)) {
    $denied = (bool)db_query("SELECT 1 FROM {blocked_ips} WHERE ip = :ip", array(':ip' => $ip))->fetchField();
  }
  return $denied;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
