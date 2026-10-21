# openid_test_install()

- **Type:** Function
- **File:** [`modules/openid/tests/openid_test.install`](_file.md), lines 11–17 · [local source](../../../../../source/modules/openid/tests/openid_test.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.install#L11-L17)
- **Module/theme:** openid_test
- **Implements:** [hook_install()](../../../system/system.api.php/hook_install.md)

## Signature

```php
function openid_test_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function openid_test_install() {
  module_load_include('inc', 'openid');
  // Generate a MAC key (Message Authentication Code) used for signing messages.
  // The variable is base64-encoded, because variables cannot contain non-UTF-8
  // data.
  variable_set('openid_test_mac_key', drupal_random_key(20));
}
```

---
_Drupal 7.103 · [modules/openid/tests/openid_test.install](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.install) · Licensed GPL-2.0-or-later (see LICENSE)._
