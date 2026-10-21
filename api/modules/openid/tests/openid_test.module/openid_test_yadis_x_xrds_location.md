# openid_test_yadis_x_xrds_location()

- **Type:** Function
- **File:** [`modules/openid/tests/openid_test.module`](_file.md), lines 177–180 · [local source](../../../../../source/modules/openid/tests/openid_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module#L177-L180)
- **Module/theme:** openid_test

## Signature

```php
function openid_test_yadis_x_xrds_location()
```

## Documentation

```text
Menu callback; regular HTML page with an X-XRDS-Location HTTP header.
```

## Code

```php
function openid_test_yadis_x_xrds_location() {
  drupal_add_http_header('X-XRDS-Location', url('openid-test/yadis/xrds', array('absolute' => TRUE)));
  return t('This page includes an X-RDS-Location HTTP header containing the URL of an XRDS document.');
}
```

---
_Drupal 7.103 · [modules/openid/tests/openid_test.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
