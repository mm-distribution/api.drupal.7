# system_theme_settings()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 399–603 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L399-L603)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_theme_settings($form, &$form_state, $key = '')
```

## Documentation

```text
Form builder; display theme configuration for entire site and individual themes.

@param $key
  A theme name.
@return
  The form structure.
@ingroup forms
@see system_theme_settings_submit()
```

## Code

```php
function system_theme_settings($form, &$form_state, $key = '') {
  // Default settings are defined in theme_get_setting() in includes/theme.inc
  if ($key) {
    $var = 'theme_' . $key . '_settings';
    $themes = list_themes();
    $features = $themes[$key]->info['features'];
  }
  else {
    $var = 'theme_settings';
  }

  $form['var'] = array('#type' => 'hidden', '#value' => $var);

  // Toggle settings
  $toggles = array(
    'logo'                      => t('Logo'),
    'name'                      => t('Site name'),
    'slogan'                    => t('Site slogan'),
    'node_user_picture'         => t('User pictures in posts'),
    'comment_user_picture'      => t('User pictures in comments'),
    'comment_user_verification' => t('User verification status in comments'),
    'favicon'                   => t('Shortcut icon'),
    'main_menu'                 => t('Main menu'),
    'secondary_menu'            => t('Secondary menu'),
  );

  // Some features are not always available
  $disabled = array();
  if (!variable_get('user_pictures', 0)) {
    $disabled['toggle_node_user_picture'] = TRUE;
    $disabled['toggle_comment_user_picture'] = TRUE;
  }
  if (!module_exists('comment')) {
    $disabled['toggle_comment_user_picture'] = TRUE;
    $disabled['toggle_comment_user_verification'] = TRUE;
  }

  $form['theme_settings'] = array(
    '#type' => 'fieldset',
    '#title' => t('Toggle display'),
    '#description' => t('Enable or disable the display of certain page elements.'),
  );
  foreach ($toggles as $name => $title) {
    if ((!$key) || in_array($name, $features)) {
      $form['theme_settings']['toggle_' . $name] = array('#type' => 'checkbox', '#title' => $title, '#default_value' => theme_get_setting('toggle_' . $name, $key));
      // Disable checkboxes for features not supported in the current configuration.
      if (isset($disabled['toggle_' . $name])) {
        $form['theme_settings']['toggle_' . $name]['#disabled'] = TRUE;
      }
    }
  }

  if (!element_children($form['theme_settings'])) {
    // If there is no element in the theme settings fieldset then do not show
    // it -- but keep it in the form if another module wants to alter.
    $form['theme_settings']['#access'] = FALSE;
  }

  // Logo settings
  if ((!$key) || in_array('logo', $features)) {
    $form['logo'] = array(
      '#type' => 'fieldset',
      '#title' => t('Logo image settings'),
      '#description' => t('If toggled on, the following logo will be displayed.'),
      '#attributes' => array('class' => array('theme-settings-bottom')),
    );
    $form['logo']['default_logo'] = array(
      '#type' => 'checkbox',
      '#title' => t('Use the default logo'),
      '#default_value' => theme_get_setting('default_logo', $key),
      '#tree' => FALSE,
      '#description' => t('Check here if you want the theme to use the logo supplied with it.')
    );
    $form['logo']['settings'] = array(
      '#type' => 'container',
      '#states' => array(
        // Hide the logo settings when using the default logo.
        'invisible' => array(
          'input[name="default_logo"]' => array('checked' => TRUE),
        ),
      ),
    );
    $form['logo']['settings']['logo_path'] = array(
      '#type' => 'textfield',
      '#title' => t('Path to custom logo'),
      '#description' => t('The path to the file you would like to use as your logo file instead of the default logo.'),
      '#default_value' => theme_get_setting('logo_path', $key),
    );
    $form['logo']['settings']['logo_upload'] = array(
      '#type' => 'file',
      '#title' => t('Upload logo image'),
      '#maxlength' => 40,
      '#description' => t("If you don't have direct file access to the server, use this field to upload your logo.")
    );
  }

  if ((!$key) || in_array('favicon', $features)) {
    $form['favicon'] = array(
      '#type' => 'fieldset',
      '#title' => t('Shortcut icon settings'),
      '#description' => t("Your shortcut icon, or 'favicon', is displayed in the address bar and bookmarks of most browsers."),
    );
    $form['favicon']['default_favicon'] = array(
      '#type' => 'checkbox',
      '#title' => t('Use the default shortcut icon.'),
      '#default_value' => theme_get_setting('default_favicon', $key),
      '#description' => t('Check here if you want the theme to use the default shortcut icon.')
    );
    $form['favicon']['settings'] = array(
      '#type' => 'container',
      '#states' => array(
        // Hide the favicon settings when using the default favicon.
        'invisible' => array(
          'input[name="default_favicon"]' => array('checked' => TRUE),
        ),
      ),
    );
    $form['favicon']['settings']['favicon_path'] = array(
      '#type' => 'textfield',
      '#title' => t('Path to custom icon'),
      '#description' => t('The path to the image file you would like to use as your custom shortcut icon.'),
      '#default_value' => theme_get_setting('favicon_path', $key),
    );
    $form['favicon']['settings']['favicon_upload'] = array(
      '#type' => 'file',
      '#title' => t('Upload icon image'),
      '#description' => t("If you don't have direct file access to the server, use this field to upload your shortcut icon.")
    );
  }

  // Inject human-friendly values for logo and favicon.
  foreach (array('logo' => 'logo.png', 'favicon' => 'favicon.ico') as $type => $default) {
    if (isset($form[$type]['settings'][$type . '_path'])) {
      $element = &$form[$type]['settings'][$type . '_path'];

      // If path is a public:// URI, display the path relative to the files
      // directory; stream wrappers are not end-user friendly.
      $original_path = $element['#default_value'];
      $friendly_path = NULL;
      if (file_uri_scheme($original_path) == 'public') {
        $friendly_path = file_uri_target($original_path);
        $element['#default_value'] = $friendly_path;
      }
    }
  }

  if ($key) {
    // Call engine-specific settings.
    $function = $themes[$key]->prefix . '_engine_settings';
    if (function_exists($function)) {
      $form['engine_specific'] = array(
        '#type' => 'fieldset',
        '#title' => t('Theme-engine-specific settings'),
        '#description' => t('These settings only exist for the themes based on the %engine theme engine.', array('%engine' => $themes[$key]->prefix)),
      );
      $function($form, $form_state);
    }

    // Create a list which includes the current theme and all its base themes.
    if (isset($themes[$key]->base_themes)) {
      $theme_keys = array_keys($themes[$key]->base_themes);
      $theme_keys[] = $key;
    }
    else {
      $theme_keys = array($key);
    }

    // Save the name of the current theme (if any), so that we can temporarily
    // override the current theme and allow theme_get_setting() to work
    // without having to pass the theme name to it.
    $default_theme = !empty($GLOBALS['theme_key']) ? $GLOBALS['theme_key'] : NULL;
    $GLOBALS['theme_key'] = $key;

    // Process the theme and all its base themes.
    foreach ($theme_keys as $theme) {
      // Include the theme-settings.php file.
      $theme_settings_path = drupal_get_path('theme', $theme) . '/theme-settings.php';
      if (file_exists(DRUPAL_ROOT . '/' . $theme_settings_path)) {
        require_once DRUPAL_ROOT . '/' . $theme_settings_path;
        $form_state['build_info']['files'][] = $theme_settings_path;
      }

      // Call theme-specific settings.
      $function = $theme . '_form_system_theme_settings_alter';
      if (function_exists($function)) {
        $function($form, $form_state);
      }
    }

    // Restore the original current theme.
    if (isset($default_theme)) {
      $GLOBALS['theme_key'] = $default_theme;
    }
    else {
      unset($GLOBALS['theme_key']);
    }
  }

  $form = system_settings_form($form);
  // We don't want to call system_settings_form_submit(), so change #submit.
  array_pop($form['#submit']);
  $form['#submit'][] = 'system_theme_settings_submit';
  $form['#validate'][] = 'system_theme_settings_validate';
  return $form;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
