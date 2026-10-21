# node_admin_nodes_submit()

- **Type:** Function
- **File:** [`modules/node/node.admin.inc`](_file.md), lines 630–652 · [local source](../../../../source/modules/node/node.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc#L630-L652)
- **Module/theme:** node

## Signature

```php
function node_admin_nodes_submit($form, &$form_state)
```

## Documentation

```text
Process node_admin_nodes form submissions.

Executes the chosen 'Update option' on the selected nodes.

@see node_admin_nodes()
@see node_admin_nodes_validate()
@see node_filter_form()
@see node_filter_form_submit()
@see node_multiple_delete_confirm()
@see node_multiple_delete_confirm_submit()
```

## Code

```php
function node_admin_nodes_submit($form, &$form_state) {
  $operations = module_invoke_all('node_operations');
  $operation = $operations[$form_state['values']['operation']];
  // Filter out unchecked nodes
  $nodes = array_filter($form_state['values']['nodes']);
  if ($function = $operation['callback']) {
    // Add in callback arguments if present.
    if (isset($operation['callback arguments'])) {
      $args = array_merge(array($nodes), $operation['callback arguments']);
    }
    else {
      $args = array($nodes);
    }
    call_user_func_array($function, $args);

    cache_clear_all();
  }
  else {
    // We need to rebuild the form to go to a second step. For example, to
    // show the confirmation form for the deletion of nodes.
    $form_state['rebuild'] = TRUE;
  }
}
```

---
_Drupal 7.103 · [modules/node/node.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
