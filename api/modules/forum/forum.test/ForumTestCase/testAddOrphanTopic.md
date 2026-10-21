# ForumTestCase::testAddOrphanTopic()

- **Type:** Method
- **File:** [`modules/forum/forum.test`](../_file.md), lines 261–278 · [local source](../../../../../source/modules/forum/forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test#L261-L278)
- **Class:** [ForumTestCase](../ForumTestCase.md)
- **Module/theme:** forum

## Signature

```php
function testAddOrphanTopic()
```

## Documentation

```text
Tests that forum nodes can't be added without a parent.

Verifies that forum nodes are not created without choosing "forum" from the
select list.
```

## Code

```php
  function testAddOrphanTopic() {
    // Must remove forum topics to test creating orphan topics.
    $vid = variable_get('forum_nav_vocabulary');
    $tree = taxonomy_get_tree($vid);
    foreach ($tree as $term) {
      taxonomy_term_delete($term->tid);
    }

    // Create an orphan forum item.
    $this->drupalLogin($this->admin_user);
    $this->drupalPost('node/add/forum', array('title' => $this->randomName(10), 'body[' . LANGUAGE_NONE .'][0][value]' => $this->randomName(120)), t('Save'));

    $nid_count = db_query('SELECT COUNT(nid) FROM {node}')->fetchField();
    $this->assertEqual(0, $nid_count, 'A forum node was not created when missing a forum vocabulary.');

    // Reset the defaults for future tests.
    module_enable(array('forum'));
  }
```

---
_Drupal 7.103 · [modules/forum/forum.test](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._
