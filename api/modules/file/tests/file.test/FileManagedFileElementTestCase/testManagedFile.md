# FileManagedFileElementTestCase::testManagedFile()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 403–491 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L403-L491)
- **Class:** [FileManagedFileElementTestCase](../FileManagedFileElementTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function testManagedFile()
```

## Documentation

```text
Tests the managed_file element type.
```

## Code

```php
  function testManagedFile() {
    // Check that $element['#size'] is passed to the child upload element.
    $this->drupalGet('file/test');
    $this->assertFieldByXpath('//input[@name="files[nested_file]" and @size="13"]', NULL, 'The custom #size attribute is passed to the child upload element.');

    // Check that the file fields don't contain duplicate HTML IDs.
    $this->assertNoDuplicateIds('There are no duplicate IDs');

    // Perform the tests with all permutations of $form['#tree'] and
    // $element['#extended'].
    foreach (array(0, 1) as $tree) {
      foreach (array(0, 1) as $extended) {
        $test_file = $this->getTestFile('text');
        $path = 'file/test/' . $tree . '/' . $extended;
        $input_base_name = $tree ? 'nested_file' : 'file';

        // Submit without a file.
        $this->drupalPost($path, array(), t('Save'));
        $this->assertRaw(t('The file id is %fid.', array('%fid' => 0)), 'Submitted without a file.');

        // Submit with a file, but with an invalid form token. Ensure the file
        // was not saved.
        $last_fid_prior = $this->getLastFileId();
        $edit = array(
          'files[' . $input_base_name . ']' => drupal_realpath($test_file->uri),
          'form_token' => 'invalid token',
        );
        $this->drupalPost($path, $edit, t('Save'));
        $this->assertText('The form has become outdated.');
        $last_fid = $this->getLastFileId();
        $this->assertEqual($last_fid_prior, $last_fid, 'File was not saved when uploaded with an invalid form token.');

        // Submit a new file, without using the Upload button.
        $last_fid_prior = $this->getLastFileId();
        $edit = array('files[' . $input_base_name . ']' => drupal_realpath($test_file->uri));
        $this->drupalPost($path, $edit, t('Save'));
        $last_fid = $this->getLastFileId();
        $this->assertTrue($last_fid > $last_fid_prior, 'New file got saved.');
        $this->assertRaw(t('The file id is %fid.', array('%fid' => $last_fid)), 'Submit handler has correct file info.');

        // Submit no new input, but with a default file.
        $this->drupalPost($path . '/' . $last_fid, array(), t('Save'));
        $this->assertRaw(t('The file id is %fid.', array('%fid' => $last_fid)), 'Empty submission did not change an existing file.');

        // Now, test the Upload and Remove buttons, with and without Ajax.
        foreach (array(FALSE, TRUE) as $ajax) {
          // Upload, then Submit.
          $last_fid_prior = $this->getLastFileId();
          $this->drupalGet($path);
          $edit = array('files[' . $input_base_name . ']' => drupal_realpath($test_file->uri));
          if ($ajax) {
            $this->drupalPostAJAX(NULL, $edit, $input_base_name . '_upload_button');
          }
          else {
            $this->drupalPost(NULL, $edit, t('Upload'));
          }
          $last_fid = $this->getLastFileId();
          $this->assertTrue($last_fid > $last_fid_prior, 'New file got uploaded.');
          $this->drupalPost(NULL, array(), t('Save'));
          $this->assertRaw(t('The file id is %fid.', array('%fid' => $last_fid)), 'Submit handler has correct file info.');

          // Remove, then Submit.
          $this->drupalGet($path . '/' . $last_fid);
          if ($ajax) {
            $this->drupalPostAJAX(NULL, array(), $input_base_name . '_remove_button');
          }
          else {
            $this->drupalPost(NULL, array(), t('Remove'));
          }
          $this->drupalPost(NULL, array(), t('Save'));
          $this->assertRaw(t('The file id is %fid.', array('%fid' => 0)), 'Submission after file removal was successful.');

          // Upload, then Remove, then Submit.
          $this->drupalGet($path);
          $edit = array('files[' . $input_base_name . ']' => drupal_realpath($test_file->uri));
          if ($ajax) {
            $this->drupalPostAJAX(NULL, $edit, $input_base_name . '_upload_button');
            $this->drupalPostAJAX(NULL, array(), $input_base_name . '_remove_button');
          }
          else {
            $this->drupalPost(NULL, $edit, t('Upload'));
            $this->drupalPost(NULL, array(), t('Remove'));
          }
          $this->drupalPost(NULL, array(), t('Save'));
          $this->assertRaw(t('The file id is %fid.', array('%fid' => 0)), 'Submission after file upload and removal was successful.');
        }
      }
    }
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
