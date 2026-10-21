# node_form_validate()

- **Type:** Function
- **File:** [`modules/node/node.pages.inc`](_file.md), lines 89–96 · [local source](../../../../source/modules/node/node.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc#L89-L96)
- **Module/theme:** node

## Signature

```php
function node_form_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for node_form().

@see node_form()
@see node_form_submit()
```

## Code

```php
function node_form_validate($form, &$form_state) {
  // $form_state['node'] contains the actual entity being edited, but we must
  // not update it with form values that have not yet been validated, so we
  // create a pseudo-entity to use during validation.
  $node = (object) $form_state['values'];
  node_validate($node, $form, $form_state);
  entity_form_field_validate('node', $form, $form_state);
}
```

---
_Drupal 7.103 · [modules/node/node.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
