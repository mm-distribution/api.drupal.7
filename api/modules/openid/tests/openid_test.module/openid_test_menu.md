# openid_test_menu()

- **Type:** Function
- **File:** [`modules/openid/tests/openid_test.module`](_file.md), lines 26–77 · [local source](../../../../../source/modules/openid/tests/openid_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module#L26-L77)
- **Module/theme:** openid_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function openid_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function openid_test_menu() {
  $items['openid-test/yadis/xrds'] = array(
    'title' => 'XRDS service document',
    'page callback' => 'openid_test_yadis_xrds',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['openid-test/yadis/x-xrds-location'] = array(
    'title' => 'Yadis discovery using X-XRDS-Location header',
    'page callback' => 'openid_test_yadis_x_xrds_location',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['openid-test/yadis/http-equiv'] = array(
    'title' => 'Yadis discovery using <meta http-equiv="X-XRDS-Location" ...>',
    'page callback' => 'openid_test_yadis_http_equiv',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['openid-test/html/openid1'] = array(
    'title' => 'HTML-based discovery using <link rel="openid.server" ...>',
    'page callback' => 'openid_test_html_openid1',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['openid-test/html/openid2'] = array(
    'title' => 'HTML-based discovery using <link rel="openid2.provider" ...>',
    'page callback' => 'openid_test_html_openid2',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['openid-test/endpoint'] = array(
    'title' => 'OpenID Provider Endpoint',
    'page callback' => 'openid_test_endpoint',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['openid-test/redirect'] = array(
    'title' => 'OpenID Provider Redirection Point',
    'page callback' => 'openid_test_redirect',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['openid-test/redirected/%/%'] = array(
    'title' => 'OpenID Provider Final URL',
    'page callback' => 'openid_test_redirected_method',
    'page arguments' => array(2, 3),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/openid/tests/openid_test.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
