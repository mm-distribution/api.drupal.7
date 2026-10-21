# poll_page()

- **Type:** Function
- **File:** [`modules/poll/poll.pages.inc`](_file.md), lines 11–46 · [local source](../../../../source/modules/poll/poll.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.pages.inc#L11-L46)
- **Module/theme:** poll

## Signature

```php
function poll_page()
```

## Documentation

```text
Menu callback to provide a simple list of all polls available.
```

## Code

```php
function poll_page() {
  $polls_per_page = 15;

  $count_select = db_select('node', 'n');
  $count_select->addExpression('COUNT(*)', 'expression');
  $count_select->join('poll', 'p', 'p.nid = n.nid');
  $count_select->condition('n.status', 1);

  // List all polls.
  $select = db_select('node', 'n');
  $select->join('poll', 'p', 'p.nid = n.nid');
  $select->join('poll_choice', 'c', 'c.nid = n.nid');
  $select->addExpression('SUM(c.chvotes)', 'votes');
  $select = $select->fields('n', array('nid', 'title', 'created'))
    ->fields('p', array('active'))
    ->condition('n.status', 1)
    ->orderBy('n.created', 'DESC')
    ->groupBy('n.nid')
    ->groupBy('n.title')
    ->groupBy('p.active')
    ->groupBy('n.created')
    ->extend('PagerDefault')
    ->limit($polls_per_page)
    ->addTag('node_access');
  $select->setCountQuery($count_select);
  $queried_nodes = $select->execute()
    ->fetchAllAssoc('nid');

  $output = '<ul>';
  foreach ($queried_nodes as $node) {
    $output .= '<li>' . l($node->title, "node/$node->nid") . ' - ' . format_plural($node->votes, '1 vote', '@count votes') . ' - ' . ($node->active ? t('open') : t('closed')) . '</li>';
  }
  $output .= '</ul>';
  $output .= theme('pager');
  return $output;
}
```

---
_Drupal 7.103 · [modules/poll/poll.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
