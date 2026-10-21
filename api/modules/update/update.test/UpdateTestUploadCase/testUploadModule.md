# UpdateTestUploadCase::testUploadModule()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 718–741 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L718-L741)
- **Class:** [UpdateTestUploadCase](../UpdateTestUploadCase.md)
- **Module/theme:** update

## Signature

```php
public function testUploadModule()
```

## Documentation

```text
Tests upload and extraction of a module.
```

## Code

```php
  public function testUploadModule() {
    // Images are not valid archives, so get one and try to install it. We
    // need an extra variable to store the result of drupalGetTestFiles()
    // since reset() takes an argument by reference and passing in a constant
    // emits a notice in strict mode.
    $imageTestFiles = $this->drupalGetTestFiles('image');
    $invalidArchiveFile = reset($imageTestFiles);
    $edit = array(
      'files[project_upload]' => $invalidArchiveFile->uri,
    );
    // This also checks that the correct archive extensions are allowed.
    $this->drupalPost('admin/modules/install', $edit, t('Install'));
    $this->assertText(t('Only files with the following extensions are allowed: @archive_extensions.', array('@archive_extensions' => archiver_get_extensions())),'Only valid archives can be uploaded.');

    // Check to ensure an existing module can't be reinstalled. Also checks that
    // the archive was extracted since we can't know if the module is already
    // installed until after extraction.
    $validArchiveFile = drupal_get_path('module', 'update') . '/tests/aaa_update_test.tar.gz';
    $edit = array(
      'files[project_upload]' => $validArchiveFile,
    );
    $this->drupalPost('admin/modules/install', $edit, t('Install'));
    $this->assertText(t('@module_name is already installed.', array('@module_name' => 'AAA Update test')), 'Existing module was extracted and not reinstalled.');
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
