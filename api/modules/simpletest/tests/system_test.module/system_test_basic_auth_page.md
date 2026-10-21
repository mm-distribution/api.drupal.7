# system_test_basic_auth_page()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 169–188 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L169-L188)
- **Module/theme:** batch_test

## Signature

```php
function system_test_basic_auth_page()
```

## Documentation

_No docblock in source._

## Code

```php
function system_test_basic_auth_page() {
  // The Authorization HTTP header is forwarded via Drupal's .htaccess file even
  // for PHP CGI SAPIs.
  if (isset($_SERVER['HTTP_AUTHORIZATION'])) {
    $authorization_header = $_SERVER['HTTP_AUTHORIZATION'];
  }
  // If using CGI on Apache with mod_rewrite, the forwarded HTTP header appears
  // in the redirected HTTP headers. See
  // https://github.com/symfony/symfony/blob/master/src/Symfony/Component/HttpFoundation/ServerBag.php#L61
  elseif (isset($_SERVER['REDIRECT_HTTP_AUTHORIZATION'])) {
    $authorization_header = $_SERVER['REDIRECT_HTTP_AUTHORIZATION'];
  }
  // Resemble PHP_AUTH_USER and PHP_AUTH_PW for a Basic authentication from
  // the HTTP_AUTHORIZATION header. See
  // http://www.php.net/manual/features.http-auth.php
  list($user, $pw) = explode(':', base64_decode(substr($authorization_header, 6)));
  $output = t('Username is @username.', array('@username' => $user));
  $output .= t('Password is @password.', array('@password' => $pw));
  return $output;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
