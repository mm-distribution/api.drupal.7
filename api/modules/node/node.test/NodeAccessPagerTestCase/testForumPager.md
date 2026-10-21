# NodeAccessPagerTestCase::testForumPager()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2821–2850 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2821-L2850)
- **Class:** [NodeAccessPagerTestCase](../NodeAccessPagerTestCase.md)
- **Module/theme:** node

## Signature

```php
public function testForumPager()
```

## Documentation

```text
Tests the forum node pager for nodes with multiple grants per realm.
```

## Code

```php
  public function testForumPager() {
    // Look up the forums vocabulary ID.
    $vid = variable_get('forum_nav_vocabulary', 0);
    $this->assertTrue($vid, 'Forum navigation vocabulary ID is set.');

    // Look up the general discussion term.
    $tree = taxonomy_get_tree($vid, 0, 1);
    $tid = reset($tree)->tid;
    $this->assertTrue($tid, 'General discussion term is found in the forum vocabulary.');

    // Create 30 nodes.
    for ($i = 0; $i < 30; $i++) {
      $this->drupalCreateNode(array(
        'nid' => NULL,
        'type' => 'forum',
        'taxonomy_forums' => array(
          LANGUAGE_NONE => array(
            array('tid' => $tid, 'vid' => $vid, 'vocabulary_machine_name' => 'forums'),
          ),
        ),
      ));
    }

    // View the general discussion forum page. With the default 25 nodes per
    // page there should be two pages for 30 nodes, no more.
    $this->drupalLogin($this->web_user);
    $this->drupalGet('forum/' . $tid);
    $this->assertRaw('page=1');
    $this->assertNoRaw('page=2');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
