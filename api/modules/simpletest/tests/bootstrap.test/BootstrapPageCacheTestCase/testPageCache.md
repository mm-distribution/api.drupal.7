# BootstrapPageCacheTestCase::testPageCache()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 179–215 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L179-L215)
- **Class:** [BootstrapPageCacheTestCase](../BootstrapPageCacheTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testPageCache()
```

## Documentation

```text
Test cache headers.
```

## Code

```php
  function testPageCache() {
    variable_set('cache', 1);

    // Fill the cache.
    $this->drupalGet('system-test/set-header', array('query' => array('name' => 'Foo', 'value' => 'bar')));
    $this->assertEqual($this->drupalGetHeader('X-Drupal-Cache'), 'MISS', 'Page was not cached.');
    $this->assertEqual($this->drupalGetHeader('Vary'), 'Cookie,Accept-Encoding', 'Vary header was sent.');
    $this->assertEqual($this->drupalGetHeader('Cache-Control'), 'public, max-age=0', 'Cache-Control header was sent.');
    $this->assertEqual($this->drupalGetHeader('Expires'), 'Sun, 19 Nov 1978 05:00:00 GMT', 'Expires header was sent.');
    $this->assertEqual($this->drupalGetHeader('Foo'), 'bar', 'Custom header was sent.');

    // Check cache.
    $this->drupalGet('system-test/set-header', array('query' => array('name' => 'Foo', 'value' => 'bar')));
    $this->assertEqual($this->drupalGetHeader('X-Drupal-Cache'), 'HIT', 'Page was cached.');
    $this->assertEqual($this->drupalGetHeader('Vary'), 'Cookie,Accept-Encoding', 'Vary: Cookie header was sent.');
    $this->assertEqual($this->drupalGetHeader('Cache-Control'), 'public, max-age=0', 'Cache-Control header was sent.');
    $this->assertEqual($this->drupalGetHeader('Expires'), 'Sun, 19 Nov 1978 05:00:00 GMT', 'Expires header was sent.');
    $this->assertEqual($this->drupalGetHeader('Foo'), 'bar', 'Custom header was sent.');
    $this->assertEqual($this->drupalGetHeader('X-Content-Type-Options'), 'nosniff', 'X-Content-Type-Options header was sent.');

    // Check replacing default headers.
    $this->drupalGet('system-test/set-header', array('query' => array('name' => 'Expires', 'value' => 'Fri, 19 Nov 2008 05:00:00 GMT')));
    $this->assertEqual($this->drupalGetHeader('Expires'), 'Fri, 19 Nov 2008 05:00:00 GMT', 'Default header was replaced.');
    $this->drupalGet('system-test/set-header', array('query' => array('name' => 'Vary', 'value' => 'User-Agent')));
    $this->assertEqual($this->drupalGetHeader('Vary'), 'User-Agent,Accept-Encoding', 'Default header was replaced.');

    // Check that authenticated users bypass the cache.
    $user = $this->drupalCreateUser();
    $this->drupalLogin($user);
    $this->drupalGet('system-test/set-header', array('query' => array('name' => 'Foo', 'value' => 'bar')));
    $this->assertFalse($this->drupalGetHeader('X-Drupal-Cache'), 'Caching was bypassed.');
    $this->assertTrue(strpos($this->drupalGetHeader('Vary'), 'Cookie') === FALSE, 'Vary: Cookie header was not sent.');
    $this->assertEqual($this->drupalGetHeader('Cache-Control'), 'no-cache, must-revalidate', 'Cache-Control header was sent.');
    $this->assertEqual($this->drupalGetHeader('Expires'), 'Sun, 19 Nov 1978 05:00:00 GMT', 'Expires header was sent.');
    $this->assertEqual($this->drupalGetHeader('Foo'), 'bar', 'Custom header was sent.');

  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
