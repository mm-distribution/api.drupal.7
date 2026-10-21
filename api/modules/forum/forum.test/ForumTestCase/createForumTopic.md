# ForumTestCase::createForumTopic()

- **Type:** Method
- **File:** [`modules/forum/forum.test`](../_file.md), lines 492–529 · [local source](../../../../../source/modules/forum/forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test#L492-L529)
- **Class:** [ForumTestCase](../ForumTestCase.md)
- **Module/theme:** forum

## Signature

```php
function createForumTopic($forum, $container = FALSE)
```

## Documentation

```text
Creates forum topic.

@param array $forum
  A forum array.
@param boolean $container
  TRUE if $forum is a container; FALSE otherwise.

@return object
  The created topic node.
```

## Code

```php
  function createForumTopic($forum, $container = FALSE) {
    // Generate a random subject/body.
    $title = $this->randomName(20);
    $body = $this->randomName(200);

    $langcode = LANGUAGE_NONE;
    $edit = array(
      "title" => $title,
      "body[$langcode][0][value]" => $body,
    );
    $tid = $forum['tid'];

    // Create the forum topic, preselecting the forum ID via a URL parameter.
    $this->drupalPost('node/add/forum/' . $tid, $edit, t('Save'));

    $type = t('Forum topic');
    if ($container) {
      $this->assertNoRaw(t('@type %title has been created.', array('@type' => $type, '%title' => $title)), 'Forum topic was not created');
      $this->assertRaw(t('The item %title is a forum container, not a forum.', array('%title' => $forum['name'])), 'Error message was shown');
      return;
    }
    else {
      $this->assertRaw(t('@type %title has been created.', array('@type' => $type, '%title' => $title)), 'Forum topic was created');
      $this->assertNoRaw(t('The item %title is a forum container, not a forum.', array('%title' => $forum['name'])), 'No error message was shown');
    }

    // Retrieve node object, ensure that the topic was created and in the proper forum.
    $node = $this->drupalGetNodeByTitle($title);
    $this->assertTrue($node != NULL, format_string('Node @title was loaded', array('@title' => $title)));
    $this->assertEqual($node->taxonomy_forums[LANGUAGE_NONE][0]['tid'], $tid, 'Saved forum topic was in the expected forum');

    // View forum topic.
    $this->drupalGet('node/' . $node->nid);
    $this->assertRaw($title, 'Subject was found');
    $this->assertRaw($body, 'Body was found');

    return $node;
  }
```

---
_Drupal 7.103 · [modules/forum/forum.test](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._
