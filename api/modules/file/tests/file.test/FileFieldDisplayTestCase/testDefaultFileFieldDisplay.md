# FileFieldDisplayTestCase::testDefaultFileFieldDisplay()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1214–1237 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1214-L1237)
- **Class:** [FileFieldDisplayTestCase](../FileFieldDisplayTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function testDefaultFileFieldDisplay()
```

## Documentation

```text
Tests default display of File Field.
```

## Code

```php
  function testDefaultFileFieldDisplay() {
    $field_name = strtolower($this->randomName());
    $type_name = 'article';
    $field_settings = array(
      'display_field' => '1',
      'display_default' => '0',
    );
    $instance_settings = array(
      'description_field' => '1',
    );
    $widget_settings = array();
    $this->createFileField($field_name, $type_name, $field_settings, $instance_settings, $widget_settings);
    $field = field_info_field($field_name);
    $instance = field_info_instance('node', $field_name, $type_name);

    $test_file = $this->getTestFile('text');

    // Create a new node with the uploaded file.
    $nid = $this->uploadNodeFile($test_file, $field_name, $type_name);

    $this->drupalGet('node/' . $nid . '/edit');
    $this->assertFieldByXPath('//input[@type="checkbox" and @name="' . $field_name . '[und][0][display]"]', NULL, 'Default file display checkbox field exists.');
    $this->assertFieldByXPath('//input[@type="checkbox" and @name="' . $field_name . '[und][0][display]" and not(@checked)]', NULL, 'Default file display is off.');
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
