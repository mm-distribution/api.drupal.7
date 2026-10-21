# node_validate()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1011–1041 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1011-L1041)
- **Module/theme:** node
- **Implements:** [hook_validate()](../node.api.php/hook_validate.md)

## Signature

```php
function node_validate($node, $form, &$form_state)
```

## Documentation

```text
Implements hook_validate().

Performs validation checks on the given node.
```

## Code

```php
function node_validate($node, $form, &$form_state) {
  if (isset($node->nid) && (node_last_changed($node->nid) > $node->changed)) {
    form_set_error('changed', t('The content on this page has either been modified by another user, or you have already submitted modifications using this form. As a result, your changes cannot be saved.'));
  }

  // Validate the "authored by" field.
  if (!empty($node->name) && !($account = user_load_by_name($node->name))) {
    // The use of empty() is mandatory in the context of usernames
    // as the empty string denotes the anonymous user. In case we
    // are dealing with an anonymous user we set the user ID to 0.
    form_set_error('name', t('The username %name does not exist.', array('%name' => $node->name)));
  }

  // Validate the "authored on" field.
  if (!empty($node->date) && strtotime($node->date) === FALSE) {
    form_set_error('date', t('You have to specify a valid date.'));
  }

  // Invoke hook_validate() for node type specific validation and
  // hook_node_validate() for miscellaneous validation needed by modules. Can't
  // use node_invoke() or module_invoke_all(), because $form_state must be
  // receivable by reference.
  $function = node_type_get_base($node) . '_validate';
  if (function_exists($function)) {
    $function($node, $form, $form_state);
  }
  foreach (module_implements('node_validate') as $module) {
    $function = $module . '_node_validate';
    $function($node, $form, $form_state);
  }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
