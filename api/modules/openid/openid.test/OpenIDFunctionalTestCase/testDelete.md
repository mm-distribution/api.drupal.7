# OpenIDFunctionalTestCase::testDelete()

- **Type:** Method
- **File:** [`modules/openid/openid.test`](../_file.md), lines 229–243 · [local source](../../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L229-L243)
- **Class:** [OpenIDFunctionalTestCase](../OpenIDFunctionalTestCase.md)
- **Module/theme:** openid

## Signature

```php
function testDelete()
```

## Documentation

```text
Test deleting an OpenID identity from a user's profile.
```

## Code

```php
  function testDelete() {
    $this->drupalLogin($this->web_user);

    // Add identity to user's profile.
    $identity = url('openid-test/yadis/xrds', array('absolute' => TRUE));
    $this->addIdentity($identity);
    $this->assertText($identity, 'Identity appears in list.');

    // Delete the newly added identity.
    $this->clickLink(t('Delete'));
    $this->drupalPost(NULL, array(), t('Confirm'));

    $this->assertText(t('OpenID deleted.'), 'Identity deleted');
    $this->assertNoText($identity, 'Identity no longer appears in list.');
  }
```

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
