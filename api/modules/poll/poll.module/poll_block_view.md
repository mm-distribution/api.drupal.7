# poll_block_view()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 144–167 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L144-L167)
- **Module/theme:** poll
- **Implements:** [hook_block_view()](../../block/block.api.php/hook_block_view.md)

## Signature

```php
function poll_block_view($delta = '')
```

## Documentation

```text
Implements hook_block_view().

Generates a block containing the latest poll.
```

## Code

```php
function poll_block_view($delta = '') {
  if (user_access('access content')) {
    // Retrieve the latest poll.
    $select = db_select('node', 'n');
    $select->join('poll', 'p', 'p.nid = n.nid');
    $select->fields('n', array('nid'))
      ->condition('n.status', 1)
      ->condition('p.active', 1)
      ->orderBy('n.created', 'DESC')
      ->range(0, 1)
      ->addTag('node_access');

    $record = $select->execute()->fetchObject();
    if ($record) {
      $poll = node_load($record->nid);
      if ($poll->nid) {
        $poll = poll_block_latest_poll_view($poll);
        $block['subject'] = t('Poll');
        $block['content'] = $poll->content;
        return $block;
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
