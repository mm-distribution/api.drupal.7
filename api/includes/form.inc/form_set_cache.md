# form_set_cache()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 557–588 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L557-L588)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_set_cache($form_build_id, $form, $form_state)
```

## Documentation

```text
Stores a form in the cache.
```

## Code

```php
function form_set_cache($form_build_id, $form, $form_state) {
  // The default cache_form expiration is 6 hours. On busy sites, the cache_form
  // table can become very large. A shorter cache lifetime can help to keep the
  // table's size under control.
  $expire = variable_get('form_cache_expiration', 21600);

  // Ensure that the form build_id embedded in the form structure is the same as
  // the one passed in as a parameter. This is an additional safety measure to
  // prevent legacy code operating directly with form_get_cache and
  // form_set_cache from accidentally overwriting immutable form state.
  if ($form['#build_id'] != $form_build_id) {
    watchdog('form', 'Form build-id mismatch detected while attempting to store a form in the cache.', array(), WATCHDOG_ERROR);
    return;
  }

  // Cache form structure.
  if (isset($form)) {
    if ($GLOBALS['user']->uid) {
      $form['#cache_token'] = drupal_get_token();
    }
    unset($form['#build_id_old']);
    cache_set('form_' . $form_build_id, $form, 'cache_form', REQUEST_TIME + $expire);
  }

  // Cache form state.
  if (variable_get('cache', 0) && drupal_page_is_cacheable()) {
    $form_state['build_info']['immutable'] = TRUE;
  }
  if ($data = array_diff_key($form_state, array_flip(form_state_keys_no_cache()))) {
    cache_set('form_state_' . $form_build_id, $data, 'cache_form', REQUEST_TIME + $expire);
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
