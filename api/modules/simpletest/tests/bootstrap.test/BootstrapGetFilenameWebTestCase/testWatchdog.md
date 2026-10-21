# BootstrapGetFilenameWebTestCase::testWatchdog()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 616–637 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L616-L637)
- **Class:** [BootstrapGetFilenameWebTestCase](../BootstrapGetFilenameWebTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testWatchdog()
```

## Documentation

```text
Test that watchdog messages about missing files are correctly recorded.
```

## Code

```php
  public function testWatchdog() {
    // Search for a module that does not exist in either the file system or the
    // {system} table. Make sure that an appropriate warning is recorded in the
    // logs.
    $non_existing_module = $this->randomName();
    $query_parameters = array(
      ':type' => 'php',
      ':severity' => WATCHDOG_WARNING,
    );
    $this->assertEqual(db_query('SELECT COUNT(*) FROM {watchdog} WHERE type = :type AND severity = :severity', $query_parameters)->fetchField(), 0, 'No warning message appears in the logs before searching for a module that does not exist.');
    // Trigger the drupal_get_filename() call. This must be done via a request
    // to a separate URL since the watchdog() will happen in a shutdown
    // function, and so that SimpleTest can be told to ignore (and not fail as
    // a result of) the expected PHP warnings generated during this process.
    variable_set('system_test_drupal_get_filename_test_module_name', $non_existing_module);
    $this->drupalGet('system-test/drupal-get-filename');
    $message_variables = db_query('SELECT variables FROM {watchdog} WHERE type = :type AND severity = :severity', $query_parameters)->fetchCol();
    $this->assertEqual(count($message_variables), 1, 'A single warning message appears in the logs after searching for a module that does not exist.');
    $variables = reset($message_variables);
    $variables = unserialize($variables);
    $this->assertTrue(isset($variables['!message']) && strpos($variables['!message'], format_string('The following module is missing from the file system: %name', array('%name' => $non_existing_module))) !== FALSE, 'The warning message that appears in the logs after searching for a module that does not exist contains the expected text.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
