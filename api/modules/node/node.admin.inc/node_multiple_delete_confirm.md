# node_multiple_delete_confirm()

- **Type:** Function
- **File:** [`modules/node/node.admin.inc`](_file.md), lines 665–686 · [local source](../../../../source/modules/node/node.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc#L665-L686)
- **Module/theme:** node
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function node_multiple_delete_confirm($form, &$form_state, $nodes)
```

## Documentation

```text
Multiple node deletion confirmation form for node_admin_content().

@see node_admin_nodes()
@see node_admin_nodes_submit()
@see node_admin_nodes_validate()
@see node_filter_form()
@see node_filter_form_submit()
@see node_multiple_delete_confirm_submit()
@ingroup forms
```

## Code

```php
function node_multiple_delete_confirm($form, &$form_state, $nodes) {
  $form['nodes'] = array('#prefix' => '<ul>', '#suffix' => '</ul>', '#tree' => TRUE);
  // array_filter returns only elements with TRUE values
  foreach ($nodes as $nid => $value) {
    $title = db_query('SELECT title FROM {node} WHERE nid = :nid', array(':nid' => $nid))->fetchField();
    $form['nodes'][$nid] = array(
      '#type' => 'hidden',
      '#value' => $nid,
      '#prefix' => '<li>',
      '#suffix' => check_plain($title) . "</li>\n",
    );
  }
  $form['operation'] = array('#type' => 'hidden', '#value' => 'delete');
  $form['#submit'][] = 'node_multiple_delete_confirm_submit';
  $confirm_question = format_plural(count($nodes),
                                  'Are you sure you want to delete this item?',
                                  'Are you sure you want to delete these items?');
  return confirm_form($form,
                    $confirm_question,
                    'admin/content', t('This action cannot be undone.'),
                    t('Delete'), t('Cancel'));
}
```

---
_Drupal 7.103 · [modules/node/node.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
