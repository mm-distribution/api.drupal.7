# simpletest_verbose()

- **Type:** Function
- **File:** [`modules/simpletest/drupal_web_test_case.php`](_file.md), lines 4070–4096 · [local source](../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L4070-L4096)
- **Module/theme:** simpletest

## Signature

```php
function simpletest_verbose($message, $original_file_directory = NULL, $test_class = NULL)
```

## Documentation

```text
Logs verbose message in a text file.

If verbose mode is enabled then page requests will be dumped to a file and
presented on the test result screen. The messages will be placed in a file
located in the simpletest directory in the original file system.

@param $message
  The verbose message to be stored.
@param $original_file_directory
  The original file directory, before it was changed for testing purposes.
@param $test_class
  The active test case class.

@return
  The ID of the message to be placed in related assertion messages.

@see DrupalTestCase->originalFileDirectory
@see DrupalWebTestCase->verbose()
```

## Code

```php
function simpletest_verbose($message, $original_file_directory = NULL, $test_class = NULL) {
  static $file_directory = NULL, $class = NULL, $id = 1, $verbose = NULL;

  // Will pass first time during setup phase, and when verbose is TRUE.
  if (!isset($original_file_directory) && !$verbose) {
    return FALSE;
  }

  if ($message && $file_directory) {
    $message = '<hr />ID #' . $id . ' (<a href="' . $class . '-' . ($id - 1) . '.html">Previous</a> | <a href="' . $class . '-' . ($id + 1) . '.html">Next</a>)<hr />' . $message;
    file_put_contents($file_directory . "/simpletest/verbose/$class-$id.html", $message, FILE_APPEND);
    return $id++;
  }

  if ($original_file_directory) {
    $file_directory = $original_file_directory;
    $class = $test_class;
    $verbose = variable_get('simpletest_verbose', TRUE);
    $directory = $file_directory . '/simpletest/verbose';
    $writable = file_prepare_directory($directory, FILE_CREATE_DIRECTORY);
    if ($writable && !file_exists($directory . '/.htaccess')) {
      file_put_contents($directory . '/.htaccess', "<IfModule mod_expires.c>\nExpiresActive Off\n</IfModule>\n");
    }
    return $writable;
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
