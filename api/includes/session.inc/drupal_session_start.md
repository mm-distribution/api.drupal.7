# drupal_session_start()

- **Type:** Function
- **File:** [`includes/session.inc`](_file.md), lines 284–312 · [local source](../../../source/includes/session.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/session.inc#L284-L312)
- **Topics:** [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_session_start()
```

## Documentation

```text
Starts a session forcefully, preserving already set session data.

@ingroup php_wrappers
```

## Code

```php
function drupal_session_start() {
  // Command line clients do not support cookies nor sessions.
  if (!drupal_session_started() && !drupal_is_cli()) {
    // Save current session data before starting it, as PHP will destroy it.
    $session_data = isset($_SESSION) ? $_SESSION : NULL;

    // Apply any overrides to the session cookie params.
    $params = $original_params = session_get_cookie_params();
    // PHP settings for samesite will be handled by _drupal_cookie_params().
    unset($params['samesite']);
    $params = _drupal_cookie_params($params);
    if ($params !== $original_params) {
      if (\PHP_VERSION_ID >= 70300) {
        session_set_cookie_params($params);
      }
      else {
        session_set_cookie_params($params['lifetime'], $params['path'], $params['domain'], $params['secure'], $params['httponly']);
      }
    }

    session_start();
    drupal_session_started(TRUE);

    // Restore session data.
    if (!empty($session_data)) {
      $_SESSION += $session_data;
    }
  }
}
```

---
_Drupal 7.103 · [includes/session.inc](https://github.com/drupal/drupal/blob/7.103/includes/session.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
