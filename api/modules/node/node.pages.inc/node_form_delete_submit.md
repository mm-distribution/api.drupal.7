# node_form_delete_submit()

- **Type:** Function
- **File:** [`modules/node/node.pages.inc`](_file.md), lines 338–346 · [local source](../../../../source/modules/node/node.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc#L338-L346)
- **Module/theme:** node

## Signature

```php
function node_form_delete_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for node_form().

Handles the 'Delete' button on the node form.

@see node_form()
@see node_form_validate()
```

## Code

```php
function node_form_delete_submit($form, &$form_state) {
  $destination = array();
  if (isset($_GET['destination'])) {
    $destination = drupal_get_destination();
    unset($_GET['destination']);
  }
  $node = $form['#node'];
  $form_state['redirect'] = array('node/' . $node->nid . '/delete', array('query' => $destination));
}
```

---
_Drupal 7.103 · [modules/node/node.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
