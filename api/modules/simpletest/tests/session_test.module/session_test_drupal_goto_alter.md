# session_test_drupal_goto_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/session_test.module`](_file.md), lines 190–198 · [local source](../../../../../source/modules/simpletest/tests/session_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module#L190-L198)
- **Module/theme:** batch_test
- **Implements:** [hook_drupal_goto_alter()](../../../system/system.api.php/hook_drupal_goto_alter.md)

## Signature

```php
function session_test_drupal_goto_alter(&$path, &$options, &$http_response_code)
```

## Documentation

```text
Implements hook_drupal_goto_alter().

Force the redirection to go to a non-secure page after being on a secure
page through https.php.
```

## Code

```php
function session_test_drupal_goto_alter(&$path, &$options, &$http_response_code) {
  global $base_insecure_url, $is_https_mock;
  // Alter the redirect to use HTTP when using a mock HTTPS request through
  // https.php because form submissions would otherwise redirect to a
  // non-existent HTTPS site.
  if (!empty($is_https_mock)) {
    $path = $base_insecure_url . '/' . $path;
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/session_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
