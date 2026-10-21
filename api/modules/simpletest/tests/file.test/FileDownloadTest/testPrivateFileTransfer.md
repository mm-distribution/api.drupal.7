# FileDownloadTest::testPrivateFileTransfer()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2610–2656 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2610-L2656)
- **Class:** [FileDownloadTest](../FileDownloadTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testPrivateFileTransfer()
```

## Documentation

```text
Test the private file transfer system.
```

## Code

```php
  function testPrivateFileTransfer() {
    // Set file downloads to private so handler functions get called.

    // Create a file.
    $contents = $this->randomName(8);
    $file = $this->createFile(NULL, $contents, 'private');
    $url  = file_create_url($file->uri);

    // Set file_test access header to allow the download.
    file_test_reset();
    file_test_set_return('download', array('x-foo' => 'Bar'));
    $this->drupalGet($url);
    $headers = $this->drupalGetHeaders();
    $this->assertEqual($headers['x-foo'], 'Bar', 'Found header set by file_test module on private download.');
    $this->assertResponse(200, 'Correctly allowed access to a file when file_test provides headers.');
    // Ensure hook_file_download is fired correctly.
    $hooks_results = file_test_get_all_calls();
    $file_uri = !empty($hooks_results['download']) ? reset($hooks_results['download'][0]) : '';
    $this->assertEqual($file->uri, $file_uri);

    // Test that the file transferred correctly.
    $this->assertEqual($contents, $this->content, 'Contents of the file are correct.');

    // Deny access to all downloads via a -1 header.
    file_test_set_return('download', -1);
    $this->drupalHead($url);
    $this->assertResponse(403, 'Correctly denied access to a file when file_test sets the header to -1.');

    // Try non-existent file.
    file_test_reset();
    $url = file_create_url('private://' . $this->randomName());
    $this->drupalHead($url);
    $this->assertResponse(404, 'Correctly returned 404 response for a non-existent file.');
    // Assert that hook_file_download is not called.
    $hooks_results = file_test_get_all_calls();
    $hook_download_results = isset($hooks_results['download']) ? $hooks_results['download'] : NULL;
    $this->assertEqual(array(), $hook_download_results);

    // Try requesting the private file url without a file specified.
    file_test_reset();
    $this->drupalGet('system/files');
    $this->assertResponse(404, 'Correctly returned 404 response for a private file url without a file specified.');
    // Assert that hook_file_download is not called.
    $hooks_results = file_test_get_all_calls();
    $hook_download_results = isset($hooks_results['download']) ? $hooks_results['download'] : NULL;
    $this->assertEqual(array(), $hook_download_results);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
