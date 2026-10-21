# FilePrivateTestCase::testPrivateFileDownloadAccessGranted()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1702–1770 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1702-L1770)
- **Class:** [FilePrivateTestCase](../FilePrivateTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function testPrivateFileDownloadAccessGranted()
```

## Documentation

```text
Tests file access for private nodes when file download access is granted.
```

## Code

```php
  function testPrivateFileDownloadAccessGranted() {
    // Tell file_module_test to attempt to grant access to all private files,
    // and ensure that it is doing so correctly.
    $test_file = $this->getTestFile('text');
    $uri = file_unmanaged_move($test_file->uri, 'private://');
    $file_url = file_create_url($uri);
    $this->drupalGet($file_url);
    $this->assertResponse(403, 'Access is not granted to an arbitrary private file by default.');
    variable_set('file_module_test_grant_download_access', TRUE);
    $this->drupalGet($file_url);
    $this->assertResponse(200, 'Access is granted to an arbitrary private file after a module grants access to all private files in hook_file_download().');

    // Create a public node with a file attached.
    $type_name = 'page';
    $field_name = strtolower($this->randomName());
    $this->createFileField($field_name, $type_name, array('uri_scheme' => 'private'));
    $test_file = $this->getTestFile('text');
    $nid = $this->uploadNodeFile($test_file, $field_name, $type_name, TRUE, array('private' => FALSE));
    $node = node_load($nid, NULL, TRUE);
    $file_url = file_create_url($node->{$field_name}[LANGUAGE_NONE][0]['uri']);

    // Unpublish the node and ensure that only administrators (not anonymous
    // users) can access the node and download the file; the expectation is
    // that the File module's hook_file_download() implementation will deny
    // access and thereby override the file_module_test module's access grant.
    $node->status = NODE_NOT_PUBLISHED;
    node_save($node);
    $this->drupalLogin($this->admin_user);
    $this->drupalGet("node/$nid");
    $this->assertResponse(200, 'Administrator can access the unpublished node.');
    $this->drupalGet($file_url);
    $this->assertResponse(200, 'Administrator can download the file attached to the unpublished node.');
    $this->drupalLogOut();
    $this->drupalGet("node/$nid");
    $this->assertResponse(403, 'Anonymous user cannot access the unpublished node.');
    $this->drupalGet($file_url);
    $this->assertResponse(403, 'Anonymous user cannot download the file attached to the unpublished node.');

    // Re-publish the node and ensure that the node and file can be accessed by
    // everyone.
    $node->status = NODE_PUBLISHED;
    node_save($node);
    $this->drupalLogin($this->admin_user);
    $this->drupalGet("node/$nid");
    $this->assertResponse(200, 'Administrator can access the published node.');
    $this->drupalGet($file_url);
    $this->assertResponse(200, 'Administrator can download the file attached to the published node.');
    $this->drupalLogOut();
    $this->drupalGet("node/$nid");
    $this->assertResponse(200, 'Anonymous user can access the published node.');
    $this->drupalGet($file_url);
    $this->assertResponse(200, 'Anonymous user can download the file attached to the published node.');

    // Make the node private via the node access system and test that only
    // administrators (not anonymous users) can access the node and download
    // the file.
    $node->private = TRUE;
    node_save($node);
    $this->drupalLogin($this->admin_user);
    $this->drupalGet("node/$nid");
    $this->assertResponse(200, 'Administrator can access the private node.');
    $this->drupalGet($file_url);
    $this->assertResponse(200, 'Administrator can download the file attached to the private node.');
    $this->drupalLogOut();
    $this->drupalGet("node/$nid");
    $this->assertResponse(403, 'Anonymous user cannot access the private node.');
    $this->drupalGet($file_url);
    $this->assertResponse(403, 'Anonymous user cannot download the file attached to the private node.');
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
