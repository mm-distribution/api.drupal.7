# FileFieldValidateTestCase::testFileMaxSize()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1306–1353 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1306-L1353)
- **Class:** [FileFieldValidateTestCase](../FileFieldValidateTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function testFileMaxSize()
```

## Documentation

```text
Tests the max file size validator.
```

## Code

```php
  function testFileMaxSize() {
    $type_name = 'article';
    $field_name = strtolower($this->randomName());
    $this->createFileField($field_name, $type_name, array(), array('required' => '1'));
    $field = field_info_field($field_name);
    $instance = field_info_instance('node', $field_name, $type_name);

    $small_file = $this->getTestFile('text', 131072); // 128KB.
    $large_file = $this->getTestFile('text', 1310720); // 1.2MB

    // Test uploading both a large and small file with different increments.
    $sizes = array(
      '1M' => 1048576,
      '1024K' => 1048576,
      '1048576' => 1048576,
    );

    foreach ($sizes as $max_filesize => $file_limit) {
      // Set the max file upload size.
      $this->updateFileField($field_name, $type_name, array('max_filesize' => $max_filesize));
      $instance = field_info_instance('node', $field_name, $type_name);

      // Create a new node with the small file, which should pass.
      $nid = $this->uploadNodeFile($small_file, $field_name, $type_name);
      $node = node_load($nid, NULL, TRUE);
      $node_file = (object) $node->{$field_name}[LANGUAGE_NONE][0];
      $this->assertFileExists($node_file, format_string('File exists after uploading a file (%filesize) under the max limit (%maxsize).', array('%filesize' => format_size($small_file->filesize), '%maxsize' => $max_filesize)));
      $this->assertFileEntryExists($node_file, format_string('File entry exists after uploading a file (%filesize) under the max limit (%maxsize).', array('%filesize' => format_size($small_file->filesize), '%maxsize' => $max_filesize)));

      // Check that uploading the large file fails (1M limit).
      $nid = $this->uploadNodeFile($large_file, $field_name, $type_name);
      $error_message = t('The file is %filesize exceeding the maximum file size of %maxsize.', array('%filesize' => format_size($large_file->filesize), '%maxsize' => format_size($file_limit)));
      $this->assertRaw($error_message, format_string('Node save failed when file (%filesize) exceeded the max upload size (%maxsize).', array('%filesize' => format_size($large_file->filesize), '%maxsize' => $max_filesize)));
    }

    // Turn off the max filesize.
    $this->updateFileField($field_name, $type_name, array('max_filesize' => ''));

    // Upload the big file successfully.
    $nid = $this->uploadNodeFile($large_file, $field_name, $type_name);
    $node = node_load($nid, NULL, TRUE);
    $node_file = (object) $node->{$field_name}[LANGUAGE_NONE][0];
    $this->assertFileExists($node_file, format_string('File exists after uploading a file (%filesize) with no max limit.', array('%filesize' => format_size($large_file->filesize))));
    $this->assertFileEntryExists($node_file, format_string('File entry exists after uploading a file (%filesize) with no max limit.', array('%filesize' => format_size($large_file->filesize))));

    // Remove our file field.
    field_delete_field($field_name);
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
