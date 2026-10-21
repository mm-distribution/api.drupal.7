# BootstrapPageCacheTestCase::testPageCompression()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 224–261 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L224-L261)
- **Class:** [BootstrapPageCacheTestCase](../BootstrapPageCacheTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testPageCompression()
```

## Documentation

```text
Test page compression.

The test should pass even if zlib.output_compression is enabled in php.ini,
.htaccess or similar, or if compression is done outside PHP, e.g. by the
mod_deflate Apache module.
```

## Code

```php
  function testPageCompression() {
    variable_set('cache', 1);

    // Fill the cache and verify that output is compressed.
    $this->drupalGet('', array(), array('Accept-Encoding: gzip,deflate'));
    $this->assertEqual($this->drupalGetHeader('X-Drupal-Cache'), 'MISS', 'Page was not cached.');
    $this->drupalSetContent(gzinflate(substr($this->drupalGetContent(), 10, -8)));
    $this->assertRaw('</html>', 'Page was gzip compressed.');

    // Verify that cached output is compressed.
    $this->drupalGet('', array(), array('Accept-Encoding: gzip,deflate'));
    $this->assertEqual($this->drupalGetHeader('X-Drupal-Cache'), 'HIT', 'Page was cached.');
    $this->assertEqual($this->drupalGetHeader('Content-Encoding'), 'gzip', 'A Content-Encoding header was sent.');
    $this->drupalSetContent(gzinflate(substr($this->drupalGetContent(), 10, -8)));
    $this->assertRaw('</html>', 'Page was gzip compressed.');

    // Verify that a client without compression support gets an uncompressed page.
    $this->drupalGet('');
    $this->assertEqual($this->drupalGetHeader('X-Drupal-Cache'), 'HIT', 'Page was cached.');
    $this->assertFalse($this->drupalGetHeader('Content-Encoding'), 'A Content-Encoding header was not sent.');
    $this->assertTitle(t('Welcome to @site-name | @site-name', array('@site-name' => variable_get('site_name', 'Drupal'))), 'Site title matches.');
    $this->assertRaw('</html>', 'Page was not compressed.');

    // Verify that an empty page doesn't throw an error when being decompressed.
    $this->drupalGet('system-test/empty-page');

    // Disable compression mode.
    variable_set('page_compression', FALSE);

    // Verify if cached page is still available for a client with compression support.
    $this->drupalGet('', array(), array('Accept-Encoding: gzip,deflate'));
    $this->drupalSetContent(gzinflate(substr($this->drupalGetContent(), 10, -8)));
    $this->assertRaw('</html>', 'Page was delivered after compression mode is changed (compression support enabled).');

    // Verify if cached page is still available for a client without compression support.
    $this->drupalGet('');
    $this->assertRaw('</html>', 'Page was delivered after compression mode is changed (compression support disabled).');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
