# profile_admin_overview()

- **Type:** Function
- **File:** [`modules/profile/profile.admin.inc`](_file.md), lines 14–75 · [local source](../../../../source/modules/profile/profile.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.admin.inc#L14-L75)
- **Module/theme:** profile
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function profile_admin_overview($form)
```

## Documentation

```text
Form builder to display a listing of all editable profile fields.

@ingroup forms
@see profile_admin_overview_submit()
```

## Code

```php
function profile_admin_overview($form) {
  $result = db_query('SELECT title, name, type, category, fid, weight FROM {profile_field} ORDER BY category, weight');

  $categories = array();
  foreach ($result as $field) {
    // Collect all category information
    $categories[] = $field->category;

    // Save all field information
    $form[$field->fid]['name'] = array('#markup' => check_plain($field->name));
    $form[$field->fid]['title'] = array('#markup' => check_plain($field->title));
    $form[$field->fid]['type'] = array('#markup' => $field->type);
    $form[$field->fid]['category'] = array(
      '#type' => 'select',
      '#title' => t('Category for @title', array('@title' => $field->title)),
      '#title_display' => 'invisible',
      '#default_value' => $field->category,
      '#options' => array(),
    );
    $form[$field->fid]['weight'] = array(
      '#type' => 'weight',
      '#title' => t('Weight for @title', array('@title' => $field->title)),
      '#title_display' => 'invisible',
      '#default_value' => $field->weight,
    );
    $form[$field->fid]['edit'] = array('#type' => 'link', '#title' => t('edit'), '#href' => "admin/config/people/profile/edit/$field->fid");
    $form[$field->fid]['delete'] = array('#type' => 'link', '#title' => t('delete'), '#href' => "admin/config/people/profile/delete/$field->fid");
  }

  // Add the category combo boxes
  $categories = array_unique($categories);
  foreach ($form as $fid => $field) {
    foreach ($categories as $cat => $category) {
      $form[$fid]['category']['#options'][$category] = $category;
    }
  }

  // Display the submit button only when there's more than one field
  if (count($form) > 1) {
    $form['actions'] = array('#type' => 'actions');
    $form['actions']['submit'] = array('#type' => 'submit', '#value' => t('Save configuration'));
  }
  else {
    // Disable combo boxes when there isn't a submit button
    foreach ($form as $fid => $field) {
      unset($form[$fid]['weight']);
      $form[$fid]['category']['#type'] = 'value';
    }
  }
  $form['#tree'] = TRUE;

  // @todo: Any reason this isn't done using an element with #theme = 'links'?
  $addnewfields = '<h2>' . t('Add new field') . '</h2>';
  $addnewfields .= '<ul>';
  foreach (_profile_field_types() as $key => $value) {
    $addnewfields .= '<li>' . l($value, "admin/config/people/profile/add/$key") . '</li>';
  }
  $addnewfields .= '</ul>';
  $form['addnewfields'] = array('#markup' => $addnewfields);

  return $form;
}
```

---
_Drupal 7.103 · [modules/profile/profile.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
