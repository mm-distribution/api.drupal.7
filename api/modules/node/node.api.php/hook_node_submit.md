# hook_node_submit()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 799–805 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L799-L805)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_node_submit($node, $form, &$form_state)
```

## Documentation

```text
Act on a node after validated form values have been copied to it.

This hook is invoked when a node form is submitted with either the "Save" or
"Preview" button, after form values have been copied to the form state's node
object, but before the node is saved or previewed. It is a chance for modules
to adjust the node's properties from what they are simply after a copy from
$form_state['values']. This hook is intended for adjusting non-field-related
properties. See hook_field_attach_submit() for customizing field-related
properties.

@param $node
  The node object being updated in response to a form submission.
@param $form
  The form being used to edit the node.
@param $form_state
  The form state array.

@ingroup node_api_hooks
```

## Code

```php
function hook_node_submit($node, $form, &$form_state) {
  // Decompose the selected menu parent option into 'menu_name' and 'plid', if
  // the form used the default parent selection widget.
  if (!empty($form_state['values']['menu']['parent'])) {
    list($node->menu['menu_name'], $node->menu['plid']) = explode(':', $form_state['values']['menu']['parent']);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_submit()".

- [menu_node_submit()](../../menu/menu.module/menu_node_submit.md) — `modules/menu/menu.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
