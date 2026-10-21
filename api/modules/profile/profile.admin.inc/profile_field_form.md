# profile_field_form()

- **Type:** Function
- **File:** [`modules/profile/profile.admin.inc`](_file.md), lines 187–305 · [local source](../../../../source/modules/profile/profile.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.admin.inc#L187-L305)
- **Module/theme:** profile
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function profile_field_form($form, &$form_state, $arg = NULL)
```

## Documentation

```text
Menu callback: Generate a form to add/edit a user profile field.

@ingroup forms
@see profile_field_form_validate()
@see profile_field_form_submit()
```

## Code

```php
function profile_field_form($form, &$form_state, $arg = NULL) {
  if (arg(4) == 'edit') {
    if (is_numeric($arg)) {
      $fid = $arg;

      $edit = db_query('SELECT * FROM {profile_field} WHERE fid = :fid', array('fid' => $fid))->fetchAssoc();

      if (!$edit) {
        drupal_not_found();
        return;
      }
      drupal_set_title(t('Edit %title', array('%title' => $edit['title'])), PASS_THROUGH);
      $form['fid'] = array('#type' => 'value',
        '#value' => $fid,
      );
      $type = $edit['type'];
    }
    else {
      drupal_not_found();
      return;
    }
  }
  else {
    $types = _profile_field_types();
    if (!isset($types[$arg])) {
      drupal_not_found();
      return;
    }
    $type = $arg;
    drupal_set_title(t('Add new %type', array('%type' => $types[$type])), PASS_THROUGH);
    $edit = array('name' => 'profile_');
    $form['type'] = array('#type' => 'value', '#value' => $type);
  }
  $edit += array(
    'category' => '',
    'title' => '',
    'explanation' => '',
    'weight' => 0,
    'page' => '',
    'autocomplete' => '',
    'required' => '',
    'register' => '',
  );
  $form['category'] = array('#type' => 'textfield',
    '#title' => t('Category'),
    '#default_value' => $edit['category'],
    '#autocomplete_path' => 'admin/config/people/profile/autocomplete',
    '#description' => t('The category the new field should be part of. Categories are used to group fields logically. An example category is "Personal information".'),
    '#required' => TRUE,
  );
  $form['title'] = array('#type' => 'textfield',
    '#title' => t('Title'),
    '#default_value' => $edit['title'],
    '#description' => t('The title of the new field. The title will be shown to the user. An example title is "Favorite color".'),
    '#required' => TRUE,
  );
  $form['name'] = array('#type' => 'textfield',
    '#title' => t('Form name'),
    '#default_value' => $edit['name'],
    '#description' => t('The name of the field. The form name is not shown to the user but used internally in the HTML code and URLs.
Unless you know what you are doing, it is highly recommended that you prefix the form name with <code>profile_</code> to avoid name clashes with other fields. Spaces or any other special characters except dash (-) and underscore (_) are not allowed. An example name is "profile_favorite_color" or perhaps just "profile_color".'),
    '#required' => TRUE,
  );
  $form['explanation'] = array('#type' => 'textarea',
    '#title' => t('Explanation'),
    '#default_value' => $edit['explanation'],
    '#description' => t('An optional explanation to go with the new field. The explanation will be shown to the user.'),
  );
  if ($type == 'selection') {
    $form['fields']['options'] = array('#type' => 'textarea',
      '#title' => t('Selection options'),
      '#default_value' => isset($edit['options']) ? $edit['options'] : '',
      '#description' => t('A list of all options. Put each option on a separate line. Example options are "red", "blue", "green", etc.'),
    );
  }
  $form['visibility'] = array('#type' => 'radios',
    '#title' => t('Visibility'),
    '#default_value' => isset($edit['visibility']) ? $edit['visibility'] : PROFILE_PUBLIC,
    '#options' => array(PROFILE_HIDDEN => t('Hidden profile field, only accessible by administrators, modules and themes.'), PROFILE_PRIVATE => t('Private field, content only available to privileged users.'), PROFILE_PUBLIC => t('Public field, content shown on profile page but not used on member list pages.'), PROFILE_PUBLIC_LISTINGS => t('Public field, content shown on profile page and on member list pages.')),
  );
  if ($type == 'selection' || $type == 'list' || $type == 'textfield') {
    $form['fields']['page'] = array('#type' => 'textfield',
      '#title' => t('Page title'),
      '#default_value' => $edit['page'],
      '#description' => t('To enable browsing this field by value, enter a title for the resulting page. The word <code>%value</code> will be substituted with the corresponding value. An example page title is "People whose favorite color is %value" . This is only applicable for a public field.'),
    );
  }
  elseif ($type == 'checkbox') {
    $form['fields']['page'] = array('#type' => 'textfield',
      '#title' => t('Page title'),
      '#default_value' => $edit['page'],
      '#description' => t('To enable browsing this field by value, enter a title for the resulting page. An example page title is "People who are employed" . This is only applicable for a public field.'),
    );
  }
  $form['weight'] = array('#type' => 'weight',
    '#title' => t('Weight'),
    '#default_value' => $edit['weight'],
    '#description' => t('The weights define the order in which the form fields are shown. Lighter fields "float up" towards the top of the category.'),
  );
  $form['autocomplete'] = array('#type' => 'checkbox',
    '#title' => t('Form will auto-complete while user is typing.'),
    '#default_value' => $edit['autocomplete'],
    '#description' => t('For security, auto-complete will be disabled if the user does not have access to user profiles.'),
  );
  $form['required'] = array('#type' => 'checkbox',
    '#title' => t('The user must enter a value.'),
    '#default_value' => $edit['required'],
  );
  $form['register'] = array('#type' => 'checkbox',
    '#title' => t('Visible in user registration form.'),
    '#default_value' => $edit['register'],
  );

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array('#type' => 'submit',
    '#value' => t('Save field'),
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/profile/profile.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
