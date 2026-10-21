# SessionHttpsTestCase::testEmptySessionId()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 742–789 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L742-L789)
- **Class:** [SessionHttpsTestCase](../SessionHttpsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testEmptySessionId()
```

## Documentation

```text
Tests that empty session IDs do not cause unrelated sessions to load.
```

## Code

```php
  public function testEmptySessionId() {
    global $is_https;

    if ($is_https) {
      $secure_session_name = session_name();
    }
    else {
      $secure_session_name = 'S' . session_name();
    }

    // Enable mixed mode for HTTP and HTTPS.
    variable_set('https', TRUE);

    $admin_user = $this->drupalCreateUser(array('access administration pages'));
    $standard_user = $this->drupalCreateUser(array('access content'));

    // First log in as the admin user on HTTP.
    // We cannot use $this->drupalLogin() here because we need to use the
    // special http.php URLs.
    $edit = array(
      'name' => $admin_user->name,
      'pass' => $admin_user->pass_raw
    );
    $this->drupalGet('user');
    $form = $this->xpath('//form[@id="user-login"]');
    $form[0]['action'] = $this->httpUrl('user');
    $this->drupalPost(NULL, $edit, t('Log in'));

    $this->curlClose();

    // Now start a session for the standard user on HTTPS.
    $edit = array(
      'name' => $standard_user->name,
      'pass' => $standard_user->pass_raw
    );
    $this->drupalGet('user');
    $form = $this->xpath('//form[@id="user-login"]');
    $form[0]['action'] = $this->httpsUrl('user');
    $this->drupalPost(NULL, $edit, t('Log in'));

    // Make the secure session cookie blank. Closing the curl handler will stop
    // the previous session ID from persisting.
    $this->curlClose();
    $this->additionalCurlOptions[CURLOPT_COOKIE] = rawurlencode($secure_session_name) . '=;';
    $this->drupalGet($this->httpsUrl('user'));
    $this->assertNoText($admin_user->name, 'User is not logged in as admin');
    $this->assertNoText($standard_user->name, "The user's own name is not displayed because the invalid session cookie has logged them out.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
