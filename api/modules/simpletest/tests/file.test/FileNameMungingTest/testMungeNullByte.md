# FileNameMungingTest::testMungeNullByte()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2842–2846 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2842-L2846)
- **Class:** [FileNameMungingTest](../FileNameMungingTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testMungeNullByte()
```

## Documentation

```text
Tests munging with a null byte in the filename.
```

## Code

```php
  function testMungeNullByte() {
    $prefix = $this->randomName();
    $filename = $prefix . '.' . $this->bad_extension . "\0.txt";
    $this->assertEqual(file_munge_filename($filename, ''), $prefix . '.' . $this->bad_extension . '_.txt', 'A filename with a null byte is correctly munged to remove the null byte.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
