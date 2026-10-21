# FileFieldWidgetTestCase::testWidgetValidation()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 658–703 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L658-L703)
- **Class:** [FileFieldWidgetTestCase](../FileFieldWidgetTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function testWidgetValidation()
```

## Documentation

```text
Tests validation with the Upload button.
```

## Code

```php
  function testWidgetValidation() {
    $type_name = 'article';
    $field_name = strtolower($this->randomName());
    $this->createFileField($field_name, $type_name);
    $this->updateFileField($field_name, $type_name, array('file_extensions' => 'txt'));

    foreach (array('nojs', 'js') as $type) {
      // Create node and prepare files for upload.
      $node = $this->drupalCreateNode(array('type' => 'article'));
      $nid = $node->nid;
      $this->drupalGet("node/$nid/edit");
      $test_file_text = $this->getTestFile('text');
      $test_file_image = $this->getTestFile('image');
      $field = field_info_field($field_name);
      $name = 'files[' . $field_name . '_' . LANGUAGE_NONE . '_0]';

      // Upload file with incorrect extension, check for validation error.
      $edit[$name] = drupal_realpath($test_file_image->uri);
      switch ($type) {
        case 'nojs':
          $this->drupalPost(NULL, $edit, t('Upload'));
          break;

        case 'js':
          $button = $this->xpath('//input[@type="submit" and @value="' . t('Upload') . '"]');
          $this->drupalPostAJAX(NULL, $edit, array((string) $button[0]['name'] => (string) $button[0]['value']));
          break;
      }
      $error_message = t('Only files with the following extensions are allowed: %files-allowed.', array('%files-allowed' => 'txt'));
      $this->assertRaw($error_message, t('Validation error when file with wrong extension uploaded (JSMode=%type).', array('%type' => $type)));

      // Upload file with correct extension, check that error message is removed.
      $edit[$name] = drupal_realpath($test_file_text->uri);
      switch ($type) {
        case 'nojs':
          $this->drupalPost(NULL, $edit, t('Upload'));
          break;

        case 'js':
          $button = $this->xpath('//input[@type="submit" and @value="' . t('Upload') . '"]');
          $this->drupalPostAJAX(NULL, $edit, array((string) $button[0]['name'] => (string) $button[0]['value']));
          break;
      }
      $this->assertNoRaw($error_message, t('Validation error removed when file with correct extension uploaded (JSMode=%type).', array('%type' => $type)));
    }
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
