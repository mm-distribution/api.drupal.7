# BootstrapPageCacheTestCase::testPageCacheHeaders()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 266–282 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L266-L282)
- **Class:** [BootstrapPageCacheTestCase](../BootstrapPageCacheTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testPageCacheHeaders()
```

## Documentation

```text
Test page cache headers.
```

## Code

```php
  function testPageCacheHeaders() {
    variable_set('cache', 1);
    // First request should store a response in the page cache.
    $this->drupalGet('system-test/page-cache-headers');

    // The test callback should remove the query string leaving the same path
    // as the previous request, which we'll try to retrieve from cache_page.
    $this->drupalGet('system-test/page-cache-headers', array('query' => array('return_headers' => 'TRUE')));

    $headers = json_decode($this->drupalGetHeader('Page-Cache-Headers'), TRUE);
    if (is_null($headers)) {
      $this->fail('No headers were retrieved from the page cache.');
    }
    else {
      $this->assertEqual($headers['X-Content-Type-Options'], 'nosniff', 'X-Content-Type-Options header retrieved from response in the page cache.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
