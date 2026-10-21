# FileFieldAnonymousSubmission::_testNodeWithFileWithoutTitle()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1886–1928 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1886-L1928)
- **Class:** [FileFieldAnonymousSubmission](../FileFieldAnonymousSubmission.md)
- **Module/theme:** file_module_test

## Signature

```php
protected function _testNodeWithFileWithoutTitle()
```

## Documentation

```text
Helper method to test file submissions with missing node titles.
```

## Code

```php
  protected function _testNodeWithFileWithoutTitle() {
    $bundle_label = 'Article';
    $node_title = 'Test page';

    // Load the node form.
    $this->drupalGet('node/add/article');
    $this->assertResponse(200, 'Loaded the article node form.');
    $this->assertText(strip_tags(t('Create @name', array('@name' => $bundle_label))));

    // Generate an image file.
    $image = $this->getTestImage();

    // Submit the form but exclude the title field.
    $edit = array(
      'body[und][0][value]' => 'Test article',
      'body[und][0][format]' => 'filtered_html',
      'files[field_image_und_0]' => drupal_realpath($image->uri),
    );
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertResponse(200);
    $t_args = array('@type' => $bundle_label, '%title' => $node_title);
    $this->assertNoText(strip_tags(t('@type %title has been created.', $t_args)), 'The node was created.');
    $this->assertText(t('!name field is required.', array('!name' => t('Title'))));

    // Submit the form again but this time with the missing title field. This
    // should still work.
    $edit = array(
      'title' => $node_title,
    );
    $this->drupalPost(NULL, $edit, t('Save'));

    // Confirm the final submission actually worked.
    $t_args = array('@type' => $bundle_label, '%title' => $node_title);
    $this->assertText(strip_tags(t('@type %title has been created.', $t_args)), 'The node was created.');
    $matches = array();
    if (preg_match('@node/(\d+)$@', $this->getUrl(), $matches)) {
      $nid = end($matches);
      $this->assertNotEqual($nid, 0, 'The node ID was extracted from the URL.');
      $node = node_load($nid);
      $this->assertNotEqual($node, NULL, 'The node was loaded successfully.');
      $this->assertEqual($node->field_image[LANGUAGE_NONE][0]['filename'], $image->filename, 'The image was uploaded successfully.');
    }
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
