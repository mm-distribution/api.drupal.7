# authorize_filetransfer_form()

- **Type:** Function
- **File:** [`includes/authorize.inc`](_file.md), lines 17–128 · [local source](../../../source/includes/authorize.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/authorize.inc#L17-L128)
- **Topics:** [forms](../../topics/forms.md)

## Signature

```php
function authorize_filetransfer_form($form, &$form_state)
```

## Documentation

```text
Form constructor for the file transfer authorization form.

Allows the user to choose a FileTransfer type and supply credentials.

@see authorize_filetransfer_form_validate()
@see authorize_filetransfer_form_submit()
@ingroup forms
```

## Code

```php
function authorize_filetransfer_form($form, &$form_state) {
  global $base_url, $is_https;
  $form = array();

  // If possible, we want to post this form securely via HTTPS.
  $form['#https'] = TRUE;

  // CSS we depend on lives in modules/system/maintenance.css, which is loaded
  // via the default maintenance theme.
  $form['#attached']['js'][] = $base_url . '/misc/authorize.js';

  // Get all the available ways to transfer files.
  if (empty($_SESSION['authorize_filetransfer_info'])) {
    drupal_set_message(t('Unable to continue, no available methods of file transfer'), 'error');
    return array();
  }
  $available_backends = $_SESSION['authorize_filetransfer_info'];

  if (!$is_https) {
    $form['information']['https_warning'] = array(
      '#prefix' => '<div class="messages error">',
      '#markup' => t('WARNING: You are not using an encrypted connection, so your password will be sent in plain text. <a href="@https-link">Learn more</a>.', array('@https-link' => 'http://drupal.org/https-information')),
      '#suffix' => '</div>',
    );
  }

  // Decide on a default backend.
  if (isset($form_state['values']['connection_settings']['authorize_filetransfer_default'])) {
    $authorize_filetransfer_default = $form_state['values']['connection_settings']['authorize_filetransfer_default'];
  }
  elseif ($authorize_filetransfer_default = variable_get('authorize_filetransfer_default', NULL));
  else {
    $authorize_filetransfer_default = key($available_backends);
  }

  $form['information']['main_header'] = array(
    '#prefix' => '<h3>',
    '#markup' => t('To continue, provide your server connection details'),
    '#suffix' => '</h3>',
  );

  $form['connection_settings']['#tree'] = TRUE;
  $form['connection_settings']['authorize_filetransfer_default'] = array(
    '#type' => 'select',
    '#title' => t('Connection method'),
    '#default_value' => $authorize_filetransfer_default,
    '#weight' => -10,
  );

  /*
   * Here we create two submit buttons. For a JS enabled client, they will
   * only ever see submit_process. However, if a client doesn't have JS
   * enabled, they will see submit_connection on the first form (when picking
   * what filetransfer type to use, and submit_process on the second one (which
   * leads to the actual operation).
   */
  $form['submit_connection'] = array(
    '#prefix' => "<br style='clear:both'/>",
    '#name' => 'enter_connection_settings',
    '#type' => 'submit',
    '#value' => t('Enter connection settings'),
    '#weight' => 100,
  );

  $form['submit_process'] = array(
    '#name' => 'process_updates',
    '#type' => 'submit',
    '#value' => t('Continue'),
    '#weight' => 100,
    '#attributes' => array('style' => 'display:none'),
  );

  // Build a container for each connection type.
  foreach ($available_backends as $name => $backend) {
    $form['connection_settings']['authorize_filetransfer_default']['#options'][$name] = $backend['title'];
    $form['connection_settings'][$name] = array(
      '#type' => 'container',
      '#attributes' => array('class' => array("filetransfer-$name", 'filetransfer')),
    );
    // We can't use #prefix on the container itself since then the header won't
    // be hidden and shown when the containers are being manipulated via JS.
    $form['connection_settings'][$name]['header'] = array(
      '#markup' => '<h4>' . t('@backend connection settings', array('@backend' => $backend['title'])) . '</h4>',
    );

    $form['connection_settings'][$name] += _authorize_filetransfer_connection_settings($name);

    // Start non-JS code.
    if (isset($form_state['values']['connection_settings']['authorize_filetransfer_default']) && $form_state['values']['connection_settings']['authorize_filetransfer_default'] == $name) {

      // Change the submit button to the submit_process one.
      $form['submit_process']['#attributes'] = array();
      unset($form['submit_connection']);

      // Activate the proper filetransfer settings form.
      $form['connection_settings'][$name]['#attributes']['style'] = 'display:block';
      // Disable the select box.
      $form['connection_settings']['authorize_filetransfer_default']['#disabled'] = TRUE;

      // Create a button for changing the type of connection.
      $form['connection_settings']['change_connection_type'] = array(
        '#name' => 'change_connection_type',
        '#type' => 'submit',
        '#value' => t('Change connection type'),
        '#weight' => -5,
        '#attributes' => array('class' => array('filetransfer-change-connection-type')),
      );
    }
    // End non-JS code.
  }
  return $form;
}
```

---
_Drupal 7.103 · [includes/authorize.inc](https://github.com/drupal/drupal/blob/7.103/includes/authorize.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
