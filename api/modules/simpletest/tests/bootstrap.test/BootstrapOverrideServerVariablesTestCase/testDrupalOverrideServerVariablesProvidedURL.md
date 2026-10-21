# BootstrapOverrideServerVariablesTestCase::testDrupalOverrideServerVariablesProvidedURL()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 795–823 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L795-L823)
- **Class:** [BootstrapOverrideServerVariablesTestCase](../BootstrapOverrideServerVariablesTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalOverrideServerVariablesProvidedURL()
```

## Documentation

```text
Test providing a direct URL to to drupal_override_server_variables().
```

## Code

```php
  function testDrupalOverrideServerVariablesProvidedURL() {
    $tests = array(
      'http://example.com' => array(
        'HTTP_HOST' => 'example.com',
        'SCRIPT_NAME' => isset($_SERVER['SCRIPT_NAME']) ? $_SERVER['SCRIPT_NAME'] : NULL,
      ),
      'http://example.com/index.php' => array(
        'HTTP_HOST' => 'example.com',
        'SCRIPT_NAME' => '/index.php',
      ),
      'http://example.com/subdirectory/index.php' => array(
        'HTTP_HOST' => 'example.com',
        'SCRIPT_NAME' => '/subdirectory/index.php',
      ),
    );
    foreach ($tests as $url => $expected_server_values) {
      // Remember the original value of $_SERVER, since the function call below
      // will modify it.
      $original_server = $_SERVER;
      // Call drupal_override_server_variables() and ensure that all expected
      // $_SERVER variables were modified correctly.
      drupal_override_server_variables(array('url' => $url));
      foreach ($expected_server_values as $key => $value) {
        $this->assertIdentical($_SERVER[$key], $value);
      }
      // Restore the original value of $_SERVER.
      $_SERVER = $original_server;
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
