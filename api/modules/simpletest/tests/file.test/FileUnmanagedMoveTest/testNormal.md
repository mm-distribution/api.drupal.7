# FileUnmanagedMoveTest::testNormal()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1569–1595 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1569-L1595)
- **Class:** [FileUnmanagedMoveTest](../FileUnmanagedMoveTest.md)
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
    // Create a file for testing
    $file = $this->createFile();

    // Moving to a new name.
    $desired_filepath = 'public://' . $this->randomName();
    $new_filepath = file_unmanaged_move($file->uri, $desired_filepath, FILE_EXISTS_ERROR);
    $this->assertTrue($new_filepath, 'Move was successful.');
    $this->assertEqual($new_filepath, $desired_filepath, 'Returned expected filepath.');
    $this->assertTrue(file_exists($new_filepath), 'File exists at the new location.');
    $this->assertFalse(file_exists($file->uri), 'No file remains at the old location.');
    $this->assertFilePermissions($new_filepath, variable_get('file_chmod_file', 0664));

    // Moving with rename.
    $desired_filepath = 'public://' . $this->randomName();
    $this->assertTrue(file_exists($new_filepath), 'File exists before moving.');
    $this->assertTrue(file_put_contents($desired_filepath, ' '), 'Created a file so a rename will have to happen.');
    $newer_filepath = file_unmanaged_move($new_filepath, $desired_filepath, FILE_EXISTS_RENAME);
    $this->assertTrue($newer_filepath, 'Move was successful.');
    $this->assertNotEqual($newer_filepath, $desired_filepath, 'Returned expected filepath.');
    $this->assertTrue(file_exists($newer_filepath), 'File exists at the new location.');
    $this->assertFalse(file_exists($new_filepath), 'No file remains at the old location.');
    $this->assertFilePermissions($newer_filepath, variable_get('file_chmod_file', 0664));

    // TODO: test moving to a directory (rather than full directory/file path)
    // TODO: test creating and moving normal files (rather than streams)
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
