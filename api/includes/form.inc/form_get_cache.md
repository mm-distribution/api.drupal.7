# form_get_cache()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 517–552 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L517-L552)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_get_cache($form_build_id, &$form_state)
```

## Documentation

```text
Fetches a form from cache.
```

## Code

```php
function form_get_cache($form_build_id, &$form_state) {
  if ($cached = cache_get('form_' . $form_build_id, 'cache_form')) {
    $form = $cached->data;

    global $user;
    if ((isset($form['#cache_token']) && drupal_valid_token($form['#cache_token'])) || (!isset($form['#cache_token']) && !$user->uid)) {
      if ($cached = cache_get('form_state_' . $form_build_id, 'cache_form')) {
        // Re-populate $form_state for subsequent rebuilds.
        $form_state = $cached->data + $form_state;

        // If the original form is contained in include files, load the files.
        // @see form_load_include()
        $form_state['build_info'] += array('files' => array());
        foreach ($form_state['build_info']['files'] as $file) {
          if (is_array($file)) {
            $file += array('type' => 'inc', 'name' => $file['module']);
            module_load_include($file['type'], $file['module'], $file['name']);
          }
          elseif (file_exists($file)) {
            require_once DRUPAL_ROOT . '/' . $file;
          }
        }
      }
      // Generate a new #build_id if the cached form was rendered on a cacheable
      // page.
      if (!empty($form_state['build_info']['immutable'])) {
        $form['#build_id_old'] = $form['#build_id'];
        $form['#build_id'] = 'form-' . drupal_random_key();
        $form['form_build_id']['#value'] = $form['#build_id'];
        $form['form_build_id']['#id'] = $form['#build_id'];
        unset($form_state['build_info']['immutable']);
      }
      return $form;
    }
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
