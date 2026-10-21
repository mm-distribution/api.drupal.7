# update_get_d6_session_name()

- **Type:** Function
- **File:** [`includes/update.inc`](_file.md), lines 895–916 · [local source](../../../source/includes/update.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/update.inc#L895-L916)

## Signature

```php
function update_get_d6_session_name()
```

## Documentation

```text
Constructs a session name compatible with a D6 environment.

@return
  D6-compatible session name string.

@see drupal_settings_initialize()
```

## Code

```php
function update_get_d6_session_name() {
  global $base_url, $cookie_domain;
  $cookie_secure = ini_get('session.cookie_secure');

  // If a custom cookie domain is set in settings.php, that variable forms
  // the basis of the session name. Re-compute the D7 hashing method to find
  // out if $cookie_domain was used as the session name.
  if (($cookie_secure ? 'SSESS' : 'SESS') . substr(hash('sha256', $cookie_domain), 0, 32) == session_name()) {
    $session_name = $cookie_domain;
  }
  else {
    // Otherwise use $base_url as session name, without the protocol
    // to use the same session identifiers across HTTP and HTTPS.
    list( , $session_name) = explode('://', $base_url, 2);
  }

  if ($cookie_secure) {
    $session_name .= 'SSL';
  }

  return 'SESS' . md5($session_name);
}
```

---
_Drupal 7.103 · [includes/update.inc](https://github.com/drupal/drupal/blob/7.103/includes/update.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
