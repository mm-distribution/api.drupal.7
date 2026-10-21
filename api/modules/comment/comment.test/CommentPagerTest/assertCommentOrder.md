# CommentPagerTest::assertCommentOrder()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 1399–1414 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L1399-L1414)
- **Class:** [CommentPagerTest](../CommentPagerTest.md)
- **Module/theme:** comment

## Signature

```php
function assertCommentOrder(array $comments, array $expected_order)
```

## Documentation

```text
Helper function: assert that the comments are displayed in the correct order.

@param $comments
  And array of comments.
@param $expected_order
  An array of keys from $comments describing the expected order.
```

## Code

```php
  function assertCommentOrder(array $comments, array $expected_order) {
    $expected_cids = array();

    // First, rekey the expected order by cid.
    foreach ($expected_order as $key) {
      $expected_cids[] = $comments[$key]->id;
    }

    $comment_anchors = $this->xpath('//a[starts-with(@id,"comment-")]');
    $result_order = array();
    foreach ($comment_anchors as $anchor) {
      $result_order[] = substr($anchor['id'], 8);
    }

    return $this->assertIdentical($expected_cids, $result_order, format_string('Comment order: expected @expected, returned @returned.', array('@expected' => implode(',', $expected_cids), '@returned' => implode(',', $result_order))));
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
