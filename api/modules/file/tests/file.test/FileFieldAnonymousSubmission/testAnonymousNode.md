# FileFieldAnonymousSubmission::testAnonymousNode()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1799–1824 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1799-L1824)
- **Class:** [FileFieldAnonymousSubmission](../FileFieldAnonymousSubmission.md)
- **Module/theme:** file_module_test

## Signature

```php
function testAnonymousNode()
```

## Documentation

```text
Tests the basic node submission for an anonymous visitor.
```

## Code

```php
  function testAnonymousNode() {
    $bundle_label = 'Article';
    $node_title = 'Test page';

    // Load the node form.
    $this->drupalGet('node/add/article');
    $this->assertResponse(200, 'Loaded the article node form.');
    $this->assertText(strip_tags(t('Create @name', array('@name' => $bundle_label))));

    $edit = array(
      'title' => $node_title,
      'body[und][0][value]' => 'Test article',
      'body[und][0][format]' => 'filtered_html',
    );
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertResponse(200);
    $t_args = array('@type' => $bundle_label, '%title' => $node_title);
    $this->assertText(strip_tags(t('@type %title has been created.', $t_args)), 'The node was created.');
    $matches = array();
    if (preg_match('@node/(\d+)$@', $this->getUrl(), $matches)) {
      $nid = end($matches);
      $this->assertNotEqual($nid, 0, 'The node ID was extracted from the URL.');
      $node = node_load($nid);
      $this->assertNotEqual($node, NULL, 'The node was loaded successfully.');
    }
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
