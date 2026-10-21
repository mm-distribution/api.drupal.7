# OpenIDWebTestCase::submitLoginForm()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 16–26 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L16-L26)
- **Class:** [OpenIDWebTestCase](../OpenIDWebTestCase.md)
- **Module/theme:** openid

## Signature

```php
function submitLoginForm($identity)
```

## Documentation

```text
Initiates the login procedure using the specified User-supplied Identity.
```

## Code

```php
  function submitLoginForm($identity) {
    // Fill out and submit the login form.
    $edit = array('openid_identifier' => $identity);
    $this->drupalPost('', $edit, t('Log in'));

    // Check we are on the OpenID redirect form.
    $this->assertTitle(t('OpenID redirect'), 'OpenID redirect page was displayed.');

    // Submit form to the OpenID Provider Endpoint.
    $this->drupalPost(NULL, array(), t('Send'));
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
