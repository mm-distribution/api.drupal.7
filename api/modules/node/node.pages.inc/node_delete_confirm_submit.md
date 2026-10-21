# node_delete_confirm_submit()

- **Type:** Function
- **File:** [`modules/node/node.pages.inc`](_file.md), lines 543–553 · [local source](../../../../source/modules/node/node.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc#L543-L553)
- **Module/theme:** node

## Signature

```php
function node_delete_confirm_submit($form, &$form_state)
```

## Documentation

```text
Executes node deletion.

@see node_delete_confirm()
```

## Code

```php
function node_delete_confirm_submit($form, &$form_state) {
  if ($form_state['values']['confirm']) {
    $node = node_load($form_state['values']['nid']);
    node_delete($form_state['values']['nid']);
    cache_clear_all();
    watchdog('content', '@type: deleted %title.', array('@type' => $node->type, '%title' => $node->title));
    drupal_set_message(t('@type %title has been deleted.', array('@type' => node_type_get_name($node), '%title' => $node->title)));
  }

  $form_state['redirect'] = '<front>';
}
```

---
_Drupal 7.103 · [modules/node/node.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
