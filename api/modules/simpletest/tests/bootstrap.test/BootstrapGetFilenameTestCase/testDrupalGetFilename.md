# BootstrapGetFilenameTestCase::testDrupalGetFilename()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 439–483 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L439-L483)
- **Class:** [BootstrapGetFilenameTestCase](../BootstrapGetFilenameTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalGetFilename()
```

## Documentation

```text
Test that drupal_get_filename() works correctly when the file is not found in the database.
```

## Code

```php
  function testDrupalGetFilename() {
    // Reset the static cache so we can test the "db is not active" code of
    // drupal_get_filename().
    drupal_static_reset('drupal_get_filename');

    // Retrieving the location of a module.
    $this->assertIdentical(drupal_get_filename('module', 'php'), 'modules/php/php.module', t('Retrieve module location.'));

    // Retrieving the location of a theme.
    $this->assertIdentical(drupal_get_filename('theme', 'stark'), 'themes/stark/stark.info', t('Retrieve theme location.'));

    // Retrieving the location of a theme engine.
    $this->assertIdentical(drupal_get_filename('theme_engine', 'phptemplate'), 'themes/engines/phptemplate/phptemplate.engine', t('Retrieve theme engine location.'));

    // Retrieving the location of a profile. Profiles are a special case with
    // a fixed location and naming.
    $this->assertIdentical(drupal_get_filename('profile', 'standard'), 'profiles/standard/standard.profile', t('Retrieve install profile location.'));

    // When a file is not found in the database cache, drupal_get_filename()
    // searches several locations on the filesystem, including the DRUPAL_ROOT
    // directory. We use the '.script' extension below because this is a
    // non-existent filetype that will definitely not exist in the database.
    // Since there is already a scripts directory, drupal_get_filename() will
    // automatically check there for 'script' files, just as it does for (e.g.)
    // 'module' files in modules.
    $this->assertIdentical(drupal_get_filename('script', 'test'), 'scripts/test.script', t('Retrieve test script location.'));

    // When searching for a module that does not exist, drupal_get_filename()
    // should return NULL and trigger an appropriate error message.
    $this->getFilenameTestTriggeredError = NULL;
    set_error_handler(array($this, 'fileNotFoundErrorHandler'));
    $non_existing_module = $this->randomName();
    $this->assertNull(drupal_get_filename('module', $non_existing_module), 'Searching for a module that does not exist returns NULL.');
    $this->assertTrue(strpos($this->getFilenameTestTriggeredError, format_string('The following module is missing from the file system: %name', array('%name' => $non_existing_module))) === 0, 'Searching for an item that does not exist triggers the correct error.');
    restore_error_handler();

    // Check that the result is stored in the file system scan cache.
    $file_scans = _drupal_file_scan_cache();
    $this->assertIdentical($file_scans['module'][$non_existing_module], FALSE, 'Searching for a module that does not exist creates a record in the missing and moved files static variable.');

    // Performing the search again in the same request still should not find
    // the file, but the error message should not be repeated (therefore we do
    // not override the error handler here).
    $this->assertNull(drupal_get_filename('module', $non_existing_module), 'Searching for a module that does not exist returns NULL during the second search.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
