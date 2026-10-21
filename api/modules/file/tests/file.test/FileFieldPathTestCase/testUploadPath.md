# FileFieldPathTestCase::testUploadPath()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1416–1457 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1416-L1457)
- **Class:** [FileFieldPathTestCase](../FileFieldPathTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function testUploadPath()
```

## Documentation

```text
Tests the normal formatter display on node display.
```

## Code

```php
  function testUploadPath() {
    $field_name = strtolower($this->randomName());
    $type_name = 'article';
    $field = $this->createFileField($field_name, $type_name);
    $test_file = $this->getTestFile('text');

    // Create a new node.
    $nid = $this->uploadNodeFile($test_file, $field_name, $type_name);

    // Check that the file was uploaded to the correct location.
    $node = node_load($nid, NULL, TRUE);
    $node_file = (object) $node->{$field_name}[LANGUAGE_NONE][0];
    $expected_path = 'public://' . date('Y', REQUEST_TIME) . '-' . date('m', REQUEST_TIME) . '/' . $test_file->filename;
    $this->assertPathMatch($expected_path, $node_file->uri, format_string('The file %file was uploaded to the correct path.', array('%file' => $node_file->uri)));

    // Change the path to contain multiple subdirectories.
    $field = $this->updateFileField($field_name, $type_name, array('file_directory' => 'foo/bar/baz'));

    // Upload a new file into the subdirectories.
    $nid = $this->uploadNodeFile($test_file, $field_name, $type_name);

    // Check that the file was uploaded into the subdirectory.
    $node = node_load($nid, NULL, TRUE);
    $node_file = (object) $node->{$field_name}[LANGUAGE_NONE][0];
    $this->assertPathMatch('public://foo/bar/baz/' . $test_file->filename, $node_file->uri, format_string('The file %file was uploaded to the correct path.', array('%file' => $node_file->uri)));

    // Check the path when used with tokens.
    // Change the path to contain multiple token directories.
    $field = $this->updateFileField($field_name, $type_name, array('file_directory' => '[current-user:uid]/[current-user:name]'));

    // Upload a new file into the token subdirectories.
    $nid = $this->uploadNodeFile($test_file, $field_name, $type_name);

    // Check that the file was uploaded into the subdirectory.
    $node = node_load($nid, NULL, TRUE);
    $node_file = (object) $node->{$field_name}[LANGUAGE_NONE][0];
    // Do token replacement using the same user which uploaded the file, not
    // the user running the test case.
    $data = array('user' => $this->admin_user);
    $subdirectory = token_replace('[user:uid]/[user:name]', $data);
    $this->assertPathMatch('public://' . $subdirectory . '/' . $test_file->filename, $node_file->uri, format_string('The file %file was uploaded to the correct path with token replacements.', array('%file' => $node_file->uri)));
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
