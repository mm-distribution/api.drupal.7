# DrupalSystemListingTestCase::testDirectoryPrecedence()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2873–2910 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2873-L2910)
- **Class:** [DrupalSystemListingTestCase](../DrupalSystemListingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDirectoryPrecedence()
```

## Documentation

```text
Test that files in different directories take precedence as expected.
```

## Code

```php
  function testDirectoryPrecedence() {
    // Define the module files we will search for, and the directory precedence
    // we expect.
    $expected_directories = array(
      // When the copy of the module in the profile directory is incompatible
      // with Drupal core, the copy in the core modules directory takes
      // precedence.
      'drupal_system_listing_incompatible_test' => array(
        'modules/simpletest/tests',
        'profiles/testing/modules',
      ),
      // When both copies of the module are compatible with Drupal core, the
      // copy in the profile directory takes precedence.
      'drupal_system_listing_compatible_test' => array(
        'profiles/testing/modules',
        'modules/simpletest/tests',
      ),
    );

    // This test relies on two versions of the same module existing in
    // different places in the filesystem. Without that, the test has no
    // meaning, so assert their presence first.
    foreach ($expected_directories as $module => $directories) {
      foreach ($directories as $directory) {
        $filename = "$directory/$module/$module.module";
        $this->assertTrue(file_exists(DRUPAL_ROOT . '/' . $filename), format_string('@filename exists.', array('@filename' => $filename)));
      }
    }

    // Now scan the directories and check that the files take precedence as
    // expected.
    $files = drupal_system_listing('/\.module$/', 'modules', 'name', 1);
    foreach ($expected_directories as $module => $directories) {
      $expected_directory = array_shift($directories);
      $expected_filename = "$expected_directory/$module/$module.module";
      $this->assertEqual($files[$module]->uri, $expected_filename, format_string('Module @module was found at @filename.', array('@module' => $module, '@filename' => $expected_filename)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
