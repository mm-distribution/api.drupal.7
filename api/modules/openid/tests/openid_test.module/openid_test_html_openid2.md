# openid_test_html_openid2()

- **Type:** Function
- **File:** [`modules/openid/tests/openid_test.module`](_file.md), lines 209–213 · [local source](../../../../../source/modules/openid/tests/openid_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module#L209-L213)
- **Module/theme:** openid_test

## Signature

```php
function openid_test_html_openid2()
```

## Documentation

```text
Menu callback; regular HTML page with OpenID 2.0 <link> element.
```

## Code

```php
function openid_test_html_openid2() {
  drupal_add_html_head_link(array('rel' => 'openid2.provider', 'href' => url('openid-test/endpoint', array('absolute' => TRUE))));
  drupal_add_html_head_link(array('rel' => 'openid2.local_id', 'href' => 'http://example.com/html-openid2'));
  return t('This page includes a &lt;link rel=...&gt; element containing the URL of an OpenID Provider Endpoint.');
}
```

---
_Drupal 7.103 · [modules/openid/tests/openid_test.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
