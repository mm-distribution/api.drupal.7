# node_form_submit()

- **Type:** Function
- **File:** [`modules/node/node.pages.inc`](_file.md), lines 456–485 · [local source](../../../../source/modules/node/node.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc#L456-L485)
- **Module/theme:** node

## Signature

```php
function node_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for node_form().

@see node_form()
@see node_form_validate()
```

## Code

```php
function node_form_submit($form, &$form_state) {
  $node = node_form_submit_build_node($form, $form_state);
  $insert = empty($node->nid);
  node_save($node);
  $node_link = l(t('view'), 'node/' . $node->nid);
  $watchdog_args = array('@type' => $node->type, '%title' => $node->title);
  $t_args = array('@type' => node_type_get_name($node), '%title' => $node->title);

  if ($insert) {
    watchdog('content', '@type: added %title.', $watchdog_args, WATCHDOG_NOTICE, $node_link);
    drupal_set_message(t('@type %title has been created.', $t_args));
  }
  else {
    watchdog('content', '@type: updated %title.', $watchdog_args, WATCHDOG_NOTICE, $node_link);
    drupal_set_message(t('@type %title has been updated.', $t_args));
  }
  if ($node->nid) {
    $form_state['values']['nid'] = $node->nid;
    $form_state['nid'] = $node->nid;
    $form_state['redirect'] = node_access('view', $node) ? 'node/' . $node->nid : '<front>';
  }
  else {
    // In the unlikely case something went wrong on save, the node will be
    // rebuilt and node form redisplayed the same way as in preview.
    drupal_set_message(t('The post could not be saved.'), 'error');
    $form_state['rebuild'] = TRUE;
  }
  // Clear the page and block caches.
  cache_clear_all();
}
```

---
_Drupal 7.103 · [modules/node/node.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
