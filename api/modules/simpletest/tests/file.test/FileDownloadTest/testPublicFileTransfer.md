# FileDownloadTest::testPublicFileTransfer()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2587–2605 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2587-L2605)
- **Class:** [FileDownloadTest](../FileDownloadTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testPublicFileTransfer()
```

## Documentation

```text
Test the public file transfer system.
```

## Code

```php
  function testPublicFileTransfer() {
    // Test generating an URL to a created file.
    $file = $this->createFile();
    $url = file_create_url($file->uri);
    // URLs can't contain characters outside the ASCII set so $filename has to be
    // encoded.
    $filename = $GLOBALS['base_url'] . '/' . file_stream_wrapper_get_instance_by_scheme('public')->getDirectoryPath() . '/' . rawurlencode($file->filename);
    $this->assertEqual($filename, $url, 'Correctly generated a URL for a created file.');
    $this->drupalHead($url);
    $this->assertResponse(200, 'Confirmed that the generated URL is correct by downloading the created file.');

    // Test generating an URL to a shipped file (i.e. a file that is part of
    // Drupal core, a module or a theme, for example a JavaScript file).
    $filepath = 'misc/jquery.js';
    $url = file_create_url($filepath);
    $this->assertEqual($GLOBALS['base_url'] . '/' . $filepath, $url, 'Correctly generated a URL for a shipped file.');
    $this->drupalHead($url);
    $this->assertResponse(200, 'Confirmed that the generated URL is correct by downloading the shipped file.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
