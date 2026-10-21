# CommentInterfaceTest::testCommentNewCommentsIndicator()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 433–478 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L433-L478)
- **Class:** [CommentInterfaceTest](../CommentInterfaceTest.md)
- **Module/theme:** comment

## Signature

```php
public function testCommentNewCommentsIndicator()
```

## Documentation

```text
Tests new comment marker.
```

## Code

```php
  public function testCommentNewCommentsIndicator() {
    // Test if the right links are displayed when no comment is present for the
    // node.
    $this->drupalLogin($this->admin_user);
    $this->node = $this->drupalCreateNode(array('type' => 'article', 'promote' => 1, 'comment' => COMMENT_NODE_OPEN));
    $this->drupalGet('node');
    $this->assertNoLink(t('@count comments', array('@count' => 0)));
    $this->assertNoLink(t('@count new comments', array('@count' => 0)));
    $this->assertLink(t('Read more'));
    $count = $this->xpath('//div[@id=:id]/div[@class=:class]/ul/li', array(':id' => 'node-' . $this->node->nid, ':class' => 'link-wrapper'));
    $this->assertTrue(count($count) == 1, 'One child found');

    // Create a new comment. This helper function may be run with different
    // comment settings so use comment_save() to avoid complex setup.
    $comment = (object) array(
      'cid' => NULL,
      'nid' => $this->node->nid,
      'node_type' => $this->node->type,
      'pid' => 0,
      'uid' => $this->loggedInUser->uid,
      'status' => COMMENT_PUBLISHED,
      'subject' => $this->randomName(),
      'hostname' => ip_address(),
      'language' => LANGUAGE_NONE,
      'comment_body' => array(LANGUAGE_NONE => array($this->randomName())),
    );
    comment_save($comment);
    $this->drupalLogout();

    // Log in with 'web user' and check comment links.
    $this->drupalLogin($this->web_user);
    $this->drupalGet('node');
    $this->assertLink(t('1 new comment'));
    $this->clickLink(t('1 new comment'));
    $this->assertRaw('<a id="new"></a>', 'Found "new" marker.');
    $this->assertTrue($this->xpath('//a[@id=:new]/following-sibling::a[1][@id=:comment_id]', array(':new' => 'new', ':comment_id' => 'comment-1')), 'The "new" anchor is positioned at the right comment.');

    // Test if "new comment" link is correctly removed.
    $this->drupalGet('node');
    $this->assertLink(t('1 comment'));
    $this->assertLink(t('Read more'));
    $this->assertNoLink(t('1 new comment'));
    $this->assertNoLink(t('@count new comments', array('@count' => 0)));
    $count = $this->xpath('//div[@id=:id]/div[@class=:class]/ul/li', array(':id' => 'node-' . $this->node->nid, ':class' => 'link-wrapper'));
    $this->assertTrue(count($count) == 2, print_r($count, TRUE));
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
