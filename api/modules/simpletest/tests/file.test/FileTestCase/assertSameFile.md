# FileTestCase::assertSameFile()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 90–93 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L90-L93)
- **Class:** [FileTestCase](../FileTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertSameFile($file1, $file2)
```

## Documentation

```text
Check that two files are the same by comparing the fid and filepath.

@param $file1
  File object to compare.
@param $file2
  File object to compare.
```

## Code

```php
  function assertSameFile($file1, $file2) {
    $this->assertEqual($file1->fid, $file2->fid, format_string('Files have the same ids: %file1 == %file2.', array('%file1' => $file1->fid, '%file2-fid' => $file2->fid)), 'Same file');
    $this->assertEqual($file1->uri, $file2->uri, format_string('Files have the same path: %file1 == %file2.', array('%file1' => $file1->uri, '%file2' => $file2->uri)), 'Same file');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
