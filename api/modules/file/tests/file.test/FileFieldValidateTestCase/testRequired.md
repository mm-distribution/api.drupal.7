# FileFieldValidateTestCase::testRequired()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1258–1301 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1258-L1301)
- **Class:** [FileFieldValidateTestCase](../FileFieldValidateTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function testRequired()
```

## Documentation

```text
Tests the required property on file fields.
```

## Code

```php
  function testRequired() {
    $type_name = 'article';
    $field_name = strtolower($this->randomName());
    $this->createFileField($field_name, $type_name, array(), array('required' => '1'));
    $field = field_info_field($field_name);
    $instance = field_info_instance('node', $field_name, $type_name);

    $test_file = $this->getTestFile('text');

    // Try to post a new node without uploading a file.
    $langcode = LANGUAGE_NONE;
    $edit = array("title" => $this->randomName());
    $this->drupalPost('node/add/' . $type_name, $edit, t('Save'));
    $this->assertRaw(t('!title field is required.', array('!title' => $instance['label'])), 'Node save failed when required file field was empty.');

    // Create a new node with the uploaded file.
    $nid = $this->uploadNodeFile($test_file, $field_name, $type_name);
    $this->assertTrue($nid !== FALSE, format_string('uploadNodeFile(@test_file, @field_name, @type_name) succeeded', array('@test_file' => $test_file->uri, '@field_name' => $field_name, '@type_name' => $type_name)));

    $node = node_load($nid, NULL, TRUE);

    $node_file = (object) $node->{$field_name}[LANGUAGE_NONE][0];
    $this->assertFileExists($node_file, 'File exists after uploading to the required field.');
    $this->assertFileEntryExists($node_file, 'File entry exists after uploading to the required field.');

    // Try again with a multiple value field.
    field_delete_field($field_name);
    $this->createFileField($field_name, $type_name, array('cardinality' => FIELD_CARDINALITY_UNLIMITED), array('required' => '1'));

    // Try to post a new node without uploading a file in the multivalue field.
    $edit = array('title' => $this->randomName());
    $this->drupalPost('node/add/' . $type_name, $edit, t('Save'));
    $this->assertRaw(t('!title field is required.', array('!title' => $instance['label'])), 'Node save failed when required multiple value file field was empty.');

    // Create a new node with the uploaded file into the multivalue field.
    $nid = $this->uploadNodeFile($test_file, $field_name, $type_name);
    $node = node_load($nid, NULL, TRUE);
    $node_file = (object) $node->{$field_name}[LANGUAGE_NONE][0];
    $this->assertFileExists($node_file, 'File exists after uploading to the required multiple value field.');
    $this->assertFileEntryExists($node_file, 'File entry exists after uploading to the required multipel value field.');

    // Remove our file field.
    field_delete_field($field_name);
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
