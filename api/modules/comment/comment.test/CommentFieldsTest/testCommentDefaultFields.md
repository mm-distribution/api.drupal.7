# CommentFieldsTest::testCommentDefaultFields()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 2121–2149 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L2121-L2149)
- **Class:** [CommentFieldsTest](../CommentFieldsTest.md)
- **Module/theme:** comment

## Signature

```php
function testCommentDefaultFields()
```

## Documentation

```text
Tests that the default 'comment_body' field is correctly added.
```

## Code

```php
  function testCommentDefaultFields() {
    // Do not make assumptions on default node types created by the test
    // installation profile, and create our own.
    $this->drupalCreateContentType(array('type' => 'test_node_type'));

    // Check that the 'comment_body' field is present on all comment bundles.
    $instances = field_info_instances('comment');
    foreach (node_type_get_types() as $type_name => $info) {
      $this->assertTrue(isset($instances['comment_node_' . $type_name]['comment_body']), format_string('The comment_body field is present for comments on type @type', array('@type' => $type_name)));

      // Delete the instance along the way.
      field_delete_instance($instances['comment_node_' . $type_name]['comment_body']);
    }

    // Check that the 'comment_body' field is deleted.
    $field = field_info_field('comment_body');
    $this->assertTrue(empty($field), 'The comment_body field was deleted');

    // Create a new content type.
    $type_name = 'test_node_type_2';
    $this->drupalCreateContentType(array('type' => $type_name));

    // Check that the 'comment_body' field exists and has an instance on the
    // new comment bundle.
    $field = field_info_field('comment_body');
    $this->assertTrue($field, 'The comment_body field exists');
    $instances = field_info_instances('comment');
    $this->assertTrue(isset($instances['comment_node_' . $type_name]['comment_body']), format_string('The comment_body field is present for comments on type @type', array('@type' => $type_name)));
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
