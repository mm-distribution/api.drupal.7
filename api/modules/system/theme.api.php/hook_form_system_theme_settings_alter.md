# hook_form_system_theme_settings_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/theme.api.php`](_file.md), lines 87–95 · [local source](../../../../source/modules/system/theme.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/theme.api.php#L87-L95)
- **Module/theme:** system

## Signature

```php
function hook_form_system_theme_settings_alter(&$form, &$form_state)
```

## Documentation

```text
Allow themes to alter the theme-specific settings form.

With this hook, themes can alter the theme-specific settings form in any way
allowable by Drupal's Form API, such as adding form elements, changing
default values and removing form elements. See the Form API documentation on
api.drupal.org for detailed information.

Note that the base theme's form alterations will be run before any sub-theme
alterations.

@param $form
  Nested array of form elements that comprise the form.
@param $form_state
  A keyed array containing the current state of the form.
```

## Code

```php
function hook_form_system_theme_settings_alter(&$form, &$form_state) {
  // Add a checkbox to toggle the breadcrumb trail.
  $form['toggle_breadcrumb'] = array(
    '#type' => 'checkbox',
    '#title' => t('Display the breadcrumb'),
    '#default_value' => theme_get_setting('toggle_breadcrumb'),
    '#description'   => t('Show a trail of links from the homepage to the current page.'),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_form_system_theme_settings_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/theme.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/theme.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
