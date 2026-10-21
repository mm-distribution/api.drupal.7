# FileSaveUploadTest::testNoUpload()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1043–1046 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1043-L1046)
- **Class:** [FileSaveUploadTest](../FileSaveUploadTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testNoUpload()
```

## Documentation

```text
Test for no failures when not uploading a file.
```

## Code

```php
  function testNoUpload() {
    $this->drupalPost('file-test/upload', array(), t('Submit'));
    $this->assertNoRaw(t('Epic upload FAIL!'), 'Failure message not found.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
