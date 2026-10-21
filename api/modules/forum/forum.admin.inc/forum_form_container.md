# forum_form_container()

- **Type:** Function
- **File:** [`modules/forum/forum.admin.inc`](_file.md), lines 148–197 · [local source](../../../../source/modules/forum/forum.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.admin.inc#L148-L197)
- **Module/theme:** forum
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function forum_form_container($form, &$form_state, $edit = array())
```

## Documentation

```text
Form constructor for adding and editing forum containers.

@param $edit
  (optional) Associative array containing a container term to be added or edited.
  Defaults to an empty array.

@see forum_form_submit()
@ingroup forms
```

## Code

```php
function forum_form_container($form, &$form_state, $edit = array()) {
  $edit += array(
    'name' => '',
    'description' => '',
    'tid' => NULL,
    'weight' => 0,
  );
  // Handle a delete operation.
  $form['name'] = array(
    '#title' => t('Container name'),
    '#type' => 'textfield',
    '#default_value' => $edit['name'],
    '#maxlength' => 255,
    '#description' => t('Short but meaningful name for this collection of related forums.'),
    '#required' => TRUE
  );

  $form['description'] = array(
    '#type' => 'textarea',
    '#title' => t('Description'),
    '#default_value' => $edit['description'],
    '#description' => t('Description and guidelines for forums within this container.')
  );
  $form['parent']['#tree'] = TRUE;
  $form['parent'][0] = _forum_parent_select($edit['tid'], t('Parent'), 'container');
  $form['weight'] = array(
    '#type' => 'weight',
    '#title' => t('Weight'),
    '#default_value' => $edit['weight'],
    '#description' => t('Containers are displayed in ascending order by weight (containers with equal weights are displayed alphabetically).')
  );

  $form['vid'] = array(
    '#type' => 'hidden',
    '#value' => variable_get('forum_nav_vocabulary', ''),
  );
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save')
  );
  if ($edit['tid']) {
    $form['actions']['delete'] = array('#type' => 'submit', '#value' => t('Delete'));
    $form['tid'] = array('#type' => 'value', '#value' => $edit['tid']);
  }
  $form['#submit'][] = 'forum_form_submit';
  $form['#theme'] = 'forum_form';

  return $form;
}
```

---
_Drupal 7.103 · [modules/forum/forum.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
