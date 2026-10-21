# aggregator_form_category()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.admin.inc`](_file.md), lines 549–568 · [local source](../../../../source/modules/aggregator/aggregator.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc#L549-L568)
- **Module/theme:** aggregator
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function aggregator_form_category($form, &$form_state, $edit = array('title' => '', 'description' => '', 'cid' => NULL))
```

## Documentation

```text
Form constructor to add/edit/delete aggregator categories.

@param $edit
  An associative array containing:
  - title: A string to use for the category title.
  - description: A string to use for the category description.
  - cid: The category ID.

@ingroup forms
@see aggregator_form_category_validate()
@see aggregator_form_category_submit()
```

## Code

```php
function aggregator_form_category($form, &$form_state, $edit = array('title' => '', 'description' => '', 'cid' => NULL)) {
  $form['title'] = array('#type' => 'textfield',
    '#title' => t('Title'),
    '#default_value' => $edit['title'],
    '#maxlength' => 64,
    '#required' => TRUE,
  );
  $form['description'] = array('#type' => 'textarea',
    '#title' => t('Description'),
    '#default_value' => $edit['description'],
  );
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array('#type' => 'submit', '#value' => t('Save'));
  if ($edit['cid']) {
    $form['actions']['delete'] = array('#type' => 'submit', '#value' => t('Delete'));
    $form['cid'] = array('#type' => 'hidden', '#value' => $edit['cid']);
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
