# node_form_block_custom_block_delete_alter()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2475–2477 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2475-L2477)
- **Module/theme:** node

## Signature

```php
function node_form_block_custom_block_delete_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORMID_alter().

Adds node specific submit handler to delete custom block form.

@see block_custom_block_delete()
```

## Code

```php
function node_form_block_custom_block_delete_alter(&$form, &$form_state) {
  $form['#submit'][] = 'node_form_block_custom_block_delete_submit';
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
