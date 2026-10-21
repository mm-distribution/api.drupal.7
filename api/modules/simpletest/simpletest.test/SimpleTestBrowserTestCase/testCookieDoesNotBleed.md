# SimpleTestBrowserTestCase::testCookieDoesNotBleed()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 449–454 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L449-L454)
- **Class:** [SimpleTestBrowserTestCase](../SimpleTestBrowserTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
public function testCookieDoesNotBleed()
```

## Documentation

```text
Tests that the cookies from a previous test do not bleed into a new test.

@see SimpleTestBrowserTestCase::testCookies().
```

## Code

```php
  public function testCookieDoesNotBleed() {
    // In order for this test to be effective it should always run after the
    // testCookies() test.
    $this->assertTrue(self::$cookieSet, 'Tests have been executed in the expected order.');
    $this->assertEqual(count($this->cookies), 0, 'No cookies are present at the start of a new test.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
