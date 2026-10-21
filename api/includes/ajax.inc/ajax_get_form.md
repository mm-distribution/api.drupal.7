# ajax_get_form()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 323–366 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L323-L366)
- **Topics:** [ajax](../../topics/ajax.md)

## Signature

```php
function ajax_get_form()
```

## Documentation

```text
Gets a form submitted via #ajax during an Ajax callback.

This will load a form from the form cache used during Ajax operations. It
pulls the form info from $_POST.

@return
  An array containing the $form, $form_state, $form_id, $form_build_id and an
  initial list of Ajax $commands. Use the list() function to break these
  apart:
  @code
    list($form, $form_state, $form_id, $form_build_id, $commands) = ajax_get_form();
  @endcode
```

## Code

```php
function ajax_get_form() {
  $form_state = form_state_defaults();

  $form_build_id = (isset($_POST['form_build_id']) ? $_POST['form_build_id'] : '');

  // Get the form from the cache.
  $form = form_get_cache($form_build_id, $form_state);
  if (!$form) {
    // If $form cannot be loaded from the cache, the form_build_id in $_POST
    // must be invalid, which means that someone performed a POST request onto
    // system/ajax without actually viewing the concerned form in the browser.
    // This is likely a hacking attempt as it never happens under normal
    // circumstances, so we just do nothing.
    watchdog('ajax', 'Invalid form POST data.', array(), WATCHDOG_WARNING);
    drupal_exit();
  }

  // When a page level cache is enabled, the form-build id might have been
  // replaced from within form_get_cache. If this is the case, it is also
  // necessary to update it in the browser by issuing an appropriate Ajax
  // command.
  $commands = array();
  if (isset($form['#build_id_old']) && $form['#build_id_old'] != $form['#build_id']) {
    // If the form build ID has changed, issue an Ajax command to update it.
    $commands[] = ajax_command_update_build_id($form);
    $form_build_id = $form['#build_id'];
  }

  // Since some of the submit handlers are run, redirects need to be disabled.
  $form_state['no_redirect'] = TRUE;

  // When a form is rebuilt after Ajax processing, its #build_id and #action
  // should not change.
  // @see drupal_rebuild_form()
  $form_state['rebuild_info']['copy']['#build_id'] = TRUE;
  $form_state['rebuild_info']['copy']['#action'] = TRUE;

  // The form needs to be processed; prepare for that by setting a few internal
  // variables.
  $form_state['input'] = $_POST;
  $form_id = $form['#form_id'];

  return array($form, $form_state, $form_id, $form_build_id, $commands);
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
