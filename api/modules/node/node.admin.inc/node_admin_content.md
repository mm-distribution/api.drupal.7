# node_admin_content()

- **Type:** Function
- **File:** [`modules/node/node.admin.inc`](_file.md), lines 404–413 · [local source](../../../../source/modules/node/node.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc#L404-L413)
- **Module/theme:** node
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function node_admin_content($form, $form_state)
```

## Documentation

```text
Page callback: Form constructor for the content administration form.

@see node_admin_nodes()
@see node_admin_nodes_submit()
@see node_admin_nodes_validate()
@see node_filter_form()
@see node_filter_form_submit()
@see node_menu()
@see node_multiple_delete_confirm()
@see node_multiple_delete_confirm_submit()
@ingroup forms
```

## Code

```php
function node_admin_content($form, $form_state) {
  if (isset($form_state['values']['operation']) && $form_state['values']['operation'] == 'delete') {
    return node_multiple_delete_confirm($form, $form_state, array_filter($form_state['values']['nodes']));
  }
  $form['filter'] = node_filter_form();
  $form['#submit'][] = 'node_filter_form_submit';
  $form['admin'] = node_admin_nodes();

  return $form;
}
```

---
_Drupal 7.103 · [modules/node/node.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
