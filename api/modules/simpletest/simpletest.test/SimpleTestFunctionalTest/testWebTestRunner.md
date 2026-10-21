# SimpleTestFunctionalTest::testWebTestRunner()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 142–172 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L142-L172)
- **Class:** [SimpleTestFunctionalTest](../SimpleTestFunctionalTest.md)
- **Module/theme:** simpletest

## Signature

```php
function testWebTestRunner()
```

## Documentation

```text
Make sure that tests selected through the web interface are run and
that the results are displayed correctly.
```

## Code

```php
  function testWebTestRunner() {
    $this->pass = t('SimpleTest pass.');
    $this->fail = t('SimpleTest fail.');
    $this->valid_permission = 'access content';
    $this->invalid_permission = 'invalid permission';

    if ($this->inCURL()) {
      // Only run following code if this test is running itself through a CURL request.
      $this->stubTest();
    }
    else {

      // Run twice so test_ids can be accumulated.
      for ($i = 0; $i < 2; $i++) {
        // Run this test from web interface.
        $this->drupalGet('admin/config/development/testing');

        $edit = array();
        $edit['SimpleTestFunctionalTest'] = TRUE;
        $this->drupalPost(NULL, $edit, t('Run tests'));

        // Parse results and confirm that they are correct.
        $this->getTestResults();
        $this->confirmStubTestResults();
      }

      // Regression test for #290316.
      // Check that test_id is incrementing.
      $this->assertTrue($this->test_ids[0] != $this->test_ids[1], 'Test ID is incrementing.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
