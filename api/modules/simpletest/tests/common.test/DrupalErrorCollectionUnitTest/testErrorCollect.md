# DrupalErrorCollectionUnitTest::testErrorCollect()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2769–2785 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2769-L2785)
- **Class:** [DrupalErrorCollectionUnitTest](../DrupalErrorCollectionUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testErrorCollect()
```

## Documentation

```text
Test that simpletest collects errors from the tested site.
```

## Code

```php
  function testErrorCollect() {
    $this->collectedErrors = array();
    $this->drupalGet('error-test/generate-warnings-with-report');
    $this->assertEqual(count($this->collectedErrors), 3, 'Three errors were collected');

    if (count($this->collectedErrors) == 3) {
      $this->assertError($this->collectedErrors[0], 'Notice', 'error_test_generate_warnings()', 'error_test.module', 'Object of class stdClass could not be converted to int');
      $this->assertError($this->collectedErrors[1], 'Warning', 'error_test_generate_warnings()', 'error_test.module', \PHP_VERSION_ID < 80000 ? 'Invalid argument supplied for foreach()' : 'foreach() argument must be of type array|object, string given');
      $this->assertError($this->collectedErrors[2], 'User warning', 'error_test_generate_warnings()', 'error_test.module', 'Drupal is awesome');
    }
    else {
      // Give back the errors to the log report.
      foreach ($this->collectedErrors as $error) {
        parent::error($error['message'], $error['group'], $error['caller']);
      }
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
