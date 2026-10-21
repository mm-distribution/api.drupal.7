# DrupalHTTPRedirectTest::testNoHostChange()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1319–1323 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1319-L1323)
- **Class:** [DrupalHTTPRedirectTest](../DrupalHTTPRedirectTest.md)
- **Module/theme:** batch_test

## Signature

```php
public function testNoHostChange()
```

## Documentation

_No docblock in source._

## Code

```php
  public function testNoHostChange() {
    $url = 'http://example.com/foo';
    $location = 'http://example.com/bar';
    $this->assertFalse(_drupal_should_strip_sensitive_headers_on_http_redirect($url, $location), 'Sensitive headers are not stripped without change of host.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
