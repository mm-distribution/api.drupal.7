# DrupalTestCase::run()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 530–587 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L530-L587)
- **Class:** [DrupalTestCase](../DrupalTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
public function run(array $methods = array())
```

## Documentation

```text
Run all tests in this class.

Regardless of whether $methods are passed or not, only method names
starting with "test" are executed.

@param $methods
  (optional) A list of method names in the test case class to run; e.g.,
  array('testFoo', 'testBar'). By default, all methods of the class are
  taken into account, but it can be useful to only run a few selected test
  methods during debugging.
```

## Code

```php
  public function run(array $methods = array()) {
    // Initialize verbose debugging.
    $class = get_class($this);
    simpletest_verbose(NULL, variable_get('file_public_path', conf_path() . '/files'), str_replace('\\', '_', $class));

    // HTTP auth settings (<username>:<password>) for the simpletest browser
    // when sending requests to the test site.
    $this->httpauth_method = variable_get('simpletest_httpauth_method', CURLAUTH_BASIC);
    $username = variable_get('simpletest_httpauth_username', NULL);
    $password = variable_get('simpletest_httpauth_password', NULL);
    if ($username && $password) {
      $this->httpauth_credentials = $username . ':' . $password;
    }

    set_error_handler(array($this, 'errorHandler'));
    // Iterate through all the methods in this class, unless a specific list of
    // methods to run was passed.
    $class_methods = get_class_methods($class);
    if ($methods) {
      $class_methods = array_intersect($class_methods, $methods);
    }
    foreach ($class_methods as $method) {
      // If the current method starts with "test", run it - it's a test.
      if (strtolower(substr($method, 0, 4)) == 'test') {
        // Insert a fail record. This will be deleted on completion to ensure
        // that testing completed.
        $method_info = new ReflectionMethod($class, $method);
        $caller = array(
          'file' => $method_info->getFileName(),
          'line' => $method_info->getStartLine(),
          'function' => $class . '->' . $method . '()',
        );
        $completion_check_id = DrupalTestCase::insertAssert($this->testId, $class, FALSE, t('The test did not complete due to a fatal error.'), 'Completion check', $caller);
        try {
          $this->setUp();
          if ($this->setup) {
            $this->$method();
            $this->tearDown();
          }
          else {
            $this->fail(t("The test cannot be executed because it has not been set up properly."));
          }
        }
        catch (Throwable $e) {
          $this->exceptionHandler($e);
        }
        catch (Exception $e) {
          // Cater for older PHP versions.
          $this->exceptionHandler($e);
        }
        // Remove the completion check record.
        DrupalTestCase::deleteAssert($completion_check_id);
      }
    }
    // Clear out the error messages and restore error handler.
    drupal_get_messages();
    restore_error_handler();
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
