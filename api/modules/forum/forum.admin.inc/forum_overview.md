# forum_overview()

- **Type:** Function
- **File:** [`modules/forum/forum.admin.inc`](_file.md), lines 270–300 · [local source](../../../../source/modules/forum/forum.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.admin.inc#L270-L300)
- **Module/theme:** forum
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function forum_overview($form, &$form_state)
```

## Documentation

```text
Form constructor for the forum overview form.

Returns a form for controlling the hierarchy of existing forums and
containers.

@see forum_menu()
@ingroup forms
```

## Code

```php
function forum_overview($form, &$form_state) {
  module_load_include('inc', 'taxonomy', 'taxonomy.admin');

  $vid = variable_get('forum_nav_vocabulary', '');
  $vocabulary = taxonomy_vocabulary_load($vid);
  $form = taxonomy_overview_terms($form, $form_state, $vocabulary);

  foreach (element_children($form) as $key) {
    if (isset($form[$key]['#term'])) {
      $term = $form[$key]['#term'];
      $form[$key]['view']['#href'] = 'forum/' . $term['tid'];
      if (in_array($form[$key]['#term']['tid'], variable_get('forum_containers', array()))) {
        $form[$key]['edit']['#title'] = t('edit container');
        $form[$key]['edit']['#href'] = 'admin/structure/forum/edit/container/' . $term['tid'];
      }
      else {
        $form[$key]['edit']['#title'] = t('edit forum');
        $form[$key]['edit']['#href'] = 'admin/structure/forum/edit/forum/' . $term['tid'];
      }
    }
  }

  // Remove the alphabetical reset.
  unset($form['actions']['reset_alphabetical']);

  // The form needs to have submit and validate handlers set explicitly.
  $form['#theme'] = 'taxonomy_overview_terms';
  $form['#submit'] = array('taxonomy_overview_terms_submit'); // Use the existing taxonomy overview submit handler.
  $form['#empty_text'] = t('No containers or forums available. <a href="@container">Add container</a> or <a href="@forum">Add forum</a>.', array('@container' => url('admin/structure/forum/add/container'), '@forum' => url('admin/structure/forum/add/forum')));
  return $form;
}
```

---
_Drupal 7.103 · [modules/forum/forum.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
