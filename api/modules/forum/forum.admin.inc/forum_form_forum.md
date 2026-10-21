# forum_form_forum()

- **Type:** Function
- **File:** [`modules/forum/forum.admin.inc`](_file.md), lines 47–85 · [local source](../../../../source/modules/forum/forum.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.admin.inc#L47-L85)
- **Module/theme:** forum
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function forum_form_forum($form, &$form_state, $edit = array())
```

## Documentation

```text
Form constructor for adding and editing a forum.

@param $edit
  (optional) Associative array containing a forum term to be added or edited.
  Defaults to an empty array.

@see forum_form_submit()
@ingroup forms
```

## Code

```php
function forum_form_forum($form, &$form_state, $edit = array()) {
  $edit += array(
    'name' => '',
    'description' => '',
    'tid' => NULL,
    'weight' => 0,
  );
  $form['name'] = array('#type' => 'textfield',
    '#title' => t('Forum name'),
    '#default_value' => $edit['name'],
    '#maxlength' => 255,
    '#description' => t('Short but meaningful name for this collection of threaded discussions.'),
    '#required' => TRUE,
  );
  $form['description'] = array('#type' => 'textarea',
    '#title' => t('Description'),
    '#default_value' => $edit['description'],
    '#description' => t('Description and guidelines for discussions within this forum.'),
  );
  $form['parent']['#tree'] = TRUE;
  $form['parent'][0] = _forum_parent_select($edit['tid'], t('Parent'), 'forum');
  $form['weight'] = array('#type' => 'weight',
    '#title' => t('Weight'),
    '#default_value' => $edit['weight'],
    '#description' => t('Forums are displayed in ascending order by weight (forums with equal weights are displayed alphabetically).'),
  );

  $form['vid'] = array('#type' => 'hidden', '#value' => variable_get('forum_nav_vocabulary', ''));
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array('#type' => 'submit', '#value' => t('Save'));
  if ($edit['tid']) {
    $form['actions']['delete'] = array('#type' => 'submit', '#value' => t('Delete'));
    $form['tid'] = array('#type' => 'hidden', '#value' => $edit['tid']);
  }
  $form['#submit'][] = 'forum_form_submit';
  $form['#theme'] = 'forum_form';

  return $form;
}
```

---
_Drupal 7.103 · [modules/forum/forum.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
