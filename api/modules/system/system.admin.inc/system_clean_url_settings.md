# system_clean_url_settings()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2258–2340 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2258-L2340)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_clean_url_settings($form, &$form_state)
```

## Documentation

```text
Form builder; Configure clean URL settings.

@ingroup forms
@see system_settings_form()
```

## Code

```php
function system_clean_url_settings($form, &$form_state) {
  $available = FALSE;
  $conflict = FALSE;

  // If the request URI is a clean URL, clean URLs must be available.
  // Otherwise, run a test.
  if (strpos(request_uri(), '?q=') === FALSE && strpos(request_uri(), '&q=') === FALSE) {
    $available = TRUE;
  }
  else {
    $request = drupal_http_request($GLOBALS['base_url'] . '/admin/config/search/clean-urls/check');
    // If the request returns HTTP 200, clean URLs are available.
    if (isset($request->code) && $request->code == 200) {
      $available = TRUE;
      // If the user started the clean URL test, provide explicit feedback.
      if (isset($form_state['input']['clean_url_test_execute'])) {
        drupal_set_message(t('The clean URL test passed.'));
      }
    }
    else {
      // If the test failed while clean URLs are enabled, make sure clean URLs
      // can be disabled.
      if (variable_get('clean_url', 0)) {
        $conflict = TRUE;
        // Warn the user of a conflicting situation, unless after processing
        // a submitted form.
        if (!isset($form_state['input']['op'])) {
          drupal_set_message(t('Clean URLs are enabled, but the clean URL test failed. Uncheck the box below to disable clean URLs.'), 'warning');
        }
      }
      // If the user started the clean URL test, provide explicit feedback.
      elseif (isset($form_state['input']['clean_url_test_execute'])) {
        drupal_set_message(t('The clean URL test failed.'), 'warning');
      }
    }
  }

  // Show the enable/disable form if clean URLs are available or if the user
  // must be able to resolve a conflicting setting.
  if ($available || $conflict) {
    $form['clean_url'] = array(
      '#type' => 'checkbox',
      '#title' => t('Enable clean URLs'),
      '#default_value' => variable_get('clean_url', 0),
      '#description' => t('Use URLs like <code>example.com/user</code> instead of <code>example.com/?q=user</code>.'),
    );
    $form = system_settings_form($form);
    if ($conflict) {
      // $form_state['redirect'] needs to be set to the non-clean URL,
      // otherwise the setting is not saved.
      $form_state['redirect'] = url('', array('query' => array('q' => '/admin/config/search/clean-urls')));
    }
  }
  // Show the clean URLs test form.
  else {
    drupal_add_js(drupal_get_path('module', 'system') . '/system.js');

    $form_state['redirect'] = url('admin/config/search/clean-urls');
    $form['clean_url_description'] = array(
      '#type' => 'markup',
      '#markup' => '<p>' . t('Use URLs like <code>example.com/user</code> instead of <code>example.com/?q=user</code>.') . '</p>',
    );
    // Explain why the user is seeing this page and what to expect after
    // clicking the 'Run the clean URL test' button.
    $form['clean_url_test_result'] = array(
      '#type' => 'markup',
      '#markup' => '<p>' . t('Clean URLs cannot be enabled. If you are directed to this page or to a <em>Page not found (404)</em> error after testing for clean URLs, see the <a href="@handbook">online handbook</a>.', array('@handbook' => 'http://drupal.org/node/15365')) . '</p>',
    );
    $form['actions'] = array(
      '#type' => 'actions',
      'clean_url_test' => array(
        '#type' => 'submit',
        '#value' => t('Run the clean URL test'),
      ),
    );
    $form['clean_url_test_execute'] = array(
      '#type' => 'hidden',
      '#value' => 1,
    );
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
