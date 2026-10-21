# FileURLRewritingTest::testPublicCreatedFileURL()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2780–2801 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2780-L2801)
- **Class:** [FileURLRewritingTest](../FileURLRewritingTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testPublicCreatedFileURL()
```

## Documentation

```text
Test the generating of rewritten public created file URLs.
```

## Code

```php
  function testPublicCreatedFileURL() {
    // Test generating an URL to a created file.

    // Test alteration of file URLs to use a CDN.
    variable_set('file_test_hook_file_url_alter', 'cdn');
    $file = $this->createFile();
    $url = file_create_url($file->uri);
    $public_directory_path = file_stream_wrapper_get_instance_by_scheme('public')->getDirectoryPath();
    $this->assertEqual(FILE_URL_TEST_CDN_2 . '/' . $public_directory_path . '/' . $file->filename, $url, 'Correctly generated a CDN URL for a created file.');

    // Test alteration of file URLs to use root-relative URLs.
    variable_set('file_test_hook_file_url_alter', 'root-relative');
    $file = $this->createFile();
    $url = file_create_url($file->uri);
    $this->assertEqual(base_path() . '/' . $public_directory_path . '/' . $file->filename, $url, 'Correctly generated a root-relative URL for a created file.');

    // Test alteration of file URLs to use a protocol-relative URLs.
    variable_set('file_test_hook_file_url_alter', 'protocol-relative');
    $file = $this->createFile();
    $url = file_create_url($file->uri);
    $this->assertEqual('/' . base_path() . '/' . $public_directory_path . '/' . $file->filename, $url, 'Correctly generated a protocol-relative URL for a created file.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
