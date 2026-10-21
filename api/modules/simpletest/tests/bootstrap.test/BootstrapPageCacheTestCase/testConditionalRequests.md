# BootstrapPageCacheTestCase::testConditionalRequests()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 139–174 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L139-L174)
- **Class:** [BootstrapPageCacheTestCase](../BootstrapPageCacheTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testConditionalRequests()
```

## Documentation

```text
Test support for requests containing If-Modified-Since and If-None-Match headers.
```

## Code

```php
  function testConditionalRequests() {
    variable_set('cache', 1);

    // Fill the cache.
    $this->drupalGet('');

    $this->drupalHead('');
    $this->assertEqual($this->drupalGetHeader('X-Drupal-Cache'), 'HIT', 'Page was cached.');
    $etag = $this->drupalGetHeader('ETag');
    $last_modified = $this->drupalGetHeader('Last-Modified');

    $this->drupalGet('', array(), array('If-Modified-Since: ' . $last_modified, 'If-None-Match: ' . $etag));
    $this->assertResponse(304, 'Conditional request returned 304 Not Modified.');

    $this->drupalGet('', array(), array('If-Modified-Since: ' . gmdate(DATE_RFC822, strtotime($last_modified)), 'If-None-Match: ' . $etag));
    $this->assertResponse(304, 'Conditional request with obsolete If-Modified-Since date returned 304 Not Modified.');

    $this->drupalGet('', array(), array('If-Modified-Since: ' . gmdate(DATE_RFC850, strtotime($last_modified)), 'If-None-Match: ' . $etag));
    $this->assertResponse(304, 'Conditional request with obsolete If-Modified-Since date returned 304 Not Modified.');

    $this->drupalGet('', array(), array('If-Modified-Since: ' . $last_modified));
    $this->assertResponse(200, 'Conditional request without If-None-Match returned 200 OK.');
    $this->assertEqual($this->drupalGetHeader('X-Drupal-Cache'), 'HIT', 'Page was cached.');

    $this->drupalGet('', array(), array('If-Modified-Since: ' . gmdate(DATE_RFC7231, strtotime($last_modified) + 1), 'If-None-Match: ' . $etag));
    $this->assertResponse(200, 'Conditional request with new a If-Modified-Since date newer than Last-Modified returned 200 OK.');
    $this->assertEqual($this->drupalGetHeader('X-Drupal-Cache'), 'HIT', 'Page was cached.');

    $user = $this->drupalCreateUser();
    $this->drupalLogin($user);
    $this->drupalGet('', array(), array('If-Modified-Since: ' . $last_modified, 'If-None-Match: ' . $etag));
    $this->assertResponse(200, 'Conditional request returned 200 OK for authenticated user.');
    $this->assertFalse($this->drupalGetHeader('X-Drupal-Cache'), 'Absence of Page was not cached.');
    $this->assertFalse($this->drupalGetHeader('ETag'), 'ETag HTTP headers are not present for logged in users.');
    $this->assertFalse($this->drupalGetHeader('Last-Modified'), 'Last-Modified HTTP headers are not present for logged in users.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
