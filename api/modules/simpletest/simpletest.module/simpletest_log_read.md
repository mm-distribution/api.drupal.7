# simpletest_log_read()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 264–286 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L264-L286)
- **Module/theme:** simpletest

## Signature

```php
function simpletest_log_read($test_id, $prefix, $test_class, $during_test = FALSE)
```

## Documentation

```text
Read the error log and report any errors as assertion failures.

The errors in the log should only be fatal errors since any other errors
will have been recorded by the error handler.

@param $test_id
  The test ID to which the log relates.
@param $prefix
  The database prefix to which the log relates.
@param $test_class
  The test class to which the log relates.
@param $during_test
  Indicates that the current file directory path is a temporary file
  file directory used during testing.
@return
  Found any entries in log.
```

## Code

```php
function simpletest_log_read($test_id, $prefix, $test_class, $during_test = FALSE) {
  $log = 'public://' . ($during_test ? '' : '/simpletest/' . substr($prefix, 10)) . '/error.log';
  $found = FALSE;
  if (file_exists($log)) {
    foreach (file($log) as $line) {
      if (preg_match('/\[.*?\] (.*?): (.*?) in (.*) on line (\d+)/', $line, $match)) {
        // Parse PHP fatal errors for example: PHP Fatal error: Call to
        // undefined function break_me() in /path/to/file.php on line 17
        $caller = array(
          'line' => $match[4],
          'file' => $match[3],
        );
        DrupalTestCase::insertAssert($test_id, $test_class, FALSE, $match[2], $match[1], $caller);
      }
      else {
        // Unknown format, place the entire message in the log.
        DrupalTestCase::insertAssert($test_id, $test_class, FALSE, $line, 'Fatal error');
      }
      $found = TRUE;
    }
  }
  return $found;
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._
