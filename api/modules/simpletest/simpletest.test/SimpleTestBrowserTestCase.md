# SimpleTestBrowserTestCase

- **Type:** Class
- **File:** [`modules/simpletest/simpletest.test`](_file.md), lines 349–456 · [local source](../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L349-L456)
- **Module/theme:** simpletest

## Signature

```php
class SimpleTestBrowserTestCase extends DrupalWebTestCase
```

## Documentation

```text
Test internal testing framework browser.
```

## Properties

### $cookieSet

```php
protected static $cookieSet = FALSE;
```

```text
A flag indicating whether a cookie has been set in a test.

@var bool
```

## Methods (derived index)

- [getInfo()](SimpleTestBrowserTestCase/getInfo.md)
- [setUp()](SimpleTestBrowserTestCase/setUp.md)
- [testGetAbsoluteUrl()](SimpleTestBrowserTestCase/testGetAbsoluteUrl.md) — Test DrupalWebTestCase::getAbsoluteUrl().
- [testXPathEscaping()](SimpleTestBrowserTestCase/testXPathEscaping.md) — Tests XPath escaping.
- [testCookies()](SimpleTestBrowserTestCase/testCookies.md) — Tests that cookies set during a request are available for testing.
- [testCookieDoesNotBleed()](SimpleTestBrowserTestCase/testCookieDoesNotBleed.md) — Tests that the cookies from a previous test do not bleed into a new test.

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
