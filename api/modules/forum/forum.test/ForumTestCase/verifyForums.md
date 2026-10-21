# ForumTestCase::verifyForums()

- **Type:** Method
- **File:** [`modules/forum/forum.test`](../_file.md), lines 543–609 · [local source](../../../../../source/modules/forum/forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test#L543-L609)
- **Class:** [ForumTestCase](../ForumTestCase.md)
- **Module/theme:** forum

## Signature

```php
private function verifyForums($node_user, $node, $admin, $response = 200)
```

## Documentation

```text
Verifies that the logged in user has access to a forum nodes.

@param $node_user
  The user who creates the node.
@param $node
  The node being checked.
@param $admin
  Boolean to indicate whether the user can 'access administration pages'.
@param $response
  The exptected HTTP response code.
```

## Code

```php
  private function verifyForums($node_user, $node, $admin, $response = 200) {
    $response2 = ($admin) ? 200 : 403;

    // View forum help node.
    $this->drupalGet('admin/help/forum');
    $this->assertResponse($response2);
    if ($response2 == 200) {
      $this->assertTitle(t('Forum | Drupal'), 'Forum help title was displayed');
      $this->assertText(t('Forum'), 'Forum help node was displayed');
    }

    // Verify the forum blocks were displayed.
    $this->drupalGet('');
    $this->assertResponse(200);
    $this->assertText(t('New forum topics'), '[New forum topics] Forum block was displayed');

    // View forum container page.
    $this->verifyForumView($this->container);
    // View forum page.
    $this->verifyForumView($this->forum, $this->container);
    // View root forum page.
    $this->verifyForumView($this->root_forum);

    // View forum node.
    $this->drupalGet('node/' . $node->nid);
    $this->assertResponse(200);
    $this->assertTitle($node->title . ' | Drupal', 'Forum node was displayed');
    $breadcrumb = array(
      l(t('Home'), NULL),
      l(t('Forums'), 'forum'),
      l($this->container['name'], 'forum/' . $this->container['tid']),
      l($this->forum['name'], 'forum/' . $this->forum['tid']),
    );
    $this->assertRaw(theme('breadcrumb', array('breadcrumb' => $breadcrumb)), 'Breadcrumbs were displayed');

    // View forum edit node.
    $this->drupalGet('node/' . $node->nid . '/edit');
    $this->assertResponse($response);
    if ($response == 200) {
      $this->assertTitle('Edit Forum topic ' . $node->title . ' | Drupal', 'Forum edit node was displayed');
    }

    if ($response == 200) {
      // Edit forum node (including moving it to another forum).
      $edit = array();
      $langcode = LANGUAGE_NONE;
      $edit["title"] = 'node/' . $node->nid;
      $edit["body[$langcode][0][value]"] = $this->randomName(256);
      // Assume the topic is initially associated with $forum.
      $edit["taxonomy_forums[$langcode]"] = $this->root_forum['tid'];
      $edit['shadow'] = TRUE;
      $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));
      $this->assertRaw(t('Forum topic %title has been updated.', array('%title' => $edit["title"])), 'Forum node was edited');

      // Verify topic was moved to a different forum.
      $forum_tid = db_query("SELECT tid FROM {forum} WHERE nid = :nid AND vid = :vid", array(
        ':nid' => $node->nid,
        ':vid' => $node->vid,
      ))->fetchField();
      $this->assertTrue($forum_tid == $this->root_forum['tid'], 'The forum topic is linked to a different forum');

      // Delete forum node.
      $this->drupalPost('node/' . $node->nid . '/delete', array(), t('Delete'));
      $this->assertResponse($response);
      $this->assertRaw(t('Forum topic %title has been deleted.', array('%title' => $edit['title'])), 'Forum node was deleted');
    }
  }
```

---
_Drupal 7.103 · [modules/forum/forum.test](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._
