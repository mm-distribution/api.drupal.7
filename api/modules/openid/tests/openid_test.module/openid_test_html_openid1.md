# openid_test_html_openid1()

- **Type:** Function
- **File:** [`modules/openid/tests/openid_test.module`](_file.md), lines 200–204 · [local source](../../../../../source/modules/openid/tests/openid_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module#L200-L204)
- **Module/theme:** openid_test

## Signature

```php
function openid_test_html_openid1()
```

## Documentation

```text
Menu callback; regular HTML page with OpenID 1.0 <link> element.
```

## Code

```php
function openid_test_html_openid1() {
  drupal_add_html_head_link(array('rel' => 'openid.server', 'href' => url('openid-test/endpoint', array('absolute' => TRUE))));
  drupal_add_html_head_link(array('rel' => 'openid.delegate', 'href' => 'http://example.com/html-openid1'));
  return t('This page includes a &lt;link rel=...&gt; element containing the URL of an OpenID Provider Endpoint.');
}
```

---
_Drupal 7.103 · [modules/openid/tests/openid_test.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
