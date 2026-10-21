# node_delete_confirm()

- **Type:** Function
- **File:** [`modules/node/node.pages.inc`](_file.md), lines 525–536 · [local source](../../../../source/modules/node/node.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc#L525-L536)
- **Module/theme:** node

## Signature

```php
function node_delete_confirm($form, &$form_state, $node)
```

## Documentation

```text
Form constructor for the node deletion confirmation form.

@see node_delete_confirm_submit()
```

## Code

```php
function node_delete_confirm($form, &$form_state, $node) {
  $form['#node'] = $node;
  // Always provide entity id in the same form key as in the entity edit form.
  $form['nid'] = array('#type' => 'value', '#value' => $node->nid);
  return confirm_form($form,
    t('Are you sure you want to delete %title?', array('%title' => $node->title)),
    'node/' . $node->nid,
    t('This action cannot be undone.'),
    t('Delete'),
    t('Cancel')
  );
}
```

---
_Drupal 7.103 · [modules/node/node.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
