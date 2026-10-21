# openid_test_redirect()

- **Type:** Function
- **File:** [`modules/openid/tests/openid_test.module`](_file.md), lines 236–246 · [local source](../../../../../source/modules/openid/tests/openid_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module#L236-L246)
- **Module/theme:** openid_test

## Signature

```php
function openid_test_redirect($count = 0)
```

## Documentation

```text
Menu callback; redirect during Normalization/Discovery.
```

## Code

```php
function openid_test_redirect($count = 0) {
  if ($count == 0) {
    $url = variable_get('openid_test_redirect_url', '');
  }
  else {
    $url = url('openid-test/redirect/' . --$count, array('absolute' => TRUE));
  }
  $http_response_code = variable_get('openid_test_redirect_http_reponse_code', 301);
  header('Location: ' . $url, TRUE, $http_response_code);
  exit();
}
```

---
_Drupal 7.103 · [modules/openid/tests/openid_test.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
