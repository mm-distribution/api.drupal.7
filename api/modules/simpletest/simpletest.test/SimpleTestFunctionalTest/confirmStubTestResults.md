# SimpleTestFunctionalTest::confirmStubTestResults()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 211–239 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L211-L239)
- **Class:** [SimpleTestFunctionalTest](../SimpleTestFunctionalTest.md)
- **Module/theme:** simpletest

## Signature

```php
function confirmStubTestResults()
```

## Documentation

```text
Confirm that the stub test produced the desired results.
```

## Code

```php
  function confirmStubTestResults() {
    $this->assertAssertion(t('Enabled modules: %modules', array('%modules' => 'non_existent_module')), 'Other', 'Fail', 'simpletest.test', 'SimpleTestFunctionalTest->setUp()');

    $this->assertAssertion($this->pass, 'Other', 'Pass', 'simpletest.test', 'SimpleTestFunctionalTest->stubTest()');
    $this->assertAssertion($this->fail, 'Other', 'Fail', 'simpletest.test', 'SimpleTestFunctionalTest->stubTest()');

    $this->assertAssertion(t('Created permissions: @perms', array('@perms' => $this->valid_permission)), 'Role', 'Pass', 'simpletest.test', 'SimpleTestFunctionalTest->stubTest()');
    $this->assertAssertion(t('Invalid permission %permission.', array('%permission' => $this->invalid_permission)), 'Role', 'Fail', 'simpletest.test', 'SimpleTestFunctionalTest->stubTest()');

    // Check that a warning is caught by simpletest.
    // The exact error message differs between PHP versions so we check only
    // the presense of the 'foreach' statement.
    $this->assertAssertion('foreach()', 'Warning', 'Fail', 'simpletest.test', 'SimpleTestFunctionalTest->stubTest()');

    // Check that the backtracing code works for specific assert function.
    $this->assertAssertion('This is nothing.', 'Other', 'Pass', 'simpletest.test', 'SimpleTestFunctionalTest->stubTest()');

    // Check that errors that occur inside PHP internal functions are correctly reported.
    // The exact error message differs between PHP versions so we check only
    // the function name 'simplexml_load_string'.
    $this->assertAssertion('simplexml_load_string', 'Warning', 'Fail', 'simpletest.test', 'SimpleTestFunctionalTest->stubTest()');

    $this->assertAssertion("Debug: 'Foo'", 'Debug', 'Fail', 'simpletest.test', 'SimpleTestFunctionalTest->stubTest()');

    $this->assertEqual('6 passes, 5 fails, 4 exceptions, and 1 debug message', $this->childTestResults['summary'], 'Stub test summary is correct');

    $this->test_ids[] = $test_id = $this->getTestIdFromResults();
    $this->assertTrue($test_id, 'Found test ID in results.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
