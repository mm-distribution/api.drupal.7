# node_form_block_admin_configure_alter()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2424–2445 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2424-L2445)
- **Module/theme:** node

## Signature

```php
function node_form_block_admin_configure_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORMID_alter().

Adds node-type specific visibility options to block configuration form.

@see block_admin_configure()
```

## Code

```php
function node_form_block_admin_configure_alter(&$form, &$form_state) {
  $default_type_options = db_query("SELECT type FROM {block_node_type} WHERE module = :module AND delta = :delta", array(
    ':module' => $form['module']['#value'],
    ':delta' => $form['delta']['#value'],
  ))->fetchCol();
  $form['visibility']['node_type'] = array(
    '#type' => 'fieldset',
    '#title' => t('Content types'),
    '#collapsible' => TRUE,
    '#collapsed' => TRUE,
    '#group' => 'visibility',
    '#weight' => 5,
  );
  $form['visibility']['node_type']['types'] = array(
    '#type' => 'checkboxes',
    '#title' => t('Show block for specific content types'),
    '#default_value' => $default_type_options,
    '#options' => node_type_get_names(),
    '#description' => t('Show this block only on pages that display content of the given type(s). If you select no types, there will be no type-specific limitation.'),
  );
  $form['#submit'][] = 'node_form_block_admin_configure_submit';
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
