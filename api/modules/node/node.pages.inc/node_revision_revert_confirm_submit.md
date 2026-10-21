# node_revision_revert_confirm_submit()

- **Type:** Function
- **File:** [`modules/node/node.pages.inc`](_file.md), lines 635–645 · [local source](../../../../source/modules/node/node.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc#L635-L645)
- **Module/theme:** node

## Signature

```php
function node_revision_revert_confirm_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for node_revision_revert_confirm().
```

## Code

```php
function node_revision_revert_confirm_submit($form, &$form_state) {
  $node_revision = $form['#node_revision'];
  $node_revision->revision = 1;
  $node_revision->log = t('Copy of the revision from %date.', array('%date' => format_date($node_revision->revision_timestamp)));

  node_save($node_revision);

  watchdog('content', '@type: reverted %title revision %revision.', array('@type' => $node_revision->type, '%title' => $node_revision->title, '%revision' => $node_revision->vid));
  drupal_set_message(t('@type %title has been reverted back to the revision from %revision-date.', array('@type' => node_type_get_name($node_revision), '%title' => $node_revision->title, '%revision-date' => format_date($node_revision->revision_timestamp))));
  $form_state['redirect'] = 'node/' . $node_revision->nid . '/revisions';
}
```

---
_Drupal 7.103 · [modules/node/node.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
