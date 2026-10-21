# FileTestCase::assertFileUnchanged()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 59–67 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L59-L67)
- **Class:** [FileTestCase](../FileTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertFileUnchanged($before, $after)
```

## Documentation

```text
Check that two files have the same values for all fields other than the
timestamp.

@param $before
  File object to compare.
@param $after
  File object to compare.
```

## Code

```php
  function assertFileUnchanged($before, $after) {
    $this->assertEqual($before->fid, $after->fid, format_string('File id is the same: %file1 == %file2.', array('%file1' => $before->fid, '%file2' => $after->fid)), 'File unchanged');
    $this->assertEqual($before->uid, $after->uid, format_string('File owner is the same: %file1 == %file2.', array('%file1' => $before->uid, '%file2' => $after->uid)), 'File unchanged');
    $this->assertEqual($before->filename, $after->filename, format_string('File name is the same: %file1 == %file2.', array('%file1' => $before->filename, '%file2' => $after->filename)), 'File unchanged');
    $this->assertEqual($before->uri, $after->uri, format_string('File path is the same: %file1 == %file2.', array('%file1' => $before->uri, '%file2' => $after->uri)), 'File unchanged');
    $this->assertEqual($before->filemime, $after->filemime, format_string('File MIME type is the same: %file1 == %file2.', array('%file1' => $before->filemime, '%file2' => $after->filemime)), 'File unchanged');
    $this->assertEqual($before->filesize, $after->filesize, format_string('File size is the same: %file1 == %file2.', array('%file1' => $before->filesize, '%file2' => $after->filesize)), 'File unchanged');
    $this->assertEqual($before->status, $after->status, format_string('File status is the same: %file1 == %file2.', array('%file1' => $before->status, '%file2' => $after->status)), 'File unchanged');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
