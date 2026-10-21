# ForumTestCase::viewForumTopics()

- **Type:** Method
- **File:** [`modules/forum/forum.test`](../_file.md), lines 660–668 · [local source](../../../../../source/modules/forum/forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test#L660-L668)
- **Class:** [ForumTestCase](../ForumTestCase.md)
- **Module/theme:** forum

## Signature

```php
private function viewForumTopics($nids)
```

## Documentation

```text
Views forum topics to test the display of an active forum block.

@todo The logic here is completely incorrect, since the active forum topics
  block is determined by comments on the node, not by views.
@todo DIE

@param $nids
  An array of forum node IDs.
```

## Code

```php
  private function viewForumTopics($nids) {
    for ($i = 0; $i < 2; $i++) {
      foreach ($nids as $nid) {
        $this->drupalGet('node/' . $nid);
        $this->drupalGet('node/' . $nid);
        $this->drupalGet('node/' . $nid);
      }
    }
  }
```

---
_Drupal 7.103 · [modules/forum/forum.test](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._
