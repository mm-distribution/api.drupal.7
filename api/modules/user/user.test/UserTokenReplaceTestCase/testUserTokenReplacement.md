# UserTokenReplaceTestCase::testUserTokenReplacement()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2664–2713 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2664-L2713)
- **Class:** [UserTokenReplaceTestCase](../UserTokenReplaceTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserTokenReplacement()
```

## Documentation

```text
Creates a user, then tests the tokens generated from it.
```

## Code

```php
  function testUserTokenReplacement() {
    global $language;
    $url_options = array(
      'absolute' => TRUE,
      'language' => $language,
    );

    // Create two users and log them in one after another.
    $user1 = $this->drupalCreateUser(array());
    $user2 = $this->drupalCreateUser(array());
    $this->drupalLogin($user1);
    $this->drupalLogout();
    $this->drupalLogin($user2);

    $account = user_load($user1->uid);
    $global_account = user_load($GLOBALS['user']->uid);

    // Generate and test sanitized tokens.
    $tests = array();
    $tests['[user:uid]'] = $account->uid;
    $tests['[user:name]'] = check_plain(format_username($account));
    $tests['[user:mail]'] = check_plain($account->mail);
    $tests['[user:url]'] = url("user/$account->uid", $url_options);
    $tests['[user:edit-url]'] = url("user/$account->uid/edit", $url_options);
    $tests['[user:last-login]'] = format_date($account->login, 'medium', '', NULL, $language->language);
    $tests['[user:last-login:short]'] = format_date($account->login, 'short', '', NULL, $language->language);
    $tests['[user:created]'] = format_date($account->created, 'medium', '', NULL, $language->language);
    $tests['[user:created:short]'] = format_date($account->created, 'short', '', NULL, $language->language);
    $tests['[user:changed]'] = format_date($account->changed, 'medium', '', NULL, $language->language);
    $tests['[user:changed:short]'] = format_date($account->changed, 'short', '', NULL, $language->language);
    $tests['[current-user:name]'] = check_plain(format_username($global_account));

    // Test to make sure that we generated something for each token.
    $this->assertFalse(in_array(0, array_map('strlen', $tests)), 'No empty tokens generated.');

    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array('user' => $account), array('language' => $language));
      $this->assertEqual($output, $expected, format_string('Sanitized user token %token replaced.', array('%token' => $input)));
    }

    // Generate and test unsanitized tokens.
    $tests['[user:name]'] = format_username($account);
    $tests['[user:mail]'] = $account->mail;
    $tests['[current-user:name]'] = format_username($global_account);

    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array('user' => $account), array('language' => $language, 'sanitize' => FALSE));
      $this->assertEqual($output, $expected, format_string('Unsanitized user token %token replaced.', array('%token' => $input)));
    }
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
