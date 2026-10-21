# _shortcut_link_form_elements()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 466–507 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L466-L507)
- **Module/theme:** shortcut

## Signature

```php
function _shortcut_link_form_elements($shortcut_link = NULL)
```

## Documentation

```text
Helper function for building a form for adding or editing shortcut links.

@param $shortcut_link
  (optional) An array representing the shortcut link that will be edited. If
  not provided, a new link will be created.

@return
  An array of form elements.
```

## Code

```php
function _shortcut_link_form_elements($shortcut_link = NULL) {
  if (!isset($shortcut_link)) {
    $shortcut_link = array(
      'link_title' => '',
      'link_path' => ''
    );
  }
  else {
    $shortcut_link['link_path'] = ($shortcut_link['link_path'] == '<front>') ? '' : drupal_get_path_alias($shortcut_link['link_path']);
  }

  $form['shortcut_link']['#tree'] = TRUE;
  $form['shortcut_link']['link_title'] = array(
    '#type' => 'textfield',
    '#title' => t('Name'),
    '#description' => t('The name of the shortcut.'),
    '#size' => 40,
    '#maxlength' => 255,
    '#default_value' => $shortcut_link['link_title'],
    '#required' => TRUE,
  );

  $form['shortcut_link']['link_path'] = array(
    '#type' => 'textfield',
    '#title' => t('Path'),
    '#description' => t('The path to the shortcut.'),
    '#size' => 40,
    '#maxlength' => 255,
    '#field_prefix' => url(NULL, array('absolute' => TRUE)) . (variable_get('clean_url', 0) ? '' : '?q='),
    '#default_value' => $shortcut_link['link_path'],
  );

  $form['#validate'][] = 'shortcut_link_edit_validate';

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
