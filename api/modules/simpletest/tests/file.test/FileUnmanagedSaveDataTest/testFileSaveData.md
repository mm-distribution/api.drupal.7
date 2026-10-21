# FileUnmanagedSaveDataTest::testFileSaveData()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 528–543 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L528-L543)
- **Class:** [FileUnmanagedSaveDataTest](../FileUnmanagedSaveDataTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testFileSaveData()
```

## Documentation

```text
Test the file_unmanaged_save_data() function.
```

## Code

```php
  function testFileSaveData() {
    $contents = $this->randomName(8);

    // No filename.
    $filepath = file_unmanaged_save_data($contents);
    $this->assertTrue($filepath, 'Unnamed file saved correctly.');
    $this->assertEqual(file_uri_scheme($filepath), file_default_scheme(), "File was placed in Drupal's files directory.");
    $this->assertEqual($contents, file_get_contents($filepath), 'Contents of the file are correct.');

    // Provide a filename.
    $filepath = file_unmanaged_save_data($contents, 'public://asdf.txt', FILE_EXISTS_REPLACE);
    $this->assertTrue($filepath, 'Unnamed file saved correctly.');
    $this->assertEqual('asdf.txt', drupal_basename($filepath), 'File was named correctly.');
    $this->assertEqual($contents, file_get_contents($filepath), 'Contents of the file are correct.');
    $this->assertFilePermissions($filepath, variable_get('file_chmod_file', 0664));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
