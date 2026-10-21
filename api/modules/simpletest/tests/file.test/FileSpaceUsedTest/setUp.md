# FileSpaceUsedTest::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 319–337 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L319-L337)
- **Class:** [FileSpaceUsedTest](../FileSpaceUsedTest.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();

    // Create records for a couple of users with different sizes.
    $file = array('uid' => 2, 'uri' => 'public://example1.txt', 'filesize' => 50, 'status' => FILE_STATUS_PERMANENT);
    drupal_write_record('file_managed', $file);
    $file = array('uid' => 2, 'uri' => 'public://example2.txt', 'filesize' => 20, 'status' => FILE_STATUS_PERMANENT);
    drupal_write_record('file_managed', $file);
    $file = array('uid' => 3, 'uri' => 'public://example3.txt', 'filesize' => 100, 'status' => FILE_STATUS_PERMANENT);
    drupal_write_record('file_managed', $file);
    $file = array('uid' => 3, 'uri' => 'public://example4.txt', 'filesize' => 200, 'status' => FILE_STATUS_PERMANENT);
    drupal_write_record('file_managed', $file);

    // Now create some non-permanent files.
    $file = array('uid' => 2, 'uri' => 'public://example5.txt', 'filesize' => 1, 'status' => 0);
    drupal_write_record('file_managed', $file);
    $file = array('uid' => 3, 'uri' => 'public://example6.txt', 'filesize' => 3, 'status' => 0);
    drupal_write_record('file_managed', $file);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
