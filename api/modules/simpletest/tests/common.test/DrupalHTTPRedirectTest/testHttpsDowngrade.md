# DrupalHTTPRedirectTest::testHttpsDowngrade()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1301–1305 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1301-L1305)
- **Class:** [DrupalHTTPRedirectTest](../DrupalHTTPRedirectTest.md)
- **Module/theme:** batch_test

## Signature

```php
public function testHttpsDowngrade()
```

## Documentation

_No docblock in source._

## Code

```php
  public function testHttpsDowngrade() {
    $url = 'https://example.com/foo';
    $location = 'http://example.com/bar';
    $this->assertTrue(_drupal_should_strip_sensitive_headers_on_http_redirect($url, $location), 'Sensitive headers are stripped on HTTPS downgrade.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
