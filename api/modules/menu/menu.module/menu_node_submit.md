# menu_node_submit()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 788–794 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L788-L794)
- **Module/theme:** menu
- **Implements:** [hook_node_submit()](../../node/node.api.php/hook_node_submit.md)

## Signature

```php
function menu_node_submit($node, $form, $form_state)
```

## Documentation

```text
Implements hook_node_submit().

@see menu_form_node_form_alter()
```

## Code

```php
function menu_node_submit($node, $form, $form_state) {
  // Decompose the selected menu parent option into 'menu_name' and 'plid', if
  // the form used the default parent selection widget.
  if (!empty($form_state['values']['menu']['parent'])) {
    list($node->menu['menu_name'], $node->menu['plid']) = explode(':', $form_state['values']['menu']['parent']);
  }
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
