# FileFieldWidgetTestCase::testSingleValuedWidget()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 546–607 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L546-L607)
- **Class:** [FileFieldWidgetTestCase](../FileFieldWidgetTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function testSingleValuedWidget()
```

## Documentation

```text
Tests upload and remove buttons for a single-valued File field.
```

## Code

```php
  function testSingleValuedWidget() {
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

    foreach (array('nojs', 'js') as $type) {
      // Create a new node with the uploaded file and ensure it got uploaded
      // successfully.
      // @todo This only tests a 'nojs' submission, because drupalPostAJAX()
      //   does not yet support file uploads.
      $nid = $this->uploadNodeFile($test_file, $field_name, $type_name);
      $node = node_load($nid, NULL, TRUE);
      $node_file = (object) $node->{$field_name}[LANGUAGE_NONE][0];
      $this->assertFileExists($node_file, 'New file saved to disk on node creation.');

      // Test that running field_attach_update() leaves the file intact.
      $field = new stdClass();
      $field->type = $type_name;
      $field->nid = $nid;
      field_attach_update('node', $field);
      $node = node_load($nid);
      $node_file = (object) $node->{$field_name}[LANGUAGE_NONE][0];
      $this->assertFileExists($node_file, 'New file still saved to disk on field update.');

      // Ensure the file can be downloaded.
      $this->drupalGet(file_create_url($node_file->uri));
      $this->assertResponse(200, 'Confirmed that the generated URL is correct by downloading the shipped file.');

      // Ensure the edit page has a remove button instead of an upload button.
      $this->drupalGet("node/$nid/edit");
      $this->assertNoFieldByXPath('//input[@type="submit"]', t('Upload'), 'Node with file does not display the "Upload" button.');
      $this->assertFieldByXpath('//input[@type="submit"]', t('Remove'), 'Node with file displays the "Remove" button.');

      // "Click" the remove button (emulating either a nojs or js submission).
      switch ($type) {
        case 'nojs':
          $this->drupalPost(NULL, array(), t('Remove'));
          break;
        case 'js':
          $button = $this->xpath('//input[@type="submit" and @value="' . t('Remove') . '"]');
          $this->drupalPostAJAX(NULL, array(), array((string) $button[0]['name'] => (string) $button[0]['value']));
          break;
      }

      // Ensure the page now has an upload button instead of a remove button.
      $this->assertNoFieldByXPath('//input[@type="submit"]', t('Remove'), 'After clicking the "Remove" button, it is no longer displayed.');
      $this->assertFieldByXpath('//input[@type="submit"]', t('Upload'), 'After clicking the "Remove" button, the "Upload" button is displayed.');

      // Save the node and ensure it does not have the file.
      $this->drupalPost(NULL, array(), t('Save'));
      $node = node_load($nid, NULL, TRUE);
      $this->assertTrue(empty($node->{$field_name}[LANGUAGE_NONE][0]['fid']), 'File was successfully removed from the node.');
    }
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
