# OpenIDFunctionalTestCase::testDiscovery()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 63–149 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L63-L149)
- **Class:** [OpenIDFunctionalTestCase](../OpenIDFunctionalTestCase.md)
- **Module/theme:** openid

## Signature

```php
function testDiscovery()
```

## Documentation

```text
Test discovery of OpenID Provider Endpoint via Yadis and HTML.
```

## Code

```php
  function testDiscovery() {
    $this->drupalLogin($this->web_user);

    // The User-supplied Identifier entered by the user may indicate the URL of
    // the OpenID Provider Endpoint in various ways, as described in OpenID
    // Authentication 2.0 and Yadis Specification 1.0.
    // Note that all of the tested identifiers refer to the same endpoint, so
    // only the first will trigger an associate request in openid_association()
    // (association is only done the first time Drupal encounters a given
    // endpoint).


    // Yadis discovery (see Yadis Specification 1.0, section 6.2.5):
    // If the User-supplied Identifier is a URL, it may be a direct or indirect
    // reference to an XRDS document (a Yadis Resource Descriptor) that contains
    // the URL of the OpenID Provider Endpoint.

    // Identifier is the URL of an XRDS document.
    // On HTTP test environments, the URL scheme is stripped in order to test
    // that the supplied identifier is normalized in openid_begin().
    $identity = url('openid-test/yadis/xrds', array('absolute' => TRUE));
    $this->addIdentity(preg_replace('@^http://@', '', $identity), 2, 'http://example.com/xrds', $identity);

    $identity = url('openid-test/yadis/xrds/delegate', array('absolute' => TRUE));
    $this->addIdentity(preg_replace('@^http://@', '', $identity), 2, 'http://example.com/xrds-delegate', $identity);

    // Identifier is the URL of an XRDS document containing an OP Identifier
    // Element. The Relying Party sends the special value
    // "http://specs.openid.net/auth/2.0/identifier_select" as Claimed
    // Identifier. The OpenID Provider responds with the actual identifier
    // including the fragment.
    $identity = url('openid-test/yadis/xrds/dummy-user', array('absolute' => TRUE, 'fragment' => $this->randomName()));
    // Tell openid_test.module to respond with this identifier. If the fragment
    // part is present in the identifier, it should be retained.
    variable_set('openid_test_response', array('openid.claimed_id' => $identity, 'openid.identity' => openid_normalize($identity)));
    $this->addIdentity(url('openid-test/yadis/xrds/server', array('absolute' => TRUE)), 2, 'http://specs.openid.net/auth/2.0/identifier_select', $identity);
    variable_set('openid_test_response', array());

    // Identifier is the URL of an HTML page that is sent with an HTTP header
    // that contains the URL of an XRDS document.
    $this->addIdentity(url('openid-test/yadis/x-xrds-location', array('absolute' => TRUE)), 2);

    // Identifier is the URL of an HTML page containing a <meta http-equiv=...>
    // element that contains the URL of an XRDS document.
    $this->addIdentity(url('openid-test/yadis/http-equiv', array('absolute' => TRUE)), 2);

    // Identifier is an XRI. Resolve using our own dummy proxy resolver.
    variable_set('xri_proxy_resolver', url('openid-test/yadis/xrds/xri', array('absolute' => TRUE)) . '/');
    $this->addIdentity('@example*résumé;%25', 2, 'http://example.com/xrds', 'http://example.com/user');

    // Make sure that unverified CanonicalID are not trusted.
    variable_set('openid_test_canonical_id_status', 'bad value');
    $this->addIdentity('@example*résumé;%25', 2, FALSE, FALSE);

    // HTML-based discovery:
    // If the User-supplied Identifier is a URL of an HTML page, the page may
    // contain a <link rel=...> element containing the URL of the OpenID
    // Provider Endpoint. OpenID 1 and 2 describe slightly different formats.

    // OpenID Authentication 1.1, section 3.1:
    $this->addIdentity(url('openid-test/html/openid1', array('absolute' => TRUE)), 1, 'http://example.com/html-openid1');

    // OpenID Authentication 2.0, section 7.3.3:
    $this->addIdentity(url('openid-test/html/openid2', array('absolute' => TRUE)), 2, 'http://example.com/html-openid2');

    // OpenID Authentication 2.0, section 7.2.4:
    // URL Identifiers MUST then be further normalized by both (1) following
    // redirects when retrieving their content and finally (2) applying the
    // rules in Section 6 of RFC3986 to the final destination URL. This final
    // URL MUST be noted by the Relying Party as the Claimed Identifier and be
    // used when requesting authentication.

    // Single redirect.
    $identity = $expected_claimed_id = url('openid-test/redirected/yadis/xrds/1', array('absolute' => TRUE));
    $this->addRedirectedIdentity($identity, 2, 'http://example.com/xrds', $expected_claimed_id, 0);

    // Exact 3 redirects (default value for the 'max_redirects' option in
    // drupal_http_request()).
    $identity = $expected_claimed_id = url('openid-test/redirected/yadis/xrds/2', array('absolute' => TRUE));
    $this->addRedirectedIdentity($identity, 2, 'http://example.com/xrds', $expected_claimed_id, 2);

    // Fails because there are more than 3 redirects (default value for the
    // 'max_redirects' option in drupal_http_request()).
    $identity = url('openid-test/redirected/yadis/xrds/3', array('absolute' => TRUE));
    $expected_claimed_id = FALSE;
    $this->addRedirectedIdentity($identity, 2, 'http://example.com/xrds', $expected_claimed_id, 3);
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
