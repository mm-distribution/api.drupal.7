# DrupalHTTPRedirectTest::testHostChange()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1313–1317 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1313-L1317)
- **Class:** [DrupalHTTPRedirectTest](../DrupalHTTPRedirectTest.md)
- **Module/theme:** batch_test

## Signature

```php
public function testHostChange()
```

## Documentation

_No docblock in source._

## Code

```php
  public function testHostChange() {
    $url = 'https://example.com/foo';
    $location = 'https://www.example.com/bar';
    $this->assertTrue(_drupal_should_strip_sensitive_headers_on_http_redirect($url, $location), 'Sensitive headers are stripped on change of host.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
