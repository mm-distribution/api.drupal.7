# poll_block_latest_poll_view()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 633–667 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L633-L667)
- **Module/theme:** poll

## Signature

```php
function poll_block_latest_poll_view($node)
```

## Documentation

```text
Return content for 'latest poll' block.

@param $node
  The node object to load.
```

## Code

```php
function poll_block_latest_poll_view($node) {
  // This is necessary for shared objects because PHP doesn't copy objects, but
  // passes them by reference.  So when the objects are cached it can result in
  // the wrong output being displayed on subsequent calls.  The cloning and
  // unsetting of $node->content prevents the block output from being the same
  // as the node output.
  $node = clone $node;
  unset($node->content);

  // No 'read more' link.
  $node->readmore = FALSE;
  $node->teaser = '';

  $links = array();
  $links[] = array('title' => t('Older polls'), 'href' => 'poll', 'attributes' => array('title' => t('View the list of polls on this site.')));
  if ($node->allowvotes) {
    $links[] = array('title' => t('Results'), 'href' => 'node/' . $node->nid . '/results', 'attributes' => array('title' => t('View the current poll results.')));
  }

  $node->links = $links;

  if (!empty($node->allowvotes)) {
    $node->content['poll_view_voting'] = drupal_get_form('poll_view_voting', $node, TRUE);
    $node->content['links'] = array(
      '#theme' => 'links',
      '#links' => $node->links,
      '#weight' => 5,
    );
  }
  else {
    $node->content['poll_view_results'] = array('#markup' => poll_view_results($node, TRUE, TRUE));
  }

  return $node;
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
