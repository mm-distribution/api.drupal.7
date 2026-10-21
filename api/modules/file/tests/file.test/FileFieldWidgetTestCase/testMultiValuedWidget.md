# FileFieldWidgetTestCase::testMultiValuedWidget()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 776–904 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L776-L904)
- **Class:** [FileFieldWidgetTestCase](../FileFieldWidgetTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function testMultiValuedWidget()
```

## Documentation

```text
Tests upload and remove buttons for multiple multi-valued File fields.
```

## Code

```php
  function testMultiValuedWidget() {
    // Use 'page' instead of 'article', so that the 'article' image field does
    // not conflict with this test. If in the future the 'page' type gets its
    // own default file or image field, this test can be made more robust by
    // using a custom node type.
    $type_name = 'page';
    $field_name = strtolower($this->randomName());
    $field_name2 = strtolower($this->randomName());
    $this->createFileField($field_name, $type_name, array('cardinality' => 3));
    $this->createFileField($field_name2, $type_name, array('cardinality' => 3));

    $field = field_info_field($field_name);
    $instance = field_info_instance('node', $field_name, $type_name);

    $field2 = field_info_field($field_name2);
    $instance2 = field_info_instance('node', $field_name2, $type_name);

    $test_file = $this->getTestFile('text');

    foreach (array('nojs', 'js') as $type) {
      // Visit the node creation form, and upload 3 files for each field. Since
      // the field has cardinality of 3, ensure the "Upload" button is displayed
      // until after the 3rd file, and after that, isn't displayed. Because
      // SimpleTest triggers the last button with a given name, so upload to the
      // second field first.
      // @todo This is only testing a non-Ajax upload, because drupalPostAJAX()
      //   does not yet emulate jQuery's file upload.
      //
      $this->drupalGet("node/add/$type_name");
      foreach (array($field_name2, $field_name) as $each_field_name) {
        for ($delta = 0; $delta < 3; $delta++) {
          $edit = array('files[' . $each_field_name . '_' . LANGUAGE_NONE . '_' . $delta . ']' => drupal_realpath($test_file->uri));
          // drupalPost() takes a $submit parameter that is the value of the
          // button whose click we want to emulate. Since we have multiple
          // buttons with the value "Upload", and want to control which one we
          // use, we change the value of the other ones to something else.
          // Since non-clicked buttons aren't included in the submitted POST
          // data, and since drupalPost() will result in $this being updated
          // with a newly rebuilt form, this doesn't cause problems. Note that
          // $buttons is an array of SimpleXMLElement objects passed by
          // reference so modifications to each button will affect
          // \DrupalWebTestCase::handleForm().
          $buttons = $this->xpath('//input[@type="submit" and @value="Upload"]');
          $button_name = $each_field_name . '_' . LANGUAGE_NONE . '_' . $delta . '_upload_button';
          foreach ($buttons as $button) {
            if ($button['name'] != $button_name) {
              $button['value'] = 'DUMMY';
            }
          }
          // If the Upload button doesn't exist, drupalPost() will automatically
          // fail with an assertion message.
          $this->drupalPost(NULL, $edit, t('Upload'));
        }
      }
      $this->assertNoFieldByXpath('//input[@type="submit"]', t('Upload'), 'After uploading 3 files for each field, the "Upload" button is no longer displayed.');

      $num_expected_remove_buttons = 6;

      foreach (array($field_name, $field_name2) as $current_field_name) {
        // How many uploaded files for the current field are remaining.
        $remaining = 3;
        // Test clicking each "Remove" button. For extra robustness, test them out
        // of sequential order. They are 0-indexed, and get renumbered after each
        // iteration, so array(1, 1, 0) means:
        // - First remove the 2nd file.
        // - Then remove what is then the 2nd file (was originally the 3rd file).
        // - Then remove the first file.
        foreach (array(1,1,0) as $delta) {
          // Ensure we have the expected number of Remove buttons, and that they
          // are numbered sequentially.
          $buttons = $this->xpath('//input[@type="submit" and @value="Remove"]');
          $this->assertTrue(is_array($buttons) && count($buttons) === $num_expected_remove_buttons, format_string('There are %n "Remove" buttons displayed (JSMode=%type).', array('%n' => $num_expected_remove_buttons, '%type' => $type)));
          foreach ($buttons as $i => $button) {
            $key = $i >= $remaining ? $i - $remaining : $i;
            $check_field_name = $field_name2;
            if ($current_field_name == $field_name && $i < $remaining) {
              $check_field_name = $field_name;
            }

            $this->assertIdentical((string) $button['name'], $check_field_name . '_' . LANGUAGE_NONE . '_' . $key. '_remove_button');
          }

          // "Click" the remove button (emulating either a nojs or js submission).
          $button_name = $current_field_name . '_' . LANGUAGE_NONE . '_' . $delta . '_remove_button';
          switch ($type) {
            case 'nojs':
              // Same workaround for multiple buttons with the value "Remove" as
              // we did for the "Upload" buttons above.
              foreach ($buttons as $button) {
                if ($button['name'] != $button_name) {
                  $button['value'] = 'DUMMY';
                }
              }
              $this->drupalPost(NULL, array(), t('Remove'));
              break;
            case 'js':
              // drupalPostAJAX() lets us target the button precisely, so we don't
              // require the workaround used above for nojs.
              $this->drupalPostAJAX(NULL, array(), array($button_name => t('Remove')));
              break;
          }
          $num_expected_remove_buttons--;
          $remaining--;

          // Ensure an "Upload" button for the current field is displayed with the
          // correct name.
          $upload_button_name = $current_field_name . '_' . LANGUAGE_NONE . '_' . $remaining . '_upload_button';
          $buttons = $this->xpath('//input[@type="submit" and @value="Upload" and @name=:name]', array(':name' => $upload_button_name));
          $this->assertTrue(is_array($buttons) && count($buttons) == 1, format_string('The upload button is displayed with the correct name (JSMode=%type).', array('%type' => $type)));

          // Ensure only at most one button per field is displayed.
          $buttons = $this->xpath('//input[@type="submit" and @value="Upload"]');
          $expected = $current_field_name == $field_name ? 1 : 2;
          $this->assertTrue(is_array($buttons) && count($buttons) == $expected, format_string('After removing a file, only one "Upload" button for each possible field is displayed (JSMode=%type).', array('%type' => $type)));
        }
      }

      // Ensure the page now has no Remove buttons.
      $this->assertNoFieldByXPath('//input[@type="submit"]', t('Remove'), format_string('After removing all files, there is no "Remove" button displayed (JSMode=%type).', array('%type' => $type)));

      // Save the node and ensure it does not have any files.
      $this->drupalPost(NULL, array('title' => $this->randomName()), t('Save'));
      $matches = array();
      preg_match('/node\/([0-9]+)/', $this->getUrl(), $matches);
      $nid = $matches[1];
      $node = node_load($nid, NULL, TRUE);
      $this->assertTrue(empty($node->{$field_name}[LANGUAGE_NONE][0]['fid']), 'Node was successfully saved without any files.');
    }
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
