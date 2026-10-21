# path_form_node_form_alter()

- **Type:** Function
- **File:** [`modules/path/path.module`](_file.md), lines 99–146 · [local source](../../../../source/modules/path/path.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module#L99-L146)
- **Module/theme:** path
- **Implements:** [hook_form_BASE_FORM_ID_alter()](../../system/system.api.php/hook_form_BASE_FORM_ID_alter.md)

## Signature

```php
function path_form_node_form_alter(&$form, $form_state)
```

## Documentation

```text
Implements hook_form_BASE_FORM_ID_alter() for node_form().

@see path_form_element_validate()
```

## Code

```php
function path_form_node_form_alter(&$form, $form_state) {
  $path = array();
  if (!empty($form['#node']->nid)) {
    $conditions = array('source' => 'node/' . $form['#node']->nid);
    $langcode = entity_language('node', $form['#node']);
    if ($langcode != LANGUAGE_NONE) {
      $conditions['language'] = $langcode;
    }
    $path = path_load($conditions);
    if ($path === FALSE) {
      $path = array();
    }
  }
  $path += array(
    'pid' => NULL,
    'source' => isset($form['#node']->nid) ? 'node/' . $form['#node']->nid : NULL,
    'alias' => '',
    'language' => isset($langcode) ? $langcode : LANGUAGE_NONE,
  );

  $form['path'] = array(
    '#type' => 'fieldset',
    '#title' => t('URL path settings'),
    '#collapsible' => TRUE,
    '#collapsed' => empty($path['alias']),
    '#group' => 'additional_settings',
    '#attributes' => array(
      'class' => array('path-form'),
    ),
    '#attached' => array(
      'js' => array(drupal_get_path('module', 'path') . '/path.js'),
    ),
    '#access' => user_access('create url aliases') || user_access('administer url aliases'),
    '#weight' => 30,
    '#tree' => TRUE,
    '#element_validate' => array('path_form_element_validate'),
  );
  $form['path']['alias'] = array(
    '#type' => 'textfield',
    '#title' => t('URL alias'),
    '#default_value' => $path['alias'],
    '#maxlength' => 255,
    '#description' => t('Optionally specify an alternative URL by which this content can be accessed. For example, type "about" when writing an about page. Use a relative path and don\'t add a trailing slash or the URL alias won\'t work.'),
  );
  $form['path']['pid'] = array('#type' => 'value', '#value' => $path['pid']);
  $form['path']['source'] = array('#type' => 'value', '#value' => $path['source']);
  $form['path']['language'] = array('#type' => 'value', '#value' => $path['language']);
}
```

---
_Drupal 7.103 · [modules/path/path.module](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module) · Licensed GPL-2.0-or-later (see LICENSE)._
