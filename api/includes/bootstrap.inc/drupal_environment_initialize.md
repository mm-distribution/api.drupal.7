# drupal_environment_initialize()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 659–727 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L659-L727)

## Signature

```php
function drupal_environment_initialize()
```

## Documentation

```text
Initializes the PHP environment.
```

## Code

```php
function drupal_environment_initialize() {
  if (!isset($_SERVER['HTTP_REFERER'])) {
    $_SERVER['HTTP_REFERER'] = '';
  }
  if (!isset($_SERVER['SERVER_PROTOCOL']) || ($_SERVER['SERVER_PROTOCOL'] != 'HTTP/1.0' && $_SERVER['SERVER_PROTOCOL'] != 'HTTP/1.1')) {
    $_SERVER['SERVER_PROTOCOL'] = 'HTTP/1.0';
  }

  if (isset($_SERVER['HTTP_HOST'])) {
    // As HTTP_HOST is user input, ensure it only contains characters allowed
    // in hostnames. See RFC 952 (and RFC 2181).
    // $_SERVER['HTTP_HOST'] is lowercased here per specifications.
    $_SERVER['HTTP_HOST'] = strtolower($_SERVER['HTTP_HOST']);
    if (!drupal_valid_http_host($_SERVER['HTTP_HOST'])) {
      // HTTP_HOST is invalid, e.g. if containing slashes it may be an attack.
      header($_SERVER['SERVER_PROTOCOL'] . ' 400 Bad Request');
      exit;
    }
  }
  else {
    // Some pre-HTTP/1.1 clients will not send a Host header. Ensure the key is
    // defined for E_ALL compliance.
    $_SERVER['HTTP_HOST'] = '';
  }

  // When clean URLs are enabled, emulate ?q=foo/bar using REQUEST_URI. It is
  // not possible to append the query string using mod_rewrite without the B
  // flag (this was added in Apache 2.2.8), because mod_rewrite unescapes the
  // path before passing it on to PHP. This is a problem when the path contains
  // e.g. "&" or "%" that have special meanings in URLs and must be encoded.
  $_GET['q'] = request_path();

  // Enforce E_ALL, but allow users to set levels not part of E_ALL.
  error_reporting(E_ALL | error_reporting());

  // Override PHP settings required for Drupal to work properly.
  // sites/default/default.settings.php contains more runtime settings.
  // The .htaccess file contains settings that cannot be changed at runtime.

  // Don't escape quotes when reading files from the database, disk, etc.
  ini_set('magic_quotes_runtime', '0');
  // Use session cookies, not transparent sessions that puts the session id in
  // the query string.
  ini_set('session.use_cookies', '1');
  ini_set('session.use_only_cookies', '1');
  ini_set('session.use_trans_sid', '0');
  // Don't send HTTP headers using PHP's session handler.
  // An empty string is used here to disable the cache limiter.
  ini_set('session.cache_limiter', '');
  // Use httponly session cookies.
  ini_set('session.cookie_httponly', '1');

  // Set sane locale settings, to ensure consistent string, dates, times and
  // numbers handling.
  setlocale(LC_ALL, 'C');

  // PHP's built-in phar:// stream wrapper is not sufficiently secure. Override
  // it with a more secure one, which requires PHP 5.3.3. For lower versions,
  // unregister the built-in one without replacing it. Sites needing phar
  // support for lower PHP versions must implement hook_stream_wrappers() to
  // register their desired implementation.
  if (in_array('phar', stream_get_wrappers(), TRUE)) {
    stream_wrapper_unregister('phar');
    if (version_compare(PHP_VERSION, '5.3.3', '>=')) {
      include_once DRUPAL_ROOT . '/includes/file.phar.inc';
      file_register_phar_wrapper();
    }
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
