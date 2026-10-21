# SimpleTestBrokenSetUp::testBreakSetUp()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 624–641 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L624-L641)
- **Class:** [SimpleTestBrokenSetUp](../SimpleTestBrokenSetUp.md)
- **Module/theme:** simpletest

## Signature

```php
function testBreakSetUp()
```

## Documentation

```text
Runs this test case from within the simpletest child site.
```

## Code

```php
  function testBreakSetUp() {
    // If the test is being run from the main site, run it again from the web
    // interface within the simpletest child site.
    if (!drupal_valid_test_ua()) {
      $edit['SimpleTestBrokenSetUp'] = TRUE;
      $this->drupalPost('admin/config/development/testing', $edit, t('Run tests'));

      // Verify that the broken test and its tearDown() method are skipped.
      $this->assertRaw(t('The test setUp() method has been run.'));
      $this->assertRaw(t('The test cannot be executed because it has not been set up properly.'));
      $this->assertNoRaw(t('The test method has run.'));
      $this->assertNoRaw(t('The tearDown() method has run.'));
    }
    // If the test is being run from within simpletest, output a message.
    else {
      $this->pass(t('The test method has run.'));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
