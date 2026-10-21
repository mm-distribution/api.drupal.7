# search_form()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 958–1000 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L958-L1000)
- **Module/theme:** search
- **Topics:** [search](../../../topics/search.md)

## Signature

```php
function search_form($form, &$form_state, $action = '', $keys = '', $module = NULL, $prompt = NULL)
```

## Documentation

```text
Builds a search form.

@param $action
  Form action. Defaults to "search/$path", where $path is the search path
  associated with the module in its hook_search_info(). This will be
  run through url().
@param $keys
  The search string entered by the user, containing keywords for the search.
@param $module
  The search module to render the form for: a module that implements
  hook_search_info(). If not supplied, the default search module is used.
@param $prompt
  Label for the keywords field. Defaults to t('Enter your keywords') if NULL.
  Supply '' to omit.

@return
  A Form API array for the search form.
```

## Code

```php
function search_form($form, &$form_state, $action = '', $keys = '', $module = NULL, $prompt = NULL) {
  $module_info = FALSE;
  if (!$module) {
    $module_info = search_get_default_module_info();
  }
  else {
    $info = search_get_info();
    $module_info = isset($info[$module]) ? $info[$module] : FALSE;
  }

  // Sanity check.
  if (!$module_info) {
    form_set_error(NULL, t('Search is currently disabled.'), 'error');
    return $form;
  }

  if (!$action) {
    $action = 'search/' . $module_info['path'];
  }
  if (!isset($prompt)) {
    $prompt = t('Enter your keywords');
  }

  $form['#action'] = url($action);
  // Record the $action for later use in redirecting.
  $form_state['action'] = $action;
  $form['#attributes']['class'][] = 'search-form';
  $form['module'] = array('#type' => 'value', '#value' => $module);
  $form['basic'] = array('#type' => 'container', '#attributes' => array('class' => array('container-inline')));
  $form['basic']['keys'] = array(
    '#type' => 'textfield',
    '#title' => $prompt,
    '#default_value' => $keys,
    '#size' => $prompt ? 40 : 20,
    '#maxlength' => 255,
  );
  // processed_keys is used to coordinate keyword passing between other forms
  // that hook into the basic search form.
  $form['basic']['processed_keys'] = array('#type' => 'value', '#value' => '');
  $form['basic']['submit'] = array('#type' => 'submit', '#value' => t('Search'));

  return $form;
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
