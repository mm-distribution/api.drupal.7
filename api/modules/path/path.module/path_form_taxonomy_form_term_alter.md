# path_form_taxonomy_form_term_alter()

- **Type:** Function
- **File:** [`modules/path/path.module`](_file.md), lines 229–262 · [local source](../../../../source/modules/path/path.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module#L229-L262)
- **Module/theme:** path
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function path_form_taxonomy_form_term_alter(&$form, $form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter() for taxonomy_form_term().
```

## Code

```php
function path_form_taxonomy_form_term_alter(&$form, $form_state) {
  // Make sure this does not show up on the delete confirmation form.
  if (empty($form_state['confirm_delete'])) {
    $langcode = entity_language('taxonomy_term', (object) $form['#term']);
    $langcode = !empty($langcode) ? $langcode : LANGUAGE_NONE;
    $conditions = array('source' => 'taxonomy/term/' . $form['#term']['tid'], 'language' => $langcode);
    $path = (isset($form['#term']['tid']) ? path_load($conditions) : array());
    if ($path === FALSE) {
      $path = array();
    }
    $path += array(
      'pid' => NULL,
      'source' => isset($form['#term']['tid']) ? 'taxonomy/term/' . $form['#term']['tid'] : NULL,
      'alias' => '',
      'language' => $langcode,
    );
    $form['path'] = array(
      '#access' => user_access('create url aliases') || user_access('administer url aliases'),
      '#tree' => TRUE,
      '#element_validate' => array('path_form_element_validate'),
    );
    $form['path']['alias'] = array(
      '#type' => 'textfield',
      '#title' => t('URL alias'),
      '#default_value' => $path['alias'],
      '#maxlength' => 255,
      '#weight' => 0,
      '#description' => t("Optionally specify an alternative URL by which this term can be accessed. Use a relative path and don't add a trailing slash or the URL alias won't work."),
    );
    $form['path']['pid'] = array('#type' => 'value', '#value' => $path['pid']);
    $form['path']['source'] = array('#type' => 'value', '#value' => $path['source']);
    $form['path']['language'] = array('#type' => 'value', '#value' => $path['language']);
  }
}
```

---
_Drupal 7.103 · [modules/path/path.module](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module) · Licensed GPL-2.0-or-later (see LICENSE)._
