# CommentRSSUnitTest::testCommentRSS()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 1793–1806 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L1793-L1806)
- **Class:** [CommentRSSUnitTest](../CommentRSSUnitTest.md)
- **Module/theme:** comment

## Signature

```php
function testCommentRSS()
```

## Documentation

```text
Test comments as part of an RSS feed.
```

## Code

```php
  function testCommentRSS() {
    // Find comment in RSS feed.
    $this->drupalLogin($this->web_user);
    $comment = $this->postComment($this->node, $this->randomName(), $this->randomName());
    $this->drupalGet('rss.xml');
    $raw = '<comments>' . url('node/' . $this->node->nid, array('fragment' => 'comments', 'absolute' => TRUE)) . '</comments>';
    $this->assertRaw($raw, 'Comments as part of RSS feed.');

    // Hide comments from RSS feed and check presence.
    $this->node->comment = COMMENT_NODE_HIDDEN;
    node_save($this->node);
    $this->drupalGet('rss.xml');
    $this->assertNoRaw($raw, 'Hidden comments is not a part of RSS feed.');
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
