# node_revision_revert_confirm()

- **Type:** Function
- **File:** [`modules/node/node.pages.inc`](_file.md), lines 627–630 · [local source](../../../../source/modules/node/node.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc#L627-L630)
- **Module/theme:** node
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function node_revision_revert_confirm($form, $form_state, $node_revision)
```

## Documentation

```text
Asks for confirmation of the reversion to prevent against CSRF attacks.

@param int $node_revision
  The node revision ID.

@return array
  An array as expected by drupal_render().

@see node_menu()
@see node_revision_revert_confirm_submit()
@ingroup forms
```

## Code

```php
function node_revision_revert_confirm($form, $form_state, $node_revision) {
  $form['#node_revision'] = $node_revision;
  return confirm_form($form, t('Are you sure you want to revert to the revision from %revision-date?', array('%revision-date' => format_date($node_revision->revision_timestamp))), 'node/' . $node_revision->nid . '/revisions', '', t('Revert'), t('Cancel'));
}
```

---
_Drupal 7.103 · [modules/node/node.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
