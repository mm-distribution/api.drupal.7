# openid_test_redirected_method()

- **Type:** Function
- **File:** [`modules/openid/tests/openid_test.module`](_file.md), lines 251–253 · [local source](../../../../../source/modules/openid/tests/openid_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module#L251-L253)
- **Module/theme:** openid_test

## Signature

```php
function openid_test_redirected_method($method1, $method2)
```

## Documentation

```text
Menu callback; respond with appropriate callback.
```

## Code

```php
function openid_test_redirected_method($method1, $method2) {
  return call_user_func('openid_test_' . $method1 . '_' . $method2);
}
```

---
_Drupal 7.103 · [modules/openid/tests/openid_test.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
