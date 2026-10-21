# SimpleTestBrowserTestCase::testCookies()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 420–442 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L420-L442)
- **Class:** [SimpleTestBrowserTestCase](../SimpleTestBrowserTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
public function testCookies()
```

## Documentation

```text
Tests that cookies set during a request are available for testing.
```

## Code

```php
  public function testCookies() {
    // Check that the $this->cookies property is populated when a user logs in.
    $user = $this->drupalCreateUser();
    $edit = array('name' => $user->name, 'pass' => $user->pass_raw);
    $this->drupalPost('<front>', $edit, t('Log in'));
    $this->assertEqual(count($this->cookies), 1, 'A cookie is set when the user logs in.');

    // Check that the name and value of the cookie match the request data.
    $cookie_header = $this->drupalGetHeader('set-cookie', TRUE);

    // The name and value are located at the start of the string, separated by
    // an equals sign and ending in a semicolon.
    preg_match('/^([^=]+)=([^;]+)/', $cookie_header, $matches);
    $name = $matches[1];
    $value = $matches[2];

    $this->assertTrue(array_key_exists($name, $this->cookies), 'The cookie name is correct.');
    $this->assertEqual($value, $this->cookies[$name]['value'], 'The cookie value is correct.');

    // Set a flag indicating that a cookie has been set in this test.
    // @see SimpleTestBrowserTestCase::testCookieDoesNotBleed().
    self::$cookieSet = TRUE;
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
