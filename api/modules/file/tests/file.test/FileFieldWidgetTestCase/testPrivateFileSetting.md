# FileFieldWidgetTestCase::testPrivateFileSetting()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 909–943 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L909-L943)
- **Class:** [FileFieldWidgetTestCase](../FileFieldWidgetTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function testPrivateFileSetting()
```

## Documentation

```text
Tests a file field with a "Private files" upload destination setting.
```

## Code

```php
  function testPrivateFileSetting() {
    // Use 'page' instead of 'article', so that the 'article' image field does
    // not conflict with this test. If in the future the 'page' type gets its
    // own default file or image field, this test can be made more robust by
    // using a custom node type.
    $type_name = 'page';
    $field_name = strtolower($this->randomName());
    $this->createFileField($field_name, $type_name);
    $field = field_info_field($field_name);
    $instance = field_info_instance('node', $field_name, $type_name);

    $test_file = $this->getTestFile('text');

    // Change the field setting to make its files private, and upload a file.
    $edit = array('field[settings][uri_scheme]' => 'private');
    $this->drupalPost("admin/structure/types/manage/$type_name/fields/$field_name", $edit, t('Save settings'));
    $nid = $this->uploadNodeFile($test_file, $field_name, $type_name);
    $node = node_load($nid, NULL, TRUE);
    $node_file = (object) $node->{$field_name}[LANGUAGE_NONE][0];
    $this->assertFileExists($node_file, 'New file saved to disk on node creation.');

    // Ensure the private file is available to the user who uploaded it.
    $this->drupalGet(file_create_url($node_file->uri));
    $this->assertResponse(200, 'Confirmed that the generated URL is correct by downloading the shipped file.');

    // Ensure we can't change 'uri_scheme' field settings while there are some
    // entities with uploaded files.
    $this->drupalGet("admin/structure/types/manage/$type_name/fields/$field_name");
    $this->assertFieldByXpath('//input[@id="edit-field-settings-uri-scheme-public" and @disabled="disabled"]', 'public', 'Upload destination setting disabled.');

    // Delete node and confirm that setting could be changed.
    node_delete($nid);
    $this->drupalGet("admin/structure/types/manage/$type_name/fields/$field_name");
    $this->assertFieldByXpath('//input[@id="edit-field-settings-uri-scheme-public" and not(@disabled)]', 'public', 'Upload destination setting enabled.');
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
