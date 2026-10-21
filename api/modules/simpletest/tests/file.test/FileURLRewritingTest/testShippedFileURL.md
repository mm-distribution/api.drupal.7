# FileURLRewritingTest::testShippedFileURL()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2745–2775 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2745-L2775)
- **Class:** [FileURLRewritingTest](../FileURLRewritingTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testShippedFileURL()
```

## Documentation

```text
Test the generating of rewritten shipped file URLs.
```

## Code

```php
  function testShippedFileURL()  {
    // Test generating an URL to a shipped file (i.e. a file that is part of
    // Drupal core, a module or a theme, for example a JavaScript file).

    // Test alteration of file URLs to use a CDN.
    variable_set('file_test_hook_file_url_alter', 'cdn');
    $filepath = 'misc/jquery.js';
    $url = file_create_url($filepath);
    $this->assertEqual(FILE_URL_TEST_CDN_1 . '/' . $filepath, $url, 'Correctly generated a CDN URL for a shipped file.');
    $filepath = 'misc/favicon.ico';
    $url = file_create_url($filepath);
    $this->assertEqual(FILE_URL_TEST_CDN_2 . '/' . $filepath, $url, 'Correctly generated a CDN URL for a shipped file.');

    // Test alteration of file URLs to use root-relative URLs.
    variable_set('file_test_hook_file_url_alter', 'root-relative');
    $filepath = 'misc/jquery.js';
    $url = file_create_url($filepath);
    $this->assertEqual(base_path() . '/' . $filepath, $url, 'Correctly generated a root-relative URL for a shipped file.');
    $filepath = 'misc/favicon.ico';
    $url = file_create_url($filepath);
    $this->assertEqual(base_path() . '/' . $filepath, $url, 'Correctly generated a root-relative URL for a shipped file.');

    // Test alteration of file URLs to use protocol-relative URLs.
    variable_set('file_test_hook_file_url_alter', 'protocol-relative');
    $filepath = 'misc/jquery.js';
    $url = file_create_url($filepath);
    $this->assertEqual('/' . base_path() . '/' . $filepath, $url, 'Correctly generated a protocol-relative URL for a shipped file.');
    $filepath = 'misc/favicon.ico';
    $url = file_create_url($filepath);
    $this->assertEqual('/' . base_path() . '/' . $filepath, $url, 'Correctly generated a protocol-relative URL for a shipped file.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
