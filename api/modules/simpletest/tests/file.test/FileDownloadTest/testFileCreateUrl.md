# FileDownloadTest::testFileCreateUrl()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2661–2677 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2661-L2677)
- **Class:** [FileDownloadTest](../FileDownloadTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testFileCreateUrl()
```

## Documentation

```text
Test file_create_url().
```

## Code

```php
  function testFileCreateUrl() {
    global $base_url;

    // Tilde (~) is excluded from this test because it is encoded by
    // rawurlencode() in PHP 5.2 but not in PHP 5.3, as per RFC 3986.
    // @see http://www.php.net/manual/en/function.rawurlencode.php#86506
    $basename = " -._!$'\"()*@[]?&+%#,;=:\n\x00" . // "Special" ASCII characters.
      "%23%25%26%2B%2F%3F" . // Characters that look like a percent-escaped string.
      "éøïвβ中國書۞"; // Characters from various non-ASCII alphabets.
    $basename_encoded = '%20-._%21%24%27%22%28%29%2A%40%5B%5D%3F%26%2B%25%23%2C%3B%3D%3A__' .
      '%2523%2525%2526%252B%252F%253F' .
      '%C3%A9%C3%B8%C3%AF%D0%B2%CE%B2%E4%B8%AD%E5%9C%8B%E6%9B%B8%DB%9E';

    $this->checkUrl('public', '', $basename, $base_url . '/' . file_stream_wrapper_get_instance_by_scheme('public')->getDirectoryPath() . '/' . $basename_encoded);
    $this->checkUrl('private', '', $basename, $base_url . '/system/files/' . $basename_encoded);
    $this->checkUrl('private', '', $basename, $base_url . '/?q=system/files/' . $basename_encoded, '0');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
