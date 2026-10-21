# FileSaveTest::testFileSave()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2203–2257 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2203-L2257)
- **Class:** [FileSaveTest](../FileSaveTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testFileSave()
```

## Documentation

_No docblock in source._

## Code

```php
  function testFileSave() {
    // Create a new file object.
    $file = array(
      'uid' => 1,
      'filename' => 'druplicon.txt',
      'uri' => 'public://druplicon.txt',
      'filemime' => 'text/plain',
      'timestamp' => 1,
      'status' => FILE_STATUS_PERMANENT,
    );
    $file = (object) $file;
    file_put_contents($file->uri, 'hello world');

    // Save it, inserting a new record.
    $saved_file = file_save($file);

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('insert'));

    $this->assertNotNull($saved_file, 'Saving the file should give us back a file object.', 'File');
    $this->assertTrue($saved_file->fid > 0, 'A new file ID is set when saving a new file to the database.', 'File');
    $loaded_file = db_query('SELECT * FROM {file_managed} f WHERE f.fid = :fid', array(':fid' => $saved_file->fid))->fetch(PDO::FETCH_OBJ);
    $this->assertNotNull($loaded_file, 'Record exists in the database.');
    $this->assertEqual($loaded_file->status, $file->status, 'Status was saved correctly.');
    $this->assertEqual($saved_file->filesize, filesize($file->uri), 'File size was set correctly.', 'File');
    $this->assertTrue($saved_file->timestamp > 1, 'File size was set correctly.', 'File');


    // Resave the file, updating the existing record.
    file_test_reset();
    $saved_file->status = 7;
    $resaved_file = file_save($saved_file);

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('load', 'update'));

    $this->assertEqual($resaved_file->fid, $saved_file->fid, 'The file ID of an existing file is not changed when updating the database.', 'File');
    $this->assertTrue($resaved_file->timestamp >= $saved_file->timestamp, "Timestamp didn't go backwards.", 'File');
    $loaded_file = db_query('SELECT * FROM {file_managed} f WHERE f.fid = :fid', array(':fid' => $saved_file->fid))->fetch(PDO::FETCH_OBJ);
    $this->assertNotNull($loaded_file, 'Record still exists in the database.', 'File');
    $this->assertEqual($loaded_file->status, $saved_file->status, 'Status was saved correctly.');

    // Try to insert a second file with the same name apart from case insensitivity
    // to ensure the 'uri' index allows for filenames with different cases.
    $file = (object) array(
      'uid' => 1,
      'filename' => 'DRUPLICON.txt',
      'uri' => 'public://DRUPLICON.txt',
      'filemime' => 'text/plain',
      'timestamp' => 1,
      'status' => FILE_STATUS_PERMANENT,
    );
    file_put_contents($file->uri, 'hello world');
    file_save($file);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
