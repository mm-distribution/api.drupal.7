# BootstrapGetFilenameWebTestCase::testDrupalGetFilename()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 525–599 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L525-L599)
- **Class:** [BootstrapGetFilenameWebTestCase](../BootstrapGetFilenameWebTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalGetFilename()
```

## Documentation

```text
Test that drupal_get_filename() works correctly with a full Drupal site.
```

## Code

```php
  function testDrupalGetFilename() {
    // Search for a module that exists in the file system and the {system}
    // table and make sure that it is found.
    $this->assertIdentical(drupal_get_filename('module', 'node'), 'modules/node/node.module', 'Module found at expected location.');

    // Search for a module that does not exist in either the file system or the
    // {system} table. Make sure that an appropriate error is triggered and
    // that the module winds up in the static and persistent cache.
    $this->getFilenameTestTriggeredError = NULL;
    set_error_handler(array($this, 'fileNotFoundErrorHandler'));
    $non_existing_module = $this->randomName();
    $this->assertNull(drupal_get_filename('module', $non_existing_module), 'Searching for a module that does not exist returns NULL.');
    $this->assertTrue(strpos($this->getFilenameTestTriggeredError, format_string('The following module is missing from the file system: %name', array('%name' => $non_existing_module))) === 0, 'Searching for a module that does not exist triggers the correct error.');
    restore_error_handler();
    $file_scans = _drupal_file_scan_cache();
    $this->assertIdentical($file_scans['module'][$non_existing_module], FALSE, 'Searching for a module that does not exist creates a record in the missing and moved files static variable.');
    drupal_file_scan_write_cache();
    $cache = cache_get('_drupal_file_scan_cache', 'cache_bootstrap');
    $this->assertIdentical($cache->data['module'][$non_existing_module], FALSE, 'Searching for a module that does not exist creates a record in the missing and moved files persistent cache.');

    // Simulate moving a module to a location that does not match the location
    // in the {system} table and perform similar tests as above.
    db_update('system')
      ->fields(array('filename' => 'modules/simpletest/tests/fake_location/module_test.module'))
      ->condition('name', 'module_test')
      ->condition('type', 'module')
      ->execute();
    $this->getFilenameTestTriggeredError = NULL;
    set_error_handler(array($this, 'fileNotFoundErrorHandler'));
    $this->assertIdentical(drupal_get_filename('module', 'module_test'), 'modules/simpletest/tests/module_test.module', 'Searching for a module that has moved finds the module at its new location.');
    $this->assertTrue(strpos($this->getFilenameTestTriggeredError, format_string('The following module has moved within the file system: %name', array('%name' => 'module_test'))) === 0, 'Searching for a module that has moved triggers the correct error.');
    restore_error_handler();
    $file_scans = _drupal_file_scan_cache();
    $this->assertIdentical($file_scans['module']['module_test'], 'modules/simpletest/tests/module_test.module', 'Searching for a module that has moved creates a record in the missing and moved files static variable.');
    drupal_file_scan_write_cache();
    $cache = cache_get('_drupal_file_scan_cache', 'cache_bootstrap');
    $this->assertIdentical($cache->data['module']['module_test'], 'modules/simpletest/tests/module_test.module', 'Searching for a module that has moved creates a record in the missing and moved files persistent cache.');

    // Simulate a module that exists in the {system} table but does not exist
    // in the file system and perform similar tests as above.
    $non_existing_module = $this->randomName();
    db_update('system')
      ->fields(array('name' => $non_existing_module))
      ->condition('name', 'module_test')
      ->condition('type', 'module')
      ->execute();
    $this->getFilenameTestTriggeredError = NULL;
    set_error_handler(array($this, 'fileNotFoundErrorHandler'));
    $this->assertNull(drupal_get_filename('module', $non_existing_module), 'Searching for a module that exists in the system table but not in the file system returns NULL.');
    $this->assertTrue(strpos($this->getFilenameTestTriggeredError, format_string('The following module is missing from the file system: %name', array('%name' => $non_existing_module))) === 0, 'Searching for a module that exists in the system table but not in the file system triggers the correct error.');
    restore_error_handler();
    $file_scans = _drupal_file_scan_cache();
    $this->assertIdentical($file_scans['module'][$non_existing_module], FALSE, 'Searching for a module that exists in the system table but not in the file system creates a record in the missing and moved files static variable.');
    drupal_file_scan_write_cache();
    $cache = cache_get('_drupal_file_scan_cache', 'cache_bootstrap');
    $this->assertIdentical($cache->data['module'][$non_existing_module], FALSE, 'Searching for a module that exists in the system table but not in the file system creates a record in the missing and moved files persistent cache.');

    // Simulate a module that exists in the file system but not in the {system}
    // table and perform similar tests as above.
    db_delete('system')
      ->condition('name', 'common_test')
      ->condition('type', 'module')
      ->execute();
    system_list_reset();
    $this->getFilenameTestTriggeredError = NULL;
    set_error_handler(array($this, 'fileNotFoundErrorHandler'));
    $this->assertIdentical(drupal_get_filename('module', 'common_test'), 'modules/simpletest/tests/common_test.module', 'Searching for a module that does not exist in the system table finds the module at its actual location.');
    $this->assertTrue(strpos($this->getFilenameTestTriggeredError, format_string('The following module has moved within the file system: %name', array('%name' => 'common_test'))) === 0, 'Searching for a module that does not exist in the system table triggers the correct error.');
    restore_error_handler();
    $file_scans = _drupal_file_scan_cache();
    $this->assertIdentical($file_scans['module']['common_test'], 'modules/simpletest/tests/common_test.module', 'Searching for a module that does not exist in the system table creates a record in the missing and moved files static variable.');
    drupal_file_scan_write_cache();
    $cache = cache_get('_drupal_file_scan_cache', 'cache_bootstrap');
    $this->assertIdentical($cache->data['module']['common_test'], 'modules/simpletest/tests/common_test.module', 'Searching for a module that does not exist in the system table creates a record in the missing and moved files persistent cache.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
