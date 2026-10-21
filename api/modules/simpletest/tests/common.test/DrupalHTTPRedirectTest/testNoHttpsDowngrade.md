# DrupalHTTPRedirectTest::testNoHttpsDowngrade()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1307–1311 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1307-L1311)
- **Class:** [DrupalHTTPRedirectTest](../DrupalHTTPRedirectTest.md)
- **Module/theme:** batch_test

## Signature

```php
public function testNoHttpsDowngrade()
```

## Documentation

_No docblock in source._

## Code

```php
  public function testNoHttpsDowngrade() {
    $url = 'https://example.com/foo';
    $location = 'https://example.com/bar';
    $this->assertFalse(_drupal_should_strip_sensitive_headers_on_http_redirect($url, $location), 'Sensitive headers are not stripped without HTTPS downgrade.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
