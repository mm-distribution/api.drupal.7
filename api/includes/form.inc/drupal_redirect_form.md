# drupal_redirect_form()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 1294–1323 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L1294-L1323)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function drupal_redirect_form($form_state)
```

## Documentation

```text
Redirects the user to a URL after a form has been processed.

After a form is submitted and processed, normally the user should be
redirected to a new destination page. This function figures out what that
destination should be, based on the $form_state array and the 'destination'
query string in the request URL, and redirects the user there.

Usually (for exceptions, see below) $form_state['redirect'] determines where
to redirect the user. This can be set either to a string (the path to
redirect to), or an array of arguments for drupal_goto(). If
$form_state['redirect'] is missing, the user is usually (again, see below for
exceptions) redirected back to the page they came from, where they should see
a fresh, unpopulated copy of the form.

Here is an example of how to set up a form to redirect to the path 'node':
@code
$form_state['redirect'] = 'node';
@endcode
And here is an example of how to redirect to 'node/123?foo=bar#baz':
@code
$form_state['redirect'] = array(
  'node/123',
  array(
    'query' => array(
      'foo' => 'bar',
    ),
    'fragment' => 'baz',
  ),
);
@endcode

There are several exceptions to the "usual" behavior described above:
- If $form_state['programmed'] is TRUE, the form submission was usually
  invoked via drupal_form_submit(), so any redirection would break the script
  that invoked drupal_form_submit() and no redirection is done.
- If $form_state['rebuild'] is TRUE, the form is being rebuilt, and no
  redirection is done.
- If $form_state['no_redirect'] is TRUE, redirection is disabled. This is
  set, for instance, by ajax_get_form() to prevent redirection in Ajax
  callbacks. $form_state['no_redirect'] should never be set or altered by
  form builder functions or form validation/submit handlers.
- If $form_state['redirect'] is set to FALSE, redirection is disabled.
- If none of the above conditions has prevented redirection, then the
  redirect is accomplished by calling drupal_goto(), passing in the value of
  $form_state['redirect'] if it is set, or the current path if it is
  not. drupal_goto() preferentially uses the value of $_GET['destination']
  (the 'destination' URL query string) if it is present, so this will
  override any values set by $form_state['redirect']. Note that during
  installation, install_goto() is called in place of drupal_goto().

@param $form_state
  An associative array containing the current state of the form.

@see drupal_process_form()
@see drupal_build_form()
```

## Code

```php
function drupal_redirect_form($form_state) {
  // Skip redirection for form submissions invoked via drupal_form_submit().
  if (!empty($form_state['programmed'])) {
    return;
  }
  // Skip redirection if rebuild is activated.
  if (!empty($form_state['rebuild'])) {
    return;
  }
  // Skip redirection if it was explicitly disallowed.
  if (!empty($form_state['no_redirect'])) {
    return;
  }
  // Only invoke drupal_goto() if redirect value was not set to FALSE.
  if (!isset($form_state['redirect']) || $form_state['redirect'] !== FALSE) {
    if (isset($form_state['redirect'])) {
      if (is_array($form_state['redirect'])) {
        call_user_func_array('drupal_goto', $form_state['redirect']);
      }
      else {
        // This function can be called from the installer, which guarantees
        // that $redirect will always be a string, so catch that case here
        // and use the appropriate redirect function.
        $function = drupal_installation_attempted() ? 'install_goto' : 'drupal_goto';
        $function($form_state['redirect']);
      }
    }
    drupal_goto(current_path(), array('query' => drupal_get_query_parameters()));
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
