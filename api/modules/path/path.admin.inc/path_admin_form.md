# path_admin_form()

- **Type:** Function
- **File:** [`modules/path/path.admin.inc`](_file.md), lines 127–173 · [local source](../../../../source/modules/path/path.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc#L127-L173)
- **Module/theme:** path
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function path_admin_form($form, &$form_state, $path = array('source' => '', 'alias' => '', 'language' => LANGUAGE_NONE, 'pid' => NULL))
```

## Documentation

```text
Form constructor for the path administration form.

@param $path
  An array containing the path ID, source, alias, and language code.

@ingroup forms
@see path_admin_form_validate()
@see path_admin_form_submit()
@see path_admin_form_delete_submit()
```

## Code

```php
function path_admin_form($form, &$form_state, $path = array('source' => '', 'alias' => '', 'language' => LANGUAGE_NONE, 'pid' => NULL)) {
  $form['source'] = array(
    '#type' => 'textfield',
    '#title' => t('Existing system path'),
    '#default_value' => $path['source'],
    '#maxlength' => 255,
    '#size' => 45,
    '#description' => t('Specify the existing path you wish to alias. For example: node/28, forum/1, taxonomy/term/1.'),
    '#field_prefix' => url(NULL, array('absolute' => TRUE)) . (variable_get('clean_url', 0) ? '' : '?q='),
    '#required' => TRUE,
  );
  $form['alias'] = array(
    '#type' => 'textfield',
    '#title' => t('Path alias'),
    '#default_value' => $path['alias'],
    '#maxlength' => 255,
    '#size' => 45,
    '#description' => t('Specify an alternative path by which this data can be accessed. For example, type "about" when writing an about page. Use a relative path and don\'t add a trailing slash or the URL alias won\'t work.'),
    '#field_prefix' => url(NULL, array('absolute' => TRUE)) . (variable_get('clean_url', 0) ? '' : '?q='),
    '#required' => TRUE,
  );

  // This will be a hidden value unless locale module is enabled.
  $form['language'] = array(
    '#type' => 'value',
    '#value' => $path['language']
  );

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save'),
  );
  if ($path['pid']) {
    $form['pid'] = array(
      '#type' => 'hidden',
      '#value' => $path['pid'],
    );
    $form['actions']['delete'] = array(
      '#type' => 'submit',
      '#value' => t('Delete'),
      '#submit' => array('path_admin_form_delete_submit'),
    );
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/path/path.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
