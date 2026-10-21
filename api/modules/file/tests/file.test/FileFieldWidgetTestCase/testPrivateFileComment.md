# FileFieldWidgetTestCase::testPrivateFileComment()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 948–1017 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L948-L1017)
- **Class:** [FileFieldWidgetTestCase](../FileFieldWidgetTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function testPrivateFileComment()
```

## Documentation

```text
Tests that download restrictions on private files work on comments.
```

## Code

```php
  function testPrivateFileComment() {
    $user = $this->drupalCreateUser(array('access comments'));

    // Remove access comments permission from anon user.
    $edit = array(
      DRUPAL_ANONYMOUS_RID . '[access comments]' => FALSE,
    );
    $this->drupalPost('admin/people/permissions', $edit, t('Save permissions'));

    // Create a new field.
    $edit = array(
      'fields[_add_new_field][label]' => $label = $this->randomName(),
      'fields[_add_new_field][field_name]' => $name = strtolower($this->randomName()),
      'fields[_add_new_field][type]' => 'file',
      'fields[_add_new_field][widget_type]' => 'file_generic',
    );
    $this->drupalPost('admin/structure/types/manage/article/comment/fields', $edit, t('Save'));
    $edit = array('field[settings][uri_scheme]' => 'private');
    $this->drupalPost(NULL, $edit, t('Save field settings'));
    $this->drupalPost(NULL, array(), t('Save settings'));

    // Create node.
    $text_file = $this->getTestFile('text');
    $edit = array(
      'title' => $this->randomName(),
    );
    $this->drupalPost('node/add/article', $edit, t('Save'));
    $node = $this->drupalGetNodeByTitle($edit['title']);

    // Add a comment with a file.
    $text_file = $this->getTestFile('text');
    $edit = array(
      'files[field_' . $name . '_' . LANGUAGE_NONE . '_' . 0 . ']' => drupal_realpath($text_file->uri),
      'comment_body[' . LANGUAGE_NONE . '][0][value]' => $comment_body = $this->randomName(),
    );
    $this->drupalPost(NULL, $edit, t('Save'));

    // Get the comment ID.
    preg_match('/comment-([0-9]+)/', $this->getUrl(), $matches);
    $cid = $matches[1];

    // Log in as normal user.
    $this->drupalLogin($user);

    $comment = comment_load($cid);
    $comment_file = (object) $comment->{'field_' . $name}[LANGUAGE_NONE][0];
    $this->assertFileExists($comment_file, 'New file saved to disk on node creation.');
    // Test authenticated file download.
    $url = file_create_url($comment_file->uri);
    $this->assertNotEqual($url, NULL, 'Confirmed that the URL is valid');
    $this->drupalGet(file_create_url($comment_file->uri));
    $this->assertResponse(200, 'Confirmed that the generated URL is correct by downloading the shipped file.');

    // Test anonymous file download.
    $this->drupalLogout();
    $this->drupalGet(file_create_url($comment_file->uri));
    $this->assertResponse(403, 'Confirmed that access is denied for the file without the needed permission.');

    // Unpublishes node.
    $this->drupalLogin($this->admin_user);
    $edit = array(
      'status' => FALSE,
    );
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));

    // Ensures normal user can no longer download the file.
    $this->drupalLogin($user);
    $this->drupalGet(file_create_url($comment_file->uri));
    $this->assertResponse(403, 'Confirmed that access is denied for the file without the needed permission.');
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
