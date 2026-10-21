# modules/openid/tests/openid_test.module

- **Source:** [local](../../../../../source/modules/openid/tests/openid_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module) · 369 lines
- **Module/theme:** openid_test

## File documentation

```text
@file
Dummy OpenID Provider used with SimpleTest.

The provider simply responds positively to all authentication requests. In
addition to a Provider Endpoint (a URL used for Drupal to communicate with
the provider using the OpenID Authentication protocol) the module provides
URLs used by the various discovery mechanisms.

When a user enters an OpenID identity, the Relying Party (in the testing
scenario, this is the OpenID module) looks up the URL of the Provider
Endpoint using one of several discovery mechanisms. The Relying Party then
redirects the user to Provider Endpoint. The provider verifies the user's
identity and redirects the user back to the Relying Party accompanied by a
signed message confirming the identity. Before redirecting to a provider for
the first time, the Relying Party fetches a secret MAC key from the provider
by doing a direct "associate" HTTP request to the Provider Endpoint. This
key is used for verifying the signed messages from the provider.
```

## Functions (derived index)

- [openid_test_menu()](openid_test_menu.md) — Implements hook_menu().
- [openid_test_menu_site_status_alter()](openid_test_menu_site_status_alter.md) — Implements hook_menu_site_status_alter().
- [openid_test_yadis_xrds()](openid_test_yadis_xrds.md) — Menu callback; XRDS document that references the OP Endpoint URL.
- [openid_test_yadis_x_xrds_location()](openid_test_yadis_x_xrds_location.md) — Menu callback; regular HTML page with an X-XRDS-Location HTTP header.
- [openid_test_yadis_http_equiv()](openid_test_yadis_http_equiv.md) — Menu callback; regular HTML page with <meta> element.
- [openid_test_html_openid1()](openid_test_html_openid1.md) — Menu callback; regular HTML page with OpenID 1.0 <link> element.
- [openid_test_html_openid2()](openid_test_html_openid2.md) — Menu callback; regular HTML page with OpenID 2.0 <link> element.
- [openid_test_endpoint()](openid_test_endpoint.md) — Menu callback; OpenID Provider Endpoint.
- [openid_test_redirect()](openid_test_redirect.md) — Menu callback; redirect during Normalization/Discovery.
- [openid_test_redirected_method()](openid_test_redirected_method.md) — Menu callback; respond with appropriate callback.
- [_openid_test_endpoint_associate()](_openid_test_endpoint_associate.md) — OpenID endpoint; handle "associate" requests (see OpenID Authentication 2.0, section 8).
- [_openid_test_endpoint_authenticate()](_openid_test_endpoint_authenticate.md) — OpenID endpoint; handle "authenticate" requests.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
