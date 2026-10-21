# poll_view_results()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 809–832 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L809-L832)
- **Module/theme:** poll

## Signature

```php
function poll_view_results($node, $view_mode, $block = FALSE)
```

## Documentation

```text
Generates a graphical representation of the results of a poll.
```

## Code

```php
function poll_view_results($node, $view_mode, $block = FALSE) {
  // Make sure that choices are ordered by their weight.
  uasort($node->choice, 'drupal_sort_weight');

  // Count the votes and find the maximum.
  $total_votes = 0;
  $max_votes = 0;
  foreach ($node->choice as $choice) {
    if (isset($choice['chvotes'])) {
      $total_votes += $choice['chvotes'];
      $max_votes = max($max_votes, $choice['chvotes']);
    }
  }

  $poll_results = '';
  foreach ($node->choice as $i => $choice) {
    if (!empty($choice['chtext'])) {
      $chvotes = isset($choice['chvotes']) ? $choice['chvotes'] : NULL;
      $poll_results .= theme('poll_bar', array('title' => $choice['chtext'], 'votes' => $chvotes, 'total_votes' => $total_votes, 'vote' => isset($node->vote) && $node->vote == $i, 'block' => $block));
    }
  }

  return theme('poll_results', array('raw_title' => $node->title, 'results' => $poll_results, 'votes' => $total_votes, 'raw_links' => isset($node->links) ? $node->links : array(), 'block' => $block, 'nid' => $node->nid, 'vote' => isset($node->vote) ? $node->vote : NULL));
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
