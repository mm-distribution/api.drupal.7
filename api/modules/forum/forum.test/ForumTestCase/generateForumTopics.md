# ForumTestCase::generateForumTopics()

- **Type:** Method
- **File:** [`modules/forum/forum.test`](../_file.md), lines 642–648 · [local source](../../../../../source/modules/forum/forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test#L642-L648)
- **Class:** [ForumTestCase](../ForumTestCase.md)
- **Module/theme:** forum

## Signature

```php
private function generateForumTopics($forum)
```

## Documentation

```text
Generates forum topics to test the display of an active forum block.

@param array $forum
  The foorum array (a row from taxonomy_term_data table).
```

## Code

```php
  private function generateForumTopics($forum) {
    $this->nids = array();
    for ($i = 0; $i < 5; $i++) {
      $node = $this->createForumTopic($this->forum, FALSE);
      $this->nids[] = $node->nid;
    }
  }
```

---
_Drupal 7.103 · [modules/forum/forum.test](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._
