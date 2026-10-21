# node_admin_nodes_validate()

- **Type:** Function
- **File:** [`modules/node/node.admin.inc`](_file.md), lines 611–616 · [local source](../../../../source/modules/node/node.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc#L611-L616)
- **Module/theme:** node

## Signature

```php
function node_admin_nodes_validate($form, &$form_state)
```

## Documentation

```text
Validate node_admin_nodes form submissions.

Checks whether any nodes have been selected to perform the chosen 'Update
option' on.

@see node_admin_nodes()
@see node_admin_nodes_submit()
@see node_filter_form()
@see node_filter_form_submit()
@see node_multiple_delete_confirm()
@see node_multiple_delete_confirm_submit()
```

## Code

```php
function node_admin_nodes_validate($form, &$form_state) {
  // Error if there are no items to select.
  if (!is_array($form_state['values']['nodes']) || !count(array_filter($form_state['values']['nodes']))) {
    form_set_error('', t('No items selected.'));
  }
}
```

---
_Drupal 7.103 · [modules/node/node.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
