# UserTokenReplaceTestCase::testAnonymousUserTokenReplacement()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2718–2732 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2718-L2732)
- **Class:** [UserTokenReplaceTestCase](../UserTokenReplaceTestCase.md)
- **Module/theme:** user

## Signature

```php
function testAnonymousUserTokenReplacement()
```

## Documentation

```text
Uses an anonymous user, then tests the tokens generated from it.
```

## Code

```php
  function testAnonymousUserTokenReplacement() {
    global $language;

    // Load anonymous user data.
    $account = drupal_anonymous_user();

    // Generate and test sanitized tokens.
    $tests = array();
    $tests['[user:mail]'] = '';

    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array('user' => $account), array('language' => $language));
      $this->assertEqual($output, $expected, format_string('Sanitized user token %token replaced.', array('%token' => $input)));
    }
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
