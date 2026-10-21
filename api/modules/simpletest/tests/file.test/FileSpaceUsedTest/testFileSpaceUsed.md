# FileSpaceUsedTest::testFileSpaceUsed()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 342–359 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L342-L359)
- **Class:** [FileSpaceUsedTest](../FileSpaceUsedTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testFileSpaceUsed()
```

## Documentation

```text
Test different users with the default status.
```

## Code

```php
  function testFileSpaceUsed() {
    // Test different users with default status.
    $this->assertEqual(file_space_used(2), 70);
    $this->assertEqual(file_space_used(3), 300);
    $this->assertEqual(file_space_used(), 370);

    // Test the status fields
    $this->assertEqual(file_space_used(NULL, 0), 4);
    $this->assertEqual(file_space_used(NULL, FILE_STATUS_PERMANENT), 370);

    // Test both the user and status.
    $this->assertEqual(file_space_used(1, 0), 0);
    $this->assertEqual(file_space_used(1, FILE_STATUS_PERMANENT), 0);
    $this->assertEqual(file_space_used(2, 0), 1);
    $this->assertEqual(file_space_used(2, FILE_STATUS_PERMANENT), 70);
    $this->assertEqual(file_space_used(3, 0), 3);
    $this->assertEqual(file_space_used(3, FILE_STATUS_PERMANENT), 300);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
