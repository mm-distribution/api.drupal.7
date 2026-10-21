# node_multiple_delete_confirm_submit()

- **Type:** Function
- **File:** [`modules/node/node.admin.inc`](_file.md), lines 698–707 · [local source](../../../../source/modules/node/node.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc#L698-L707)
- **Module/theme:** node

## Signature

```php
function node_multiple_delete_confirm_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for node_multiple_delete_confirm().

@see node_admin_nodes()
@see node_admin_nodes_submit()
@see node_admin_nodes_validate()
@see node_filter_form()
@see node_filter_form_submit()
@see node_multiple_delete_confirm()
```

## Code

```php
function node_multiple_delete_confirm_submit($form, &$form_state) {
  if ($form_state['values']['confirm']) {
    node_delete_multiple(array_keys($form_state['values']['nodes']));
    cache_clear_all();
    $count = count($form_state['values']['nodes']);
    watchdog('content', 'Deleted @count posts.', array('@count' => $count));
    drupal_set_message(format_plural($count, 'Deleted 1 post.', 'Deleted @count posts.'));
  }
  $form_state['redirect'] = 'admin/content';
}
```

---
_Drupal 7.103 · [modules/node/node.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
