# shortcut_set_customize()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 266–313 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L266-L313)
- **Module/theme:** shortcut
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function shortcut_set_customize($form, &$form_state, $shortcut_set)
```

## Documentation

```text
Form callback: builds the form for customizing shortcut sets.

@param $form
  An associative array containing the structure of the form.
@param $form_state
  An associative array containing the current state of the form.
@param $shortcut_set
  An object representing the shortcut set which is being edited.

@return
  An array representing the form definition.

@ingroup forms
@see shortcut_set_customize_submit()
```

## Code

```php
function shortcut_set_customize($form, &$form_state, $shortcut_set) {
  $form['#shortcut_set_name'] = $shortcut_set->set_name;
  $form['shortcuts'] = array(
    '#tree' => TRUE,
    '#weight' => -20,
    'enabled' => array(),
    'disabled' => array(),
  );

  foreach ($shortcut_set->links as $link) {
    $mlid = $link['mlid'];
    $status = $link['hidden'] ? 'disabled' : 'enabled';
    $form['shortcuts'][$status][$mlid]['name']['#markup'] = l($link['link_title'], $link['link_path']);
    $form['shortcuts'][$status][$mlid]['weight'] = array(
      '#type' => 'weight',
      '#title' => t('Weight'),
      '#delta' => 50,
      '#default_value' => $link['weight'],
      '#attributes' => array('class' => array('shortcut-weight')),
    );
    $form['shortcuts'][$status][$mlid]['status'] = array(
      '#type' => 'select',
      '#title' => t('Status'),
      '#options' => array('disabled' => t('Disabled'), 'enabled' => t('Enabled')),
      '#default_value' => $status,
      '#attributes' => array('class' => array('shortcut-status-select')),
    );

    $form['shortcuts'][$status][$mlid]['edit']['#markup'] = l(t('edit'), 'admin/config/user-interface/shortcut/link/' . $mlid);
    $form['shortcuts'][$status][$mlid]['delete']['#markup'] = l(t('delete'), 'admin/config/user-interface/shortcut/link/' . $mlid . '/delete');
  }

  $form['#attached'] = array(
    'css' => array(drupal_get_path('module', 'shortcut') . '/shortcut.admin.css'),
    'js' => array(drupal_get_path('module', 'shortcut') . '/shortcut.admin.js'),
  );

  $form['actions'] = array(
    '#type' => 'actions',
    '#access' => !empty($shortcut_set->links),
  );
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save changes'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
