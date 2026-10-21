# FileSaveUploadTest::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 594–623 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L594-L623)
- **Class:** [FileSaveUploadTest](../FileSaveUploadTest.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();
    $account = $this->drupalCreateUser(array('access content'));
    $this->drupalLogin($account);

    $image_files = $this->drupalGetTestFiles('image');
    $this->image = current($image_files);

    list(, $this->image_extension) = explode('.', $this->image->filename);
    $this->assertTrue(is_file($this->image->uri), "The image file we're going to upload exists.");

    $this->phpfile = current($this->drupalGetTestFiles('php'));
    $this->assertTrue(is_file($this->phpfile->uri), "The PHP file we're going to upload exists.");

    $this->maxFidBefore = db_query('SELECT MAX(fid) AS fid FROM {file_managed}')->fetchField();

    // Upload with replace to guarantee there's something there.
    $edit = array(
      'file_test_replace' => FILE_EXISTS_REPLACE,
      'files[file_test_upload]' => drupal_realpath($this->image->uri),
    );
    $this->drupalPost('file-test/upload', $edit, t('Submit'));
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $this->assertRaw(t('You WIN!'), 'Found the success message.');

    // Check that the correct hooks were called then clean out the hook
    // counters.
    $this->assertFileHooksCalled(array('validate', 'insert'));
    file_test_reset();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
