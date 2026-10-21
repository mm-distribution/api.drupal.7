# node_filter_form_submit()

- **Type:** Function
- **File:** [`modules/node/node.admin.inc`](_file.md), lines 234–258 · [local source](../../../../source/modules/node/node.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc#L234-L258)
- **Module/theme:** node

## Signature

```php
function node_filter_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for node_filter_form().

@see node_admin_content()
@see node_admin_nodes()
@see node_admin_nodes_submit()
@see node_admin_nodes_validate()
@see node_filter_form()
@see node_multiple_delete_confirm()
@see node_multiple_delete_confirm_submit()
```

## Code

```php
function node_filter_form_submit($form, &$form_state) {
  $filters = node_filters();
  switch ($form_state['values']['op']) {
    case t('Filter'):
    case t('Refine'):
      // Apply every filter that has a choice selected other than 'any'.
      foreach ($filters as $filter => $options) {
        if (isset($form_state['values'][$filter]) && $form_state['values'][$filter] != '[any]') {
          // Flatten the options array to accommodate hierarchical/nested options.
          $flat_options = form_options_flatten($filters[$filter]['options']);
          // Only accept valid selections offered on the dropdown, block bad input.
          if (isset($flat_options[$form_state['values'][$filter]])) {
            $_SESSION['node_overview_filter'][] = array($filter, $form_state['values'][$filter]);
          }
        }
      }
      break;
    case t('Undo'):
      array_pop($_SESSION['node_overview_filter']);
      break;
    case t('Reset'):
      $_SESSION['node_overview_filter'] = array();
      break;
  }
}
```

---
_Drupal 7.103 · [modules/node/node.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
