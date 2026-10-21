# FileTestCase::assertDifferentFile()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 77–80 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L77-L80)
- **Class:** [FileTestCase](../FileTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertDifferentFile($file1, $file2)
```

## Documentation

```text
Check that two files are not the same by comparing the fid and filepath.

@param $file1
  File object to compare.
@param $file2
  File object to compare.
```

## Code

```php
  function assertDifferentFile($file1, $file2) {
    $this->assertNotEqual($file1->fid, $file2->fid, format_string('Files have different ids: %file1 != %file2.', array('%file1' => $file1->fid, '%file2' => $file2->fid)), 'Different file');
    $this->assertNotEqual($file1->uri, $file2->uri, format_string('Files have different paths: %file1 != %file2.', array('%file1' => $file1->uri, '%file2' => $file2->uri)), 'Different file');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
