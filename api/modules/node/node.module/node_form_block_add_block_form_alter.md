# node_form_block_add_block_form_alter()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2413–2415 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2413-L2415)
- **Module/theme:** node

## Signature

```php
function node_form_block_add_block_form_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORMID_alter().

Adds node-type specific visibility options to add block form.

@see block_add_block_form()
```

## Code

```php
function node_form_block_add_block_form_alter(&$form, &$form_state) {
  node_form_block_admin_configure_alter($form, $form_state);
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
