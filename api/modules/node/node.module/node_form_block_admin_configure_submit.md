# node_form_block_admin_configure_submit()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2452–2466 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2452-L2466)
- **Module/theme:** node

## Signature

```php
function node_form_block_admin_configure_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for node_form_block_admin_configure_alter().

@see node_form_block_admin_configure_alter()
```

## Code

```php
function node_form_block_admin_configure_submit($form, &$form_state) {
  db_delete('block_node_type')
    ->condition('module', $form_state['values']['module'])
    ->condition('delta', $form_state['values']['delta'])
    ->execute();
  $query = db_insert('block_node_type')->fields(array('type', 'module', 'delta'));
  foreach (array_filter($form_state['values']['types']) as $type) {
    $query->values(array(
      'type' => $type,
      'module' => $form_state['values']['module'],
      'delta' => $form_state['values']['delta'],
    ));
  }
  $query->execute();
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
