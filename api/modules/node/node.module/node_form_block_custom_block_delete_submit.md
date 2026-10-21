# node_form_block_custom_block_delete_submit()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2484–2489 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2484-L2489)
- **Module/theme:** node

## Signature

```php
function node_form_block_custom_block_delete_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for node_form_block_custom_block_delete_alter().

@see node_form_block_custom_block_delete_alter()
```

## Code

```php
function node_form_block_custom_block_delete_submit($form, &$form_state) {
  db_delete('block_node_type')
    ->condition('module', 'block')
    ->condition('delta', $form_state['values']['bid'])
    ->execute();
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
