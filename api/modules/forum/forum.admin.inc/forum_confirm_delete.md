# forum_confirm_delete()

- **Type:** Function
- **File:** [`modules/forum/forum.admin.inc`](_file.md), lines 208–215 · [local source](../../../../source/modules/forum/forum.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.admin.inc#L208-L215)
- **Module/theme:** forum
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function forum_confirm_delete($form, &$form_state, $tid)
```

## Documentation

```text
Form constructor for confirming deletion of a forum taxonomy term.

@param $tid
  ID of the term to be deleted.

@see forum_confirm_delete_submit()
@ingroup forms
```

## Code

```php
function forum_confirm_delete($form, &$form_state, $tid) {
  $term = taxonomy_term_load($tid);

  $form['tid'] = array('#type' => 'value', '#value' => $tid);
  $form['name'] = array('#type' => 'value', '#value' => $term->name);

  return confirm_form($form, t('Are you sure you want to delete the forum %name?', array('%name' => $term->name)), 'admin/structure/forum', t('Deleting a forum or container will also delete its sub-forums, if any. To delete posts in this forum, visit <a href="@content">content administration</a> first. This action cannot be undone.', array('@content' => url('admin/content'))), t('Delete'), t('Cancel'));
}
```

---
_Drupal 7.103 · [modules/forum/forum.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
