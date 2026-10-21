# node_form_build_preview()

- **Type:** Function
- **File:** [`modules/node/node.pages.inc`](_file.md), lines 356–360 · [local source](../../../../source/modules/node/node.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc#L356-L360)
- **Module/theme:** node

## Signature

```php
function node_form_build_preview($form, &$form_state)
```

## Documentation

```text
Form submission handler for node_form().

Handles the 'Preview' button on the node form.

@see node_form()
@see node_form_validate()
```

## Code

```php
function node_form_build_preview($form, &$form_state) {
  $node = node_form_submit_build_node($form, $form_state);
  $form_state['node_preview'] = node_preview($node);
  $form_state['rebuild'] = TRUE;
}
```

---
_Drupal 7.103 · [modules/node/node.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
