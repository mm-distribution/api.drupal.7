# node_form_submit_build_node()

- **Type:** Function
- **File:** [`modules/node/node.pages.inc`](_file.md), lines 498–518 · [local source](../../../../source/modules/node/node.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc#L498-L518)
- **Module/theme:** node

## Signature

```php
function node_form_submit_build_node($form, &$form_state)
```

## Documentation

```text
Updates the form state's node entity by processing this submission's values.

This is the default builder function for the node form. It is called
during the "Save" and "Preview" submit handlers to retrieve the entity to
save or preview. This function can also be called by a "Next" button of a
wizard to update the form state's entity with the current step's values
before proceeding to the next step.

@see node_form()
```

## Code

```php
function node_form_submit_build_node($form, &$form_state) {
  // @todo Legacy support for modules that extend the node form with form-level
  //   submit handlers that adjust $form_state['values'] prior to those values
  //   being used to update the entity. Module authors are encouraged to instead
  //   adjust the node directly within a hook_node_submit() implementation. For
  //   Drupal 8, evaluate whether the pattern of triggering form-level submit
  //   handlers during button-level submit processing is worth supporting
  //   properly, and if so, add a Form API function for doing so.
  unset($form_state['submit_handlers']);
  form_execute_handlers('submit', $form, $form_state);

  $node = $form_state['node'];
  entity_form_submit_build_entity('node', $node, $form, $form_state);

  node_submit($node);
  foreach (module_implements('node_submit') as $module) {
    $function = $module . '_node_submit';
    $function($node, $form, $form_state);
  }
  return $node;
}
```

---
_Drupal 7.103 · [modules/node/node.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
