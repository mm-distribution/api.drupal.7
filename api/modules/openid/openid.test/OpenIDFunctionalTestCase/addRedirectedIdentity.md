# OpenIDFunctionalTestCase::addRedirectedIdentity()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 333–346 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L333-L346)
- **Class:** [OpenIDFunctionalTestCase](../OpenIDFunctionalTestCase.md)
- **Module/theme:** openid

## Signature

```php
function addRedirectedIdentity($identity, $version = 2, $local_id = 'http://example.com/xrds', $claimed_id = NULL, $redirects = 0)
```

## Documentation

```text
Add OpenID identity, changed by the following redirects, to user's profile.

According to OpenID Authentication 2.0, section 7.2.4, URL Identifiers MUST
be further normalized by following redirects when retrieving their content
and this final URL MUST be noted by the Relying Party as the Claimed
Identifier and be used when requesting authentication.

@param $identity
  The User-supplied Identifier.
@param $version
  The protocol version used by the service.
@param $local_id
  The expected OP-Local Identifier found during discovery.
@param $claimed_id
  The expected Claimed Identifier returned by the OpenID Provider, or FALSE
  if the discovery is expected to fail.
@param $redirects
  The number of redirects.
```

## Code

```php
  function addRedirectedIdentity($identity, $version = 2, $local_id = 'http://example.com/xrds', $claimed_id = NULL, $redirects = 0) {
    // Set the final destination URL which is the same as the Claimed
    // Identifier, we insert the same identifier also to the provider response,
    // but provider could further change the Claimed ID actually (e.g. it could
    // add unique fragment).
    variable_set('openid_test_redirect_url', $identity);
    variable_set('openid_test_response', array('openid.claimed_id' => $identity));

    $this->addIdentity(url('openid-test/redirect/' . $redirects, array('absolute' => TRUE)), $version, $local_id, $claimed_id);

    // Clean up.
    variable_del('openid_test_redirect_url');
    variable_del('openid_test_response');
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
