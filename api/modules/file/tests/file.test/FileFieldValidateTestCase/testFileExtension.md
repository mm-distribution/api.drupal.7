# FileFieldValidateTestCase::testFileExtension()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1358–1398 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1358-L1398)
- **Class:** [FileFieldValidateTestCase](../FileFieldValidateTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function testFileExtension()
```

## Documentation

```text
Tests file extension checking.
```

## Code

```php
  function testFileExtension() {
    $type_name = 'article';
    $field_name = strtolower($this->randomName());
    $this->createFileField($field_name, $type_name);
    $field = field_info_field($field_name);
    $instance = field_info_instance('node', $field_name, $type_name);

    $test_file = $this->getTestFile('image');
    list(, $test_file_extension) = explode('.', $test_file->filename);

    // Disable extension checking.
    $this->updateFileField($field_name, $type_name, array('file_extensions' => ''));

    // Check that the file can be uploaded with no extension checking.
    $nid = $this->uploadNodeFile($test_file, $field_name, $type_name);
    $node = node_load($nid, NULL, TRUE);
    $node_file = (object) $node->{$field_name}[LANGUAGE_NONE][0];
    $this->assertFileExists($node_file, 'File exists after uploading a file with no extension checking.');
    $this->assertFileEntryExists($node_file, 'File entry exists after uploading a file with no extension checking.');

    // Enable extension checking for text files.
    $this->updateFileField($field_name, $type_name, array('file_extensions' => 'txt'));

    // Check that the file with the wrong extension cannot be uploaded.
    $nid = $this->uploadNodeFile($test_file, $field_name, $type_name);
    $error_message = t('Only files with the following extensions are allowed: %files-allowed.', array('%files-allowed' => 'txt'));
    $this->assertRaw($error_message, 'Node save failed when file uploaded with the wrong extension.');

    // Enable extension checking for text and image files.
    $this->updateFileField($field_name, $type_name, array('file_extensions' => "txt $test_file_extension"));

    // Check that the file can be uploaded with extension checking.
    $nid = $this->uploadNodeFile($test_file, $field_name, $type_name);
    $node = node_load($nid, NULL, TRUE);
    $node_file = (object) $node->{$field_name}[LANGUAGE_NONE][0];
    $this->assertFileExists($node_file, 'File exists after uploading a file with extension checking.');
    $this->assertFileEntryExists($node_file, 'File entry exists after uploading a file with extension checking.');

    // Remove our file field.
    field_delete_field($field_name);
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
