# drupal_prepare_form()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 1007–1132 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L1007-L1132)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function drupal_prepare_form($form_id, &$form, &$form_state)
```

## Documentation

```text
Prepares a structured form array.

Adds required elements, executes any hook_form_alter functions, and
optionally inserts a validation token to prevent tampering.

@param $form_id
  A unique string identifying the form for validation, submission,
  theming, and hook_form_alter functions.
@param $form
  An associative array containing the structure of the form.
@param $form_state
  A keyed array containing the current state of the form. Passed
  in here so that hook_form_alter() calls can use it, as well.
```

## Code

```php
function drupal_prepare_form($form_id, &$form, &$form_state) {
  global $user;

  $form['#type'] = 'form';
  $form_state['programmed'] = isset($form_state['programmed']) ? $form_state['programmed'] : FALSE;

  // Fix the form method, if it is 'get' in $form_state, but not in $form.
  if ($form_state['method'] == 'get' && !isset($form['#method'])) {
    $form['#method'] = 'get';
  }

  // Generate a new #build_id for this form, if none has been set already. The
  // form_build_id is used as key to cache a particular build of the form. For
  // multi-step forms, this allows the user to go back to an earlier build, make
  // changes, and re-submit.
  // @see drupal_build_form()
  // @see drupal_rebuild_form()
  if (!isset($form['#build_id'])) {
    $form['#build_id'] = 'form-' . drupal_random_key();
  }
  $form['form_build_id'] = array(
    '#type' => 'hidden',
    '#value' => $form['#build_id'],
    '#id' => $form['#build_id'],
    '#name' => 'form_build_id',
    // Form processing and validation requires this value, so ensure the
    // submitted form value appears literally, regardless of custom #tree
    // and #parents being set elsewhere.
    '#parents' => array('form_build_id'),
  );

  // Add a token, based on either #token or form_id, to any form displayed to
  // authenticated users. This ensures that any submitted form was actually
  // requested previously by the user and protects against cross site request
  // forgeries.
  // This does not apply to programmatically submitted forms. Furthermore, since
  // tokens are session-bound and forms displayed to anonymous users are very
  // likely cached, we cannot assign a token for them.
  // During installation, there is no $user yet.
  if (!empty($user->uid) && !$form_state['programmed']) {
    // Form constructors may explicitly set #token to FALSE when cross site
    // request forgery is irrelevant to the form, such as search forms.
    if (isset($form['#token']) && $form['#token'] === FALSE) {
      unset($form['#token']);
    }
    // Otherwise, generate a public token based on the form id.
    else {
      $form['#token'] = $form_id;
      $form['form_token'] = array(
        '#id' => drupal_html_id('edit-' . $form_id . '-form-token'),
        '#type' => 'token',
        '#default_value' => drupal_get_token($form['#token']),
        // Form processing and validation requires this value, so ensure the
        // submitted form value appears literally, regardless of custom #tree
        // and #parents being set elsewhere.
        '#parents' => array('form_token'),
      );
    }
  }

  if (isset($form_id)) {
    $form['form_id'] = array(
      '#type' => 'hidden',
      '#value' => $form_id,
      '#id' => drupal_html_id("edit-$form_id"),
      // Form processing and validation requires this value, so ensure the
      // submitted form value appears literally, regardless of custom #tree
      // and #parents being set elsewhere.
      '#parents' => array('form_id'),
    );
  }
  if (!isset($form['#id'])) {
    $form['#id'] = drupal_html_id($form_id);
  }

  $form += element_info('form');
  $form += array('#tree' => FALSE, '#parents' => array());

  if (!isset($form['#validate'])) {
    // Ensure that modules can rely on #validate being set.
    $form['#validate'] = array();
    // Check for a handler specific to $form_id.
    if (function_exists($form_id . '_validate')) {
      $form['#validate'][] = $form_id . '_validate';
    }
    // Otherwise check whether this is a shared form and whether there is a
    // handler for the shared $form_id.
    elseif (isset($form_state['build_info']['base_form_id']) && function_exists($form_state['build_info']['base_form_id'] . '_validate')) {
      $form['#validate'][] = $form_state['build_info']['base_form_id'] . '_validate';
    }
  }

  if (!isset($form['#submit'])) {
    // Ensure that modules can rely on #submit being set.
    $form['#submit'] = array();
    // Check for a handler specific to $form_id.
    if (function_exists($form_id . '_submit')) {
      $form['#submit'][] = $form_id . '_submit';
    }
    // Otherwise check whether this is a shared form and whether there is a
    // handler for the shared $form_id.
    elseif (isset($form_state['build_info']['base_form_id']) && function_exists($form_state['build_info']['base_form_id'] . '_submit')) {
      $form['#submit'][] = $form_state['build_info']['base_form_id'] . '_submit';
    }
  }

  // If no #theme has been set, automatically apply theme suggestions.
  // theme_form() itself is in #theme_wrappers and not #theme. Therefore, the
  // #theme function only has to care for rendering the inner form elements,
  // not the form itself.
  if (!isset($form['#theme'])) {
    $form['#theme'] = array($form_id);
    if (isset($form_state['build_info']['base_form_id'])) {
      $form['#theme'][] = $form_state['build_info']['base_form_id'];
    }
  }

  // Invoke hook_form_alter(), hook_form_BASE_FORM_ID_alter(), and
  // hook_form_FORM_ID_alter() implementations.
  $hooks = array('form');
  if (isset($form_state['build_info']['base_form_id'])) {
    $hooks[] = 'form_' . $form_state['build_info']['base_form_id'];
  }
  $hooks[] = 'form_' . $form_id;
  drupal_alter($hooks, $form, $form_state, $form_id);
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
