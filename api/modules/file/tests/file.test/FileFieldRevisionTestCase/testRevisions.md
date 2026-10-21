# FileFieldRevisionTestCase::testRevisions()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1044–1133 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1044-L1133)
- **Class:** [FileFieldRevisionTestCase](../FileFieldRevisionTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function testRevisions()
```

## Documentation

```text
Tests creating multiple revisions of a node and managing attached files.

Expected behaviors:
 - Adding a new revision will make another entry in the field table, but
   the original file will not be duplicated.
 - Deleting a revision should not delete the original file if the file
   is in use by another revision.
 - When the last revision that uses a file is deleted, the original file
   should be deleted also.
```

## Code

```php
  function testRevisions() {
    $type_name = 'article';
    $field_name = strtolower($this->randomName());
    $this->createFileField($field_name, $type_name);
    $field = field_info_field($field_name);
    $instance = field_info_instance('node', $field_name, $type_name);

    // Attach the same fields to users.
    $this->attachFileField($field_name, 'user', 'user');

    $test_file = $this->getTestFile('text');

    // Create a new node with the uploaded file.
    $nid = $this->uploadNodeFile($test_file, $field_name, $type_name);

    // Check that the file exists on disk and in the database.
    $node = node_load($nid, NULL, TRUE);
    $node_file_r1 = (object) $node->{$field_name}[LANGUAGE_NONE][0];
    $node_vid_r1 = $node->vid;
    $this->assertFileExists($node_file_r1, 'New file saved to disk on node creation.');
    $this->assertFileEntryExists($node_file_r1, 'File entry exists in database on node creation.');
    $this->assertFileIsPermanent($node_file_r1, 'File is permanent.');

    // Upload another file to the same node in a new revision.
    $this->replaceNodeFile($test_file, $field_name, $nid);
    $node = node_load($nid, NULL, TRUE);
    $node_file_r2 = (object) $node->{$field_name}[LANGUAGE_NONE][0];
    $node_vid_r2 = $node->vid;
    $this->assertFileExists($node_file_r2, 'Replacement file exists on disk after creating new revision.');
    $this->assertFileEntryExists($node_file_r2, 'Replacement file entry exists in database after creating new revision.');
    $this->assertFileIsPermanent($node_file_r2, 'Replacement file is permanent.');

    // Check that the original file is still in place on the first revision.
    $node = node_load($nid, $node_vid_r1, TRUE);
    $this->assertEqual($node_file_r1, (object) $node->{$field_name}[LANGUAGE_NONE][0], 'Original file still in place after replacing file in new revision.');
    $this->assertFileExists($node_file_r1, 'Original file still in place after replacing file in new revision.');
    $this->assertFileEntryExists($node_file_r1, 'Original file entry still in place after replacing file in new revision');
    $this->assertFileIsPermanent($node_file_r1, 'Original file is still permanent.');

    // Save a new version of the node without any changes.
    // Check that the file is still the same as the previous revision.
    $this->drupalPost('node/' . $nid . '/edit', array('revision' => '1'), t('Save'));
    $node = node_load($nid, NULL, TRUE);
    $node_file_r3 = (object) $node->{$field_name}[LANGUAGE_NONE][0];
    $node_vid_r3 = $node->vid;
    $this->assertEqual($node_file_r2, $node_file_r3, 'Previous revision file still in place after creating a new revision without a new file.');
    $this->assertFileIsPermanent($node_file_r3, 'New revision file is permanent.');

    // Revert to the first revision and check that the original file is active.
    $this->drupalPost('node/' . $nid . '/revisions/' . $node_vid_r1 . '/revert', array(), t('Revert'));
    $node = node_load($nid, NULL, TRUE);
    $node_file_r4 = (object) $node->{$field_name}[LANGUAGE_NONE][0];
    $node_vid_r4 = $node->vid;
    $this->assertEqual($node_file_r1, $node_file_r4, 'Original revision file still in place after reverting to the original revision.');
    $this->assertFileIsPermanent($node_file_r4, 'Original revision file still permanent after reverting to the original revision.');

    // Delete the second revision and check that the file is kept (since it is
    // still being used by the third revision).
    $this->drupalPost('node/' . $nid . '/revisions/' . $node_vid_r2 . '/delete', array(), t('Delete'));
    $this->assertFileExists($node_file_r3, 'Second file is still available after deleting second revision, since it is being used by the third revision.');
    $this->assertFileEntryExists($node_file_r3, 'Second file entry is still available after deleting second revision, since it is being used by the third revision.');
    $this->assertFileIsPermanent($node_file_r3, 'Second file entry is still permanent after deleting second revision, since it is being used by the third revision.');

    // Attach the second file to a user.
    $user = $this->drupalCreateUser();
    $edit = (array) $user;
    $edit[$field_name][LANGUAGE_NONE][0] = (array) $node_file_r3;
    user_save($user, $edit);
    $this->drupalGet('user/' . $user->uid . '/edit');

    // Delete the third revision and check that the file is not deleted yet.
    $this->drupalPost('node/' . $nid . '/revisions/' . $node_vid_r3 . '/delete', array(), t('Delete'));
    $this->assertFileExists($node_file_r3, 'Second file is still available after deleting third revision, since it is being used by the user.');
    $this->assertFileEntryExists($node_file_r3, 'Second file entry is still available after deleting third revision, since it is being used by the user.');
    $this->assertFileIsPermanent($node_file_r3, 'Second file entry is still permanent after deleting third revision, since it is being used by the user.');

    // Delete the user and check that the file is also deleted.
    user_delete($user->uid);
    // TODO: This seems like a bug in File API. Clearing the stat cache should
    // not be necessary here. The file really is deleted, but stream wrappers
    // doesn't seem to think so unless we clear the PHP file stat() cache.
    clearstatcache();
    $this->assertFileNotExists($node_file_r3, 'Second file is now deleted after deleting third revision, since it is no longer being used by any other nodes.');
    $this->assertFileEntryNotExists($node_file_r3, 'Second file entry is now deleted after deleting third revision, since it is no longer being used by any other nodes.');

    // Delete the entire node and check that the original file is deleted.
    $this->drupalPost('node/' . $nid . '/delete', array(), t('Delete'));
    $this->assertFileNotExists($node_file_r1, 'Original file is deleted after deleting the entire node with two revisions remaining.');
    $this->assertFileEntryNotExists($node_file_r1, 'Original file entry is deleted after deleting the entire node with two revisions remaining.');
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
