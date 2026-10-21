# NodeAccessPagerTestCase::testCommentPager()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2787–2816 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2787-L2816)
- **Class:** [NodeAccessPagerTestCase](../NodeAccessPagerTestCase.md)
- **Module/theme:** node

## Signature

```php
public function testCommentPager()
```

## Documentation

```text
Tests the comment pager for nodes with multiple grants per realm.
```

## Code

```php
  public function testCommentPager() {
    // Create a node.
    $node = $this->drupalCreateNode();

    // Create 60 comments.
    for ($i = 0; $i < 60; $i++) {
      $comment = new stdClass();
      $comment->cid = 0;
      $comment->pid = 0;
      $comment->uid = $this->web_user->uid;
      $comment->nid = $node->nid;
      $comment->subject = $this->randomName();
      $comment->comment_body = array(
        LANGUAGE_NONE => array(
          array('value' => $this->randomName()),
        ),
      );
      comment_save($comment);
    }

    $this->drupalLogin($this->web_user);

    // View the node page. With the default 50 comments per page there should
    // be two pages (0, 1) but no third (2) page.
    $this->drupalGet('node/' . $node->nid);
    $this->assertText($node->title);
    $this->assertText(t('Comments'));
    $this->assertRaw('page=1');
    $this->assertNoRaw('page=2');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
