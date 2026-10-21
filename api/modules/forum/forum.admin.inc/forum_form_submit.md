# forum_form_submit()

- **Type:** Function
- **File:** [`modules/forum/forum.admin.inc`](_file.md), lines 90–120 · [local source](../../../../source/modules/forum/forum.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.admin.inc#L90-L120)
- **Module/theme:** forum

## Signature

```php
function forum_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for forum_form_forum() and forum_form_container().
```

## Code

```php
function forum_form_submit($form, &$form_state) {
  if ($form['form_id']['#value'] == 'forum_form_container') {
    $container = TRUE;
    $type = t('forum container');
  }
  else {
    $container = FALSE;
    $type = t('forum');
  }

  $term = (object) $form_state['values'];
  $status = taxonomy_term_save($term);
  switch ($status) {
    case SAVED_NEW:
      if ($container) {
        $containers = variable_get('forum_containers', array());
        $containers[] = $term->tid;
        variable_set('forum_containers', $containers);
      }
      $form_state['values']['tid'] = $term->tid;
      drupal_set_message(t('Created new @type %term.', array('%term' => $form_state['values']['name'], '@type' => $type)));
      break;
    case SAVED_UPDATED:
      drupal_set_message(t('The @type %term has been updated.', array('%term' => $form_state['values']['name'], '@type' => $type)));
      // Clear the page and block caches to avoid stale data.
      cache_clear_all();
      break;
  }
  $form_state['redirect'] = 'admin/structure/forum';
  return;
}
```

---
_Drupal 7.103 · [modules/forum/forum.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
