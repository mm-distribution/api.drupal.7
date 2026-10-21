# FilePrivateTestCase::testPrivateFile()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1578–1697 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1578-L1697)
- **Class:** [FilePrivateTestCase](../FilePrivateTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function testPrivateFile()
```

## Documentation

```text
Tests file access for file uploaded to a private node.
```

## Code

```php
  function testPrivateFile() {
    // Use 'page' instead of 'article', so that the 'article' image field does
    // not conflict with this test. If in the future the 'page' type gets its
    // own default file or image field, this test can be made more robust by
    // using a custom node type.
    $type_name = 'page';
    $field_name = strtolower($this->randomName());
    $this->createFileField($field_name, $type_name, array('uri_scheme' => 'private'));

    // Create a field with no view access - see field_test_field_access().
    $no_access_field_name = 'field_no_view_access';
    $this->createFileField($no_access_field_name, $type_name, array('uri_scheme' => 'private'));

    $test_file = $this->getTestFile('text');
    $nid = $this->uploadNodeFile($test_file, $field_name, $type_name, TRUE, array('private' => TRUE));
    $node = node_load($nid, NULL, TRUE);
    $node_file = (object) $node->{$field_name}[LANGUAGE_NONE][0];
    // Ensure the file can be downloaded.
    $this->drupalGet(file_create_url($node_file->uri));
    $this->assertResponse(200, 'Confirmed that the generated URL is correct by downloading the shipped file.');
    $this->drupalLogOut();
    $this->drupalGet(file_create_url($node_file->uri));
    $this->assertResponse(403, 'Confirmed that access is denied for the file without the needed permission.');

    // Test with the field that should deny access through field access.
    $this->drupalLogin($this->admin_user);
    $nid = $this->uploadNodeFile($test_file, $no_access_field_name, $type_name, TRUE, array('private' => TRUE));
    $node = node_load($nid, NULL, TRUE);
    $node_file = (object) $node->{$no_access_field_name}[LANGUAGE_NONE][0];
    // Ensure the file cannot be downloaded.
    $this->drupalGet(file_create_url($node_file->uri));
    $this->assertResponse(403, 'Confirmed that access is denied for the file without view field access permission.');

    // Attempt to reuse the existing file when creating a new node, and confirm
    // that access is still denied.
    $edit = array();
    $edit['title'] = $this->randomName(8);
    $edit[$field_name . '[' . LANGUAGE_NONE . '][0][fid]'] = $node_file->fid;
    $this->drupalPost('node/add/page', $edit, t('Save'));
    $new_node = $this->drupalGetNodeByTitle($edit['title']);
    $this->assertTrue(!empty($new_node), 'Node was created.');
    $this->assertUrl('node/' . $new_node->nid);
    $this->assertNoRaw($node_file->filename, 'File without view field access permission does not appear after attempting to attach it to a new node.');
    $this->drupalGet(file_create_url($node_file->uri));
    $this->assertResponse(403, 'Confirmed that access is denied for the file without view field access permission after attempting to attach it to a new node.');

    // As an anonymous user, create a temporary file with no references and
    // confirm that only the session that uploaded it may view it.
    $this->drupalLogout();
    user_role_grant_permissions(DRUPAL_ANONYMOUS_RID, array(
      "create $type_name content",
      'access content',
    ));
    $test_file = $this->getTestFile('text');
    $this->drupalGet('node/add/' . $type_name);
    $edit = array('files[' . $field_name . '_' . LANGUAGE_NONE . '_0]' => drupal_realpath($test_file->uri));
    $this->drupalPost(NULL, $edit, t('Upload'));
    $files = file_load_multiple(array(), array('uid' => 0));
    $this->assertEqual(1, count($files), 'Loaded one anonymous file.');
    $file = end($files);
    $this->assertNotEqual($file->status, FILE_STATUS_PERMANENT, 'File is temporary.');
    $usage = file_usage_list($file);
    $this->assertFalse($usage, 'No file usage found.');
    $file_url = file_create_url($file->uri);
    $this->drupalGet($file_url);
    $this->assertResponse(200, 'Confirmed that the anonymous uploader has access to the temporary file.');
    // Close the prior connection and remove the session cookie.
    $this->curlClose();
    $this->cookies = array();
    $this->drupalGet($file_url);
    $this->assertResponse(403, 'Confirmed that another anonymous user cannot access the temporary file.');

    // As an anonymous user, create a permanent file that is referenced by a
    // published node and confirm that all anonymous users may view it.
    $test_file = $this->getTestFile('text');
    $this->drupalGet('node/add/' . $type_name);
    $edit = array();
    $edit['title'] = $this->randomName();
    $edit['files[' . $field_name . '_' . LANGUAGE_NONE . '_0]'] = drupal_realpath($test_file->uri);
    $this->drupalPost(NULL, $edit, t('Save'));
    $new_node = $this->drupalGetNodeByTitle($edit['title']);
    $file = file_load($new_node->{$field_name}[LANGUAGE_NONE][0]['fid']);
    $this->assertEqual($file->status, FILE_STATUS_PERMANENT, 'File is permanent.');
    $usage = file_usage_list($file);
    $this->assertTrue($usage, 'File usage found.');
    $file_url = file_create_url($file->uri);
    $this->drupalGet($file_url);
    $this->assertResponse(200, 'Confirmed that the anonymous uploader has access to the permanent file that is referenced by a published node.');
    // Close the prior connection and remove the session cookie.
    $this->curlClose();
    $this->cookies = array();
    $this->drupalGet($file_url);
    $this->assertResponse(200, 'Confirmed that another anonymous user also has access to the permanent file that is referenced by a published node.');

    // As an anonymous user, create a permanent file that is referenced by an
    // unpublished node and confirm that no anonymous users may view it (even
    // the session that uploaded the file) because they cannot view the
    // unpublished node.
    $test_file = $this->getTestFile('text');
    $this->drupalGet('node/add/' . $type_name);
    $edit = array();
    $edit['title'] = $this->randomName();
    $edit['files[' . $field_name . '_' . LANGUAGE_NONE . '_0]'] = drupal_realpath($test_file->uri);
    $this->drupalPost(NULL, $edit, t('Save'));
    $new_node = $this->drupalGetNodeByTitle($edit['title']);
    $new_node->status = NODE_NOT_PUBLISHED;
    node_save($new_node);
    $file = file_load($new_node->{$field_name}[LANGUAGE_NONE][0]['fid']);
    $this->assertEqual($file->status, FILE_STATUS_PERMANENT, 'File is permanent.');
    $usage = file_usage_list($file);
    $this->assertTrue($usage, 'File usage found.');
    $file_url = file_create_url($file->uri);
    $this->drupalGet($file_url);
    $this->assertResponse(403, 'Confirmed that the anonymous uploader cannot access the permanent file when it is referenced by an unpublished node.');
    // Close the prior connection and remove the session cookie.
    $this->curlClose();
    $this->cookies = array();
    $this->drupalGet($file_url);
    $this->assertResponse(403, 'Confirmed that another anonymous user cannot access the permanent file when it is referenced by an unpublished node.');
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
