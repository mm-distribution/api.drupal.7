# openid_test_yadis_http_equiv()

- **Type:** Function
- **File:** [`modules/openid/tests/openid_test.module`](_file.md), lines 185–195 · [local source](../../../../../source/modules/openid/tests/openid_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module#L185-L195)
- **Module/theme:** openid_test

## Signature

```php
function openid_test_yadis_http_equiv()
```

## Documentation

```text
Menu callback; regular HTML page with <meta> element.
```

## Code

```php
function openid_test_yadis_http_equiv() {
  $element = array(
    '#tag' => 'meta',
    '#attributes' => array(
      'http-equiv' => 'X-XRDS-Location',
      'content' => url('openid-test/yadis/xrds', array('absolute' => TRUE)),
    ),
  );
  drupal_add_html_head($element, 'openid_test_yadis_http_equiv');
  return t('This page includes a &lt;meta equiv=...&gt; element containing the URL of an XRDS document.');
}
```

---
_Drupal 7.103 · [modules/openid/tests/openid_test.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
