# FileMoveTest::testNormal()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1816–1841 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1816-L1841)
- **Class:** [FileMoveTest](../FileMoveTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testNormal()
```

## Documentation

```text
Move a normal file.
```

## Code

```php
  function testNormal() {
    $contents = $this->randomName(10);
    $source = $this->createFile(NULL, $contents);
    $desired_filepath = 'public://' . $this->randomName();

    // Clone the object so we don't have to worry about the function changing
    // our reference copy.
    $result = file_move(clone $source, $desired_filepath, FILE_EXISTS_ERROR);

    // Check the return status and that the contents changed.
    $this->assertTrue($result, 'File moved successfully.');
    $this->assertFalse(file_exists($source->uri));
    $this->assertEqual($contents, file_get_contents($result->uri), 'Contents of file correctly written.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('move', 'load', 'update'));

    // Make sure we got the same file back.
    $this->assertEqual($source->fid, $result->fid, format_string("Source file id's' %fid is unchanged after move.", array('%fid' => $source->fid)));

    // Reload the file from the database and check that the changes were
    // actually saved.
    $loaded_file = file_load($result->fid, TRUE);
    $this->assertTrue($loaded_file, 'File can be loaded from the database.');
    $this->assertFileUnchanged($result, $loaded_file);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
