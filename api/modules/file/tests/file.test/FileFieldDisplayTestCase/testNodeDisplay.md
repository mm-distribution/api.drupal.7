# FileFieldDisplayTestCase::testNodeDisplay()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1151–1209 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1151-L1209)
- **Class:** [FileFieldDisplayTestCase](../FileFieldDisplayTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function testNodeDisplay()
```

## Documentation

```text
Tests normal formatter display on node display.
```

## Code

```php
  function testNodeDisplay() {
    $field_name = strtolower($this->randomName());
    $type_name = 'article';
    $field_settings = array(
      'display_field' => '1',
      'display_default' => '1',
      'cardinality' => FIELD_CARDINALITY_UNLIMITED,
    );
    $instance_settings = array(
      'description_field' => '1',
    );
    $widget_settings = array();
    $this->createFileField($field_name, $type_name, $field_settings, $instance_settings, $widget_settings);
    $field = field_info_field($field_name);
    $instance = field_info_instance('node', $field_name, $type_name);

    // Create a new node *without* the file field set, and check that the field
    // is not shown for each node display.
    $node = $this->drupalCreateNode(array('type' => $type_name));
    $file_formatters = array('file_default', 'file_table', 'file_url_plain', 'hidden');
    foreach ($file_formatters as $formatter) {
      $edit = array(
        "fields[$field_name][type]" => $formatter,
      );
      $this->drupalPost("admin/structure/types/manage/$type_name/display", $edit, t('Save'));
      $this->drupalGet('node/' . $node->nid);
      $this->assertNoText($field_name, format_string('Field label is hidden when no file attached for formatter %formatter', array('%formatter' => $formatter)));
    }

    $test_file = $this->getTestFile('text');

    // Create a new node with the uploaded file.
    $nid = $this->uploadNodeFile($test_file, $field_name, $type_name);
    $this->drupalGet('node/' . $nid . '/edit');

    // Check that the default formatter is displaying with the file name.
    $node = node_load($nid, NULL, TRUE);
    $node_file = (object) $node->{$field_name}[LANGUAGE_NONE][0];
    $default_output = theme('file_link', array('file' => $node_file));
    $this->assertRaw($default_output, 'Default formatter displaying correctly on full node view.');

    // Turn the "display" option off and check that the file is no longer displayed.
    $edit = array($field_name . '[' . LANGUAGE_NONE . '][0][display]' => FALSE);
    $this->drupalPost('node/' . $nid . '/edit', $edit, t('Save'));

    $this->assertNoRaw($default_output, 'Field is hidden when "display" option is unchecked.');

    // Test that fields appear as expected during the preview.
    // Add a second file.
    $name = 'files[' . $field_name . '_' . LANGUAGE_NONE . '_1]';
    $edit[$name] = drupal_realpath($test_file->uri);

    // Uncheck the display checkboxes and go to the preview.
    $edit[$field_name . '[' . LANGUAGE_NONE . '][0][display]'] = FALSE;
    $edit[$field_name . '[' . LANGUAGE_NONE . '][1][display]'] = FALSE;
    $this->drupalPost('node/' . $nid . '/edit', $edit, t('Preview'));
    $this->assertRaw($field_name . '[' . LANGUAGE_NONE . '][0][display]', 'First file appears as expected.');
    $this->assertRaw($field_name . '[' . LANGUAGE_NONE . '][1][display]', 'Second file appears as expected.');
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
