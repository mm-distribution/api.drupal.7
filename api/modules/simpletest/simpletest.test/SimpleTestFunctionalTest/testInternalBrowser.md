# SimpleTestFunctionalTest::testInternalBrowser()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 64–99 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L64-L99)
- **Class:** [SimpleTestFunctionalTest](../SimpleTestFunctionalTest.md)
- **Module/theme:** simpletest

## Signature

```php
function testInternalBrowser()
```

## Documentation

```text
Test the internal browsers functionality.
```

## Code

```php
  function testInternalBrowser() {
    global $conf;
    if (!$this->inCURL()) {
      $this->drupalGet('node');
      $this->assertTrue($this->drupalGetHeader('Date'), 'An HTTP header was received.');
      $this->assertTitle(t('Welcome to @site-name | @site-name', array('@site-name' => variable_get('site_name', 'Drupal'))), 'Site title matches.');
      $this->assertNoTitle('Foo', 'Site title does not match.');
      // Make sure that we are locked out of the installer when prefixing
      // using the user-agent header. This is an important security check.
      global $base_url;

      $this->drupalGet($base_url . '/install.php', array('external' => TRUE));
      $this->assertResponse(403, 'Cannot access install.php with a "simpletest" user-agent header.');

      $user = $this->drupalCreateUser();
      $this->drupalLogin($user);
      $headers = $this->drupalGetHeaders(TRUE);
      $this->assertEqual(count($headers), 2, 'There was one intermediate request.');
      $this->assertTrue(strpos($headers[0][':status'], '302') !== FALSE, 'Intermediate response code was 302.');
      $this->assertFalse(empty($headers[0]['location']), 'Intermediate request contained a Location header.');
      $this->assertEqual($this->getUrl(), $headers[0]['location'], 'HTTP redirect was followed');
      $this->assertFalse($this->drupalGetHeader('Location'), 'Headers from intermediate request were reset.');
      $this->assertResponse(200, 'Response code from intermediate request was reset.');

      // Test the maximum redirection option.
      $this->drupalLogout();
      $edit = array(
        'name' => $user->name,
        'pass' => $user->pass_raw
      );
      variable_set('simpletest_maximum_redirects', 1);
      $this->drupalPost('user?destination=user/logout', $edit, t('Log in'));
      $headers = $this->drupalGetHeaders(TRUE);
      $this->assertEqual(count($headers), 2, 'Simpletest stopped following redirects after the first one.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
